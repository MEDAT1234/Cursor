"""
Video Generator for ASMR Content
Creates visually appealing videos with ASMR audio
"""

import os
import random
from datetime import datetime
from moviepy.editor import (
    ColorClip, TextClip, CompositeVideoClip, 
    AudioFileClip, concatenate_videoclips
)
from moviepy.video.fx.all import fadein, fadeout
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from asmr_generator import ASMRGenerator


class VideoGenerator:
    def __init__(self, width=1080, height=1920, duration=15, fps=30):
        self.width = width
        self.height = height
        self.duration = duration
        self.fps = fps
        self.output_dir = "generated_videos"
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_gradient_background(self, colors, duration):
        """Create an animated gradient background"""
        def make_frame(t):
            # Create gradient that changes over time
            img = Image.new('RGB', (self.width, self.height))
            draw = ImageDraw.Draw(img)
            
            # Interpolate between colors based on time
            progress = (t / duration) % 1.0
            color_index = int(progress * (len(colors) - 1))
            next_color_index = (color_index + 1) % len(colors)
            
            color1 = colors[color_index]
            color2 = colors[next_color_index]
            
            local_progress = (progress * (len(colors) - 1)) % 1.0
            
            # Create vertical gradient
            for y in range(self.height):
                ratio = y / self.height
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                
                # Add time-based color interpolation
                r = int(r * (1 - local_progress) + color2[0] * local_progress)
                g = int(g * (1 - local_progress) + color2[1] * local_progress)
                b = int(b * (1 - local_progress) + color2[2] * local_progress)
                
                draw.line([(0, y), (self.width, y)], fill=(r, g, b))
            
            return np.array(img)
        
        return make_frame
    
    def create_rain_visual(self):
        """Create rain-themed visual"""
        colors = [
            (20, 30, 60),    # Dark blue
            (40, 60, 100),   # Medium blue
            (60, 80, 120),   # Lighter blue
            (30, 50, 80)     # Blue-gray
        ]
        return self.create_gradient_background(colors, self.duration)
    
    def create_fire_visual(self):
        """Create fire-themed visual"""
        colors = [
            (139, 0, 0),     # Dark red
            (255, 69, 0),    # Orange-red
            (255, 140, 0),   # Dark orange
            (255, 165, 0),   # Orange
            (139, 0, 0)      # Back to dark red
        ]
        return self.create_gradient_background(colors, self.duration)
    
    def create_waves_visual(self):
        """Create ocean waves visual"""
        colors = [
            (0, 105, 148),   # Deep ocean
            (0, 119, 182),   # Ocean blue
            (3, 169, 244),   # Light blue
            (0, 150, 199),   # Cyan blue
            (0, 105, 148)    # Back to deep
        ]
        return self.create_gradient_background(colors, self.duration)
    
    def create_typing_visual(self):
        """Create typing/work themed visual"""
        colors = [
            (30, 30, 30),    # Dark gray
            (50, 50, 55),    # Medium gray
            (40, 40, 50),    # Blue-gray
            (30, 30, 30)     # Back to dark
        ]
        return self.create_gradient_background(colors, self.duration)
    
    def create_whisper_visual(self):
        """Create soft/whisper themed visual"""
        colors = [
            (147, 112, 219), # Purple
            (186, 85, 211),  # Medium orchid
            (221, 160, 221), # Plum
            (216, 191, 216), # Thistle
            (147, 112, 219)  # Back to purple
        ]
        return self.create_gradient_background(colors, self.duration)
    
    def add_floating_particles(self, duration):
        """Add floating particle effect"""
        def make_frame(t):
            img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Create particles
            num_particles = 30
            for i in range(num_particles):
                # Deterministic but seemingly random motion
                seed = i * 1000
                x = int((self.width / 2) + 
                       np.sin(t * 0.5 + seed) * (self.width * 0.4))
                y = int((self.height * (i / num_particles) + 
                       t * 50 + seed) % self.height)
                
                # Particle properties
                size = random.randint(2, 6)
                opacity = int(128 + 127 * np.sin(t + seed))
                
                draw.ellipse(
                    [x - size, y - size, x + size, y + size],
                    fill=(255, 255, 255, opacity)
                )
            
            return np.array(img)
        
        return make_frame
    
    def create_text_overlay(self, text, duration, position='center'):
        """Create animated text overlay"""
        try:
            txt_clip = TextClip(
                text,
                fontsize=80,
                color='white',
                font='Arial-Bold',
                stroke_color='black',
                stroke_width=2,
                method='caption',
                size=(self.width - 100, None)
            )
        except:
            # Fallback without stroke if not supported
            txt_clip = TextClip(
                text,
                fontsize=80,
                color='white',
                font='Arial',
                method='caption',
                size=(self.width - 100, None)
            )
        
        txt_clip = txt_clip.set_duration(duration)
        
        # Position text
        if position == 'center':
            txt_clip = txt_clip.set_position('center')
        elif position == 'top':
            txt_clip = txt_clip.set_position(('center', 100))
        elif position == 'bottom':
            txt_clip = txt_clip.set_position(('center', self.height - 300))
        
        # Add fade effects
        txt_clip = fadein(txt_clip, 0.5)
        txt_clip = fadeout(txt_clip, 0.5)
        
        return txt_clip
    
    def generate_video(self, asmr_type=None):
        """Generate a complete ASMR video"""
        print("🎬 Starting video generation...")
        
        # Generate ASMR audio
        print("🔊 Generating ASMR audio...")
        generator = ASMRGenerator(duration=self.duration)
        
        if asmr_type:
            method = getattr(generator, f'generate_{asmr_type}')
            audio_segment = method()
            asmr_name = asmr_type
        else:
            audio_segment, asmr_name = generator.generate_random_asmr()
        
        # Save audio temporarily
        temp_audio = f"temp_audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        audio_segment.export(temp_audio, format="mp3")
        audio_clip = AudioFileClip(temp_audio)
        
        print(f"✨ Creating {asmr_name} themed visuals...")
        
        # Create visual based on ASMR type
        visual_map = {
            'rain': self.create_rain_visual,
            'fire': self.create_fire_visual,
            'waves': self.create_waves_visual,
            'typing': self.create_typing_visual,
            'whisper': self.create_whisper_visual
        }
        
        visual_func = visual_map.get(asmr_name, self.create_waves_visual)
        background_frame = visual_func()
        
        # Create background clip
        background = ColorClip(
            size=(self.width, self.height),
            color=(0, 0, 0),
            duration=self.duration
        ).set_fps(self.fps)
        
        background = background.fl(lambda gf, t: background_frame(t))
        
        # Create text overlays
        title_map = {
            'rain': 'Relaxing Rain Sounds 🌧️',
            'fire': 'Cozy Fireplace Sounds 🔥',
            'waves': 'Peaceful Ocean Waves 🌊',
            'typing': 'Satisfying Typing ASMR ⌨️',
            'whisper': 'Soft Whisper ASMR 💜'
        }
        
        title = title_map.get(asmr_name, 'ASMR Sounds')
        
        # Title text
        title_clip = self.create_text_overlay(title, 3, 'center')
        
        # Bottom text
        bottom_text = self.create_text_overlay(
            'Like & Follow for more! 💤',
            self.duration,
            'bottom'
        ).set_start(self.duration - 3)
        
        # Composite video
        print("🎨 Compositing video...")
        video = CompositeVideoClip(
            [background, title_clip, bottom_text],
            size=(self.width, self.height)
        )
        
        # Add audio
        video = video.set_audio(audio_clip)
        
        # Generate output filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(
            self.output_dir,
            f"asmr_{asmr_name}_{timestamp}.mp4"
        )
        
        # Write video file
        print(f"💾 Rendering video to {output_file}...")
        video.write_videofile(
            output_file,
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            preset='medium',
            threads=4
        )
        
        # Cleanup
        video.close()
        audio_clip.close()
        if os.path.exists(temp_audio):
            os.remove(temp_audio)
        
        print(f"✅ Video generated successfully: {output_file}")
        return output_file


if __name__ == "__main__":
    # Test video generation
    print("Testing Video Generator...")
    gen = VideoGenerator(duration=10)
    video_path = gen.generate_video()
    print(f"Test video created: {video_path}")
