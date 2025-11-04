"""
Discord Auto Sender (Remote) - Multitasking Bot
A powerful automation tool for managing multiple Discord channels with message automation
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import random
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from datetime import datetime
from queue import Queue
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('discord_bot.log'),
        logging.StreamHandler()
    ]
)

class DiscordAutoSender:
    def __init__(self, root):
        self.root = root
        self.root.title("Discord Auto Sender (Remote)")
        self.root.geometry("900x700")
        self.root.configure(bg='#2C2F33')
        
        # Bot state
        self.is_running = False
        self.is_paused = False
        self.drivers = {}
        self.channels = []
        self.messages = []
        self.current_channel_index = 0
        self.message_queue = Queue()
        self.worker_threads = []
        
        # Configuration
        self.config = {
            'chrome_path': '',
            'chromedriver_path': '',
            'remote_port': '9222',
            'delay_min': 60,
            'delay_max': 100,
            'channel_mode': 1,  # 0=random, 1=first, 2=sequential
            'notifications': True
        }
        
        self.load_config()
        self.create_ui()
        
    def create_ui(self):
        """Create the user interface"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="Discord Auto Sender (Remote)", 
            font=("Arial", 20, "bold"),
            bg='#2C2F33', 
            fg='#FF9900'
        )
        title_label.pack(pady=10)
        
        # Configuration Frame
        config_frame = tk.LabelFrame(
            self.root, 
            text="Configuration", 
            bg='#23272A', 
            fg='white',
            font=("Arial", 10, "bold"),
            padx=10, 
            pady=10
        )
        config_frame.pack(padx=20, pady=10, fill="x")
        
        # Chrome Path
        self.create_config_row(config_frame, "Chrome Path:", 'chrome_path', 0)
        
        # Chromedriver Path
        self.create_config_row(config_frame, "Chromedriver Path:", 'chromedriver_path', 1)
        
        # Remote Debugging Port
        self.create_config_row(config_frame, "Remote Debugging Port:", 'remote_port', 2, width=10)
        
        # Delay Range
        delay_frame = tk.Frame(config_frame, bg='#23272A')
        delay_frame.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)
        
        tk.Label(delay_frame, text="Delay Range (sec):", bg='#23272A', fg='white').pack(side="left", padx=5)
        self.delay_min_entry = tk.Entry(delay_frame, width=8, bg='#40444B', fg='white', insertbackground='white')
        self.delay_min_entry.insert(0, str(self.config['delay_min']))
        self.delay_min_entry.pack(side="left", padx=2)
        
        tk.Label(delay_frame, text="to", bg='#23272A', fg='white').pack(side="left", padx=5)
        self.delay_max_entry = tk.Entry(delay_frame, width=8, bg='#40444B', fg='white', insertbackground='white')
        self.delay_max_entry.insert(0, str(self.config['delay_max']))
        self.delay_max_entry.pack(side="left", padx=2)
        
        # Channel Mode
        mode_frame = tk.Frame(config_frame, bg='#23272A')
        mode_frame.grid(row=4, column=0, columnspan=2, sticky="w", pady=5)
        
        tk.Label(mode_frame, text="Channel Mode (0=random, 1=first, 2=sequential):", 
                bg='#23272A', fg='white').pack(side="left", padx=5)
        self.mode_entry = tk.Entry(mode_frame, width=5, bg='#40444B', fg='white', insertbackground='white')
        self.mode_entry.insert(0, str(self.config['channel_mode']))
        self.mode_entry.pack(side="left", padx=2)
        
        # Notifications
        self.notifications_var = tk.BooleanVar(value=self.config['notifications'])
        notif_check = tk.Checkbutton(
            config_frame, 
            text="Enable Notifications",
            variable=self.notifications_var,
            bg='#23272A', 
            fg='white',
            selectcolor='#40444B',
            activebackground='#23272A',
            activeforeground='white'
        )
        notif_check.grid(row=5, column=0, columnspan=2, sticky="w", pady=5)
        
        # Channel Management Frame
        channel_frame = tk.LabelFrame(
            self.root, 
            text="Channel Management", 
            bg='#23272A', 
            fg='white',
            font=("Arial", 10, "bold"),
            padx=10, 
            pady=10
        )
        channel_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Add Channel
        add_frame = tk.Frame(channel_frame, bg='#23272A')
        add_frame.pack(fill="x", pady=5)
        
        tk.Label(add_frame, text="Add Discord Channel URL:", bg='#23272A', fg='white').pack(side="left", padx=5)
        self.channel_entry = tk.Entry(add_frame, bg='#40444B', fg='white', insertbackground='white')
        self.channel_entry.pack(side="left", fill="x", expand=True, padx=5)
        
        add_btn = tk.Button(
            add_frame, 
            text="Add", 
            command=self.add_channel,
            bg='#00AFF4', 
            fg='white',
            font=("Arial", 9, "bold"),
            cursor="hand2"
        )
        add_btn.pack(side="left", padx=5)
        
        # Saved Channels List
        tk.Label(channel_frame, text="Saved Channels:", bg='#23272A', fg='white').pack(anchor="w", pady=5)
        
        self.channels_text = scrolledtext.ScrolledText(
            channel_frame, 
            height=5, 
            bg='#40444B', 
            fg='white',
            insertbackground='white'
        )
        self.channels_text.pack(fill="both", expand=True, pady=5)
        self.update_channels_display()
        
        # Control Buttons Frame
        control_frame = tk.Frame(self.root, bg='#2C2F33')
        control_frame.pack(pady=10)
        
        self.start_btn = tk.Button(
            control_frame, 
            text="▶ Start", 
            command=self.start_bot,
            bg='#43B581', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=10,
            cursor="hand2"
        )
        self.start_btn.grid(row=0, column=0, padx=5)
        
        self.pause_btn = tk.Button(
            control_frame, 
            text="⏸ Pause", 
            command=self.pause_bot,
            bg='#7289DA', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=10,
            cursor="hand2",
            state="disabled"
        )
        self.pause_btn.grid(row=0, column=1, padx=5)
        
        self.resume_btn = tk.Button(
            control_frame, 
            text="▶ Resume", 
            command=self.resume_bot,
            bg='#7289DA', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=10,
            cursor="hand2",
            state="disabled"
        )
        self.resume_btn.grid(row=0, column=2, padx=5)
        
        self.stop_btn = tk.Button(
            control_frame, 
            text="⏹ Stop", 
            command=self.stop_bot,
            bg='#F04747', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=10,
            cursor="hand2",
            state="disabled"
        )
        self.stop_btn.grid(row=0, column=3, padx=5)
        
        self.regen_btn = tk.Button(
            control_frame, 
            text="🔄 Regenerate Messages", 
            command=self.regenerate_messages,
            bg='#FF9900', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=20,
            cursor="hand2"
        )
        self.regen_btn.grid(row=0, column=4, padx=5)
        
        # Status Frame
        status_frame = tk.LabelFrame(
            self.root, 
            text="Status", 
            bg='#23272A', 
            fg='white',
            font=("Arial", 10, "bold"),
            padx=10, 
            pady=10
        )
        status_frame.pack(padx=20, pady=10, fill="x")
        
        # Generated Messages
        tk.Label(status_frame, text="Generated Messages:", bg='#23272A', fg='white').grid(row=0, column=0, sticky="w")
        self.messages_text = scrolledtext.ScrolledText(
            status_frame, 
            height=4, 
            bg='#40444B', 
            fg='white',
            insertbackground='white'
        )
        self.messages_text.grid(row=1, column=0, sticky="ew", pady=5)
        
        # Current Info
        tk.Label(status_frame, text="Current Channel:", bg='#23272A', fg='white').grid(row=2, column=0, sticky="w", pady=2)
        self.current_channel_label = tk.Label(status_frame, text="-", bg='#23272A', fg='#43B581', font=("Arial", 9))
        self.current_channel_label.grid(row=3, column=0, sticky="w")
        
        tk.Label(status_frame, text="Current Message:", bg='#23272A', fg='white').grid(row=4, column=0, sticky="w", pady=2)
        self.current_message_label = tk.Label(status_frame, text="-", bg='#23272A', fg='#43B581', font=("Arial", 9))
        self.current_message_label.grid(row=5, column=0, sticky="w")
        
        tk.Label(status_frame, text="Progress:", bg='#23272A', fg='white').grid(row=6, column=0, sticky="w", pady=2)
        self.progress_label = tk.Label(status_frame, text="0 / 0", bg='#23272A', fg='#43B581', font=("Arial", 9))
        self.progress_label.grid(row=7, column=0, sticky="w")
        
        status_frame.columnconfigure(0, weight=1)
    
    def create_config_row(self, parent, label, config_key, row, width=50):
        """Create a configuration row"""
        tk.Label(parent, text=label, bg='#23272A', fg='white').grid(row=row, column=0, sticky="w", pady=5, padx=5)
        entry = tk.Entry(parent, width=width, bg='#40444B', fg='white', insertbackground='white')
        entry.insert(0, self.config.get(config_key, ''))
        entry.grid(row=row, column=1, sticky="w", pady=5, padx=5)
        setattr(self, f"{config_key}_entry", entry)
    
    def add_channel(self):
        """Add a Discord channel URL"""
        url = self.channel_entry.get().strip()
        if url:
            if url not in self.channels:
                self.channels.append(url)
                self.update_channels_display()
                self.channel_entry.delete(0, tk.END)
                self.save_config()
                logging.info(f"Added channel: {url}")
            else:
                messagebox.showwarning("Duplicate", "This channel is already added!")
        else:
            messagebox.showwarning("Empty URL", "Please enter a channel URL!")
    
    def update_channels_display(self):
        """Update the channels display"""
        self.channels_text.delete(1.0, tk.END)
        for i, channel in enumerate(self.channels, 1):
            self.channels_text.insert(tk.END, f"{i}. {channel}\n")
    
    def regenerate_messages(self):
        """Generate random messages"""
        from message_generator import MessageGenerator
        generator = MessageGenerator()
        self.messages = generator.generate_messages(20)
        
        self.messages_text.delete(1.0, tk.END)
        for msg in self.messages[:5]:  # Show first 5
            self.messages_text.insert(tk.END, f"• {msg}\n")
        self.messages_text.insert(tk.END, f"... and {len(self.messages) - 5} more messages")
        
        logging.info(f"Generated {len(self.messages)} messages")
        if self.notifications_var.get():
            messagebox.showinfo("Success", f"Generated {len(self.messages)} messages!")
    
    def start_bot(self):
        """Start the bot"""
        if not self.channels:
            messagebox.showerror("Error", "Please add at least one channel!")
            return
        
        if not self.messages:
            self.regenerate_messages()
        
        # Update config from UI
        self.update_config_from_ui()
        
        self.is_running = True
        self.is_paused = False
        
        # Update button states
        self.start_btn.config(state="disabled")
        self.pause_btn.config(state="normal")
        self.stop_btn.config(state="normal")
        
        # Start worker threads
        self.start_workers()
        
        logging.info("Bot started!")
        if self.notifications_var.get():
            messagebox.showinfo("Started", "Bot is now running!")
    
    def start_workers(self):
        """Start worker threads for multitasking"""
        # Clear old threads
        self.worker_threads = []
        
        # Create worker thread for each channel (multitasking)
        for i, channel in enumerate(self.channels):
            thread = threading.Thread(target=self.worker_task, args=(channel, i), daemon=True)
            thread.start()
            self.worker_threads.append(thread)
            logging.info(f"Started worker thread {i+1} for channel: {channel}")
    
    def worker_task(self, channel_url, worker_id):
        """Worker task for sending messages to a channel"""
        message_count = 0
        
        while self.is_running:
            # Check if paused
            while self.is_paused and self.is_running:
                time.sleep(1)
            
            if not self.is_running:
                break
            
            try:
                # Get a random message
                if self.messages:
                    message = random.choice(self.messages)
                    
                    # Update UI
                    self.root.after(0, lambda: self.current_channel_label.config(text=channel_url[:50] + "..."))
                    self.root.after(0, lambda: self.current_message_label.config(text=message[:100] + "..."))
                    
                    # Simulate sending (replace with actual Selenium code)
                    self.send_message_to_channel(channel_url, message, worker_id)
                    
                    message_count += 1
                    self.root.after(0, lambda: self.progress_label.config(text=f"{message_count} / ∞"))
                    
                    # Random delay
                    delay = random.randint(self.config['delay_min'], self.config['delay_max'])
                    logging.info(f"Worker {worker_id}: Sent message. Waiting {delay}s...")
                    time.sleep(delay)
            
            except Exception as e:
                logging.error(f"Worker {worker_id} error: {str(e)}")
                time.sleep(5)
        
        logging.info(f"Worker {worker_id} stopped.")
    
    def send_message_to_channel(self, channel_url, message, worker_id):
        """Send a message to a Discord channel using Selenium"""
        try:
            # Initialize driver if not exists
            if worker_id not in self.drivers:
                self.drivers[worker_id] = self.init_driver()
            
            driver = self.drivers[worker_id]
            
            # Navigate to channel
            driver.get(channel_url)
            time.sleep(2)
            
            # Find message input and send
            # Note: This is a simplified version. Actual implementation needs proper selectors
            try:
                # Wait for message box
                message_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
                )
                
                message_box.click()
                message_box.send_keys(message)
                time.sleep(0.5)
                
                # Send button or Enter key
                message_box.send_keys("\n")
                
                logging.info(f"Worker {worker_id}: Message sent to {channel_url}")
                
            except Exception as e:
                logging.error(f"Worker {worker_id}: Failed to send message: {str(e)}")
        
        except Exception as e:
            logging.error(f"Worker {worker_id}: Driver error: {str(e)}")
    
    def init_driver(self):
        """Initialize Selenium WebDriver"""
        chrome_options = Options()
        chrome_options.add_argument(f"--remote-debugging-port={self.config['remote_port']}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Use custom paths if provided
        if self.config['chrome_path']:
            chrome_options.binary_location = self.config['chrome_path']
        
        service = None
        if self.config['chromedriver_path']:
            service = Service(self.config['chromedriver_path'])
        
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    
    def pause_bot(self):
        """Pause the bot"""
        self.is_paused = True
        self.pause_btn.config(state="disabled")
        self.resume_btn.config(state="normal")
        logging.info("Bot paused")
    
    def resume_bot(self):
        """Resume the bot"""
        self.is_paused = False
        self.pause_btn.config(state="normal")
        self.resume_btn.config(state="disabled")
        logging.info("Bot resumed")
    
    def stop_bot(self):
        """Stop the bot"""
        self.is_running = False
        self.is_paused = False
        
        # Close all drivers
        for driver in self.drivers.values():
            try:
                driver.quit()
            except:
                pass
        self.drivers = {}
        
        # Update button states
        self.start_btn.config(state="normal")
        self.pause_btn.config(state="disabled")
        self.resume_btn.config(state="disabled")
        self.stop_btn.config(state="disabled")
        
        logging.info("Bot stopped")
        if self.notifications_var.get():
            messagebox.showinfo("Stopped", "Bot has been stopped!")
    
    def update_config_from_ui(self):
        """Update configuration from UI entries"""
        self.config['chrome_path'] = self.chrome_path_entry.get()
        self.config['chromedriver_path'] = self.chromedriver_path_entry.get()
        self.config['remote_port'] = self.remote_port_entry.get()
        
        try:
            self.config['delay_min'] = int(self.delay_min_entry.get())
            self.config['delay_max'] = int(self.delay_max_entry.get())
            self.config['channel_mode'] = int(self.mode_entry.get())
        except ValueError:
            pass
        
        self.config['notifications'] = self.notifications_var.get()
        self.save_config()
    
    def load_config(self):
        """Load configuration from file"""
        if os.path.exists('config.json'):
            try:
                with open('config.json', 'r') as f:
                    data = json.load(f)
                    self.config.update(data.get('config', {}))
                    self.channels = data.get('channels', [])
                    logging.info("Configuration loaded")
            except Exception as e:
                logging.error(f"Failed to load config: {str(e)}")
    
    def save_config(self):
        """Save configuration to file"""
        try:
            data = {
                'config': self.config,
                'channels': self.channels
            }
            with open('config.json', 'w') as f:
                json.dump(data, f, indent=4)
            logging.info("Configuration saved")
        except Exception as e:
            logging.error(f"Failed to save config: {str(e)}")
    
    def on_closing(self):
        """Handle window closing"""
        if self.is_running:
            if messagebox.askokcancel("Quit", "Bot is running. Do you want to stop and quit?"):
                self.stop_bot()
                self.root.destroy()
        else:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = DiscordAutoSender(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
