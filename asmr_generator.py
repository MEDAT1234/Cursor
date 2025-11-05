"""
ASMR Audio Generator
Generates various types of ASMR sounds programmatically
"""

import numpy as np
from scipy import signal
from pydub import AudioSegment
from pydub.generators import WhiteNoise, Sine
import random
import io


class ASMRGenerator:
    def __init__(self, duration=15, sample_rate=44100):
        self.duration = duration
        self.sample_rate = sample_rate
        self.samples = int(duration * sample_rate)
    
    def generate_rain(self):
        """Generate rain sound using filtered white noise"""
        # Generate white noise
        noise = np.random.normal(0, 1, self.samples)
        
        # Apply low-pass filter for rain effect
        nyquist = self.sample_rate / 2
        cutoff = 4000 / nyquist
        b, a = signal.butter(4, cutoff, btype='low')
        filtered = signal.filtfilt(b, a, noise)
        
        # Add occasional droplets (higher frequency bursts)
        for _ in range(random.randint(50, 100)):
            pos = random.randint(0, self.samples - 1000)
            droplet = np.random.normal(0, 0.5, 1000) * np.exp(-np.linspace(0, 5, 1000))
            filtered[pos:pos+1000] += droplet
        
        # Normalize
        filtered = filtered / np.max(np.abs(filtered)) * 0.7
        return self._to_audio_segment(filtered)
    
    def generate_fire(self):
        """Generate crackling fire sound"""
        # Base crackling using pink noise
        noise = self._generate_pink_noise()
        
        # Add random crackles
        for _ in range(random.randint(100, 200)):
            pos = random.randint(0, self.samples - 500)
            crackle_len = random.randint(100, 500)
            crackle = np.random.normal(0, random.uniform(0.3, 0.8), crackle_len)
            crackle *= np.exp(-np.linspace(0, 10, crackle_len))
            noise[pos:pos+crackle_len] += crackle
        
        # Apply band-pass filter
        nyquist = self.sample_rate / 2
        low = 100 / nyquist
        high = 2000 / nyquist
        b, a = signal.butter(3, [low, high], btype='band')
        filtered = signal.filtfilt(b, a, noise)
        
        # Normalize
        filtered = filtered / np.max(np.abs(filtered)) * 0.7
        return self._to_audio_segment(filtered)
    
    def generate_waves(self):
        """Generate ocean waves sound"""
        # Base wave sound using modulated noise
        noise = np.random.normal(0, 1, self.samples)
        
        # Apply low-pass filter
        nyquist = self.sample_rate / 2
        cutoff = 1500 / nyquist
        b, a = signal.butter(5, cutoff, btype='low')
        filtered = signal.filtfilt(b, a, noise)
        
        # Add wave rhythm (slow amplitude modulation)
        t = np.linspace(0, self.duration, self.samples)
        wave_rhythm = 0.3 + 0.7 * (np.sin(2 * np.pi * 0.2 * t) * 0.5 + 0.5)
        filtered *= wave_rhythm
        
        # Add occasional wave crashes
        for _ in range(random.randint(3, 8)):
            pos = random.randint(0, self.samples - self.sample_rate * 2)
            crash_len = self.sample_rate * 2
            crash = np.random.normal(0, 0.8, crash_len)
            crash *= np.exp(-np.linspace(0, 3, crash_len))
            b2, a2 = signal.butter(4, 2000 / nyquist, btype='low')
            crash = signal.filtfilt(b2, a2, crash)
            filtered[pos:pos+crash_len] += crash
        
        # Normalize
        filtered = filtered / np.max(np.abs(filtered)) * 0.7
        return self._to_audio_segment(filtered)
    
    def generate_typing(self):
        """Generate keyboard typing sound"""
        audio = np.zeros(self.samples)
        
        # Simulate typing rhythm
        keys_per_second = random.uniform(3, 6)
        num_keys = int(self.duration * keys_per_second)
        
        for i in range(num_keys):
            # Random position with typing rhythm
            if i == 0:
                pos = random.randint(0, self.sample_rate // 4)
            else:
                pos = int(i / keys_per_second * self.sample_rate) + random.randint(-1000, 1000)
            
            if pos < 0 or pos >= self.samples - 2000:
                continue
            
            # Generate key press sound
            key_len = random.randint(800, 1200)
            freq = random.uniform(800, 1500)
            t = np.linspace(0, key_len / self.sample_rate, key_len)
            
            # Click sound with quick decay
            key_sound = np.sin(2 * np.pi * freq * t) * np.exp(-t * 50)
            # Add noise component
            key_sound += np.random.normal(0, 0.1, key_len) * np.exp(-t * 40)
            
            audio[pos:pos+key_len] += key_sound * random.uniform(0.4, 0.7)
        
        # Normalize
        audio = audio / np.max(np.abs(audio)) * 0.7
        return self._to_audio_segment(audio)
    
    def generate_whisper(self):
        """Generate whispering/breathing ASMR sound"""
        audio = np.zeros(self.samples)
        
        # Generate breathing pattern
        breaths = random.randint(8, 15)
        for i in range(breaths):
            pos = int((i / breaths) * self.samples)
            breath_len = int(self.sample_rate * random.uniform(0.8, 1.5))
            
            if pos + breath_len >= self.samples:
                breath_len = self.samples - pos - 1
            
            # Create breath sound using filtered noise
            breath = np.random.normal(0, 0.3, breath_len)
            
            # Apply envelope (breath in and out)
            envelope = np.sin(np.linspace(0, np.pi, breath_len)) ** 2
            breath *= envelope
            
            # Apply band-pass filter for whisper quality
            nyquist = self.sample_rate / 2
            low = 1000 / nyquist
            high = 8000 / nyquist
            b, a = signal.butter(4, [low, high], btype='band')
            breath = signal.filtfilt(b, a, breath)
            
            audio[pos:pos+breath_len] += breath
        
        # Add soft whisper elements
        for _ in range(random.randint(20, 40)):
            pos = random.randint(0, self.samples - 5000)
            whisper_len = random.randint(2000, 5000)
            whisper = np.random.normal(0, 0.2, whisper_len)
            
            # High-pass filter for whisper
            nyquist = self.sample_rate / 2
            b, a = signal.butter(3, 3000 / nyquist, btype='high')
            whisper = signal.filtfilt(b, a, whisper)
            whisper *= np.exp(-np.linspace(0, 3, whisper_len))
            
            audio[pos:pos+whisper_len] += whisper * 0.5
        
        # Normalize
        audio = audio / np.max(np.abs(audio)) * 0.6
        return self._to_audio_segment(audio)
    
    def _generate_pink_noise(self):
        """Generate pink noise (1/f noise)"""
        white = np.random.randn(self.samples)
        # Simple pink noise approximation using cascaded filters
        b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
        a = [1, -2.494956002, 2.017265875, -0.522189400]
        pink = signal.lfilter(b, a, white)
        return pink / np.max(np.abs(pink))
    
    def _to_audio_segment(self, audio_array):
        """Convert numpy array to AudioSegment"""
        # Convert to 16-bit PCM
        audio_int16 = np.int16(audio_array * 32767)
        
        # Create AudioSegment
        audio_segment = AudioSegment(
            audio_int16.tobytes(),
            frame_rate=self.sample_rate,
            sample_width=2,
            channels=1
        )
        return audio_segment
    
    def generate_random_asmr(self):
        """Generate a random ASMR sound"""
        asmr_types = [
            self.generate_rain,
            self.generate_fire,
            self.generate_waves,
            self.generate_typing,
            self.generate_whisper
        ]
        asmr_func = random.choice(asmr_types)
        return asmr_func(), asmr_func.__name__.replace('generate_', '')


if __name__ == "__main__":
    # Test the generator
    print("Testing ASMR Generator...")
    generator = ASMRGenerator(duration=5)
    
    for asmr_type in ['rain', 'fire', 'waves', 'typing', 'whisper']:
        print(f"Generating {asmr_type} sound...")
        method = getattr(generator, f'generate_{asmr_type}')
        audio = method()
        audio.export(f"test_{asmr_type}.mp3", format="mp3")
        print(f"Saved test_{asmr_type}.mp3")
