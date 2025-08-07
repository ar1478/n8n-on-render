# video_generator.py - Healing Video Creation Engine
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import tempfile
import random
import math
from datetime import datetime
import requests
import subprocess

class HealingVideoGenerator:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.fps = 30
        
        # Healing color palettes
        self.color_themes = {
            'chakra': [
                (255, 0, 0),    # Root - Red
                (255, 165, 0),  # Sacral - Orange  
                (255, 255, 0),  # Solar Plexus - Yellow
                (0, 255, 0),    # Heart - Green
                (0, 191, 255),  # Throat - Light Blue
                (75, 0, 130),   # Third Eye - Indigo
                (238, 130, 238) # Crown - Violet
            ],
            'ocean_waves': [
                (0, 119, 190),   # Deep Ocean
                (0, 180, 216),   # Ocean Blue
                (144, 224, 239), # Light Blue
                (173, 216, 230), # Powder Blue
                (240, 248, 255)  # Alice Blue
            ],
            'forest_meditation': [
                (34, 139, 34),   # Forest Green
                (107, 142, 35),  # Olive Drab
                (154, 205, 50),  # Yellow Green
                (144, 238, 144), # Light Green
                (240, 255, 240)  # Honeydew
            ],
            'sacred_geometry': [
                (138, 43, 226),  # Blue Violet
                (147, 112, 219), # Medium Purple
                (221, 160, 221), # Plum
                (255, 182, 193), # Light Pink
                (255, 240, 245)  # Lavender Blush
            ],
            'crystal_healing': [
                (230, 230, 250), # Lavender
                (221, 160, 221), # Plum
                (255, 192, 203), # Pink
                (255, 255, 224), # Light Yellow
                (240, 255, 255)  # Azure
            ],
            'sunset_peace': [
                (255, 94, 77),   # Sunset Red
                (255, 154, 0),   # Orange
                (255, 206, 84),  # Golden
                (255, 238, 173), # Light Golden
                (255, 248, 220)  # Cornsilk
            ],
            'northern_lights': [
                (0, 255, 127),   # Spring Green
                (64, 224, 208),  # Turquoise
                (138, 43, 226),  # Blue Violet
                (186, 85, 211),  # Medium Orchid
                (221, 160, 221)  # Plum
            ],
            'mandala_flow': [
                (255, 215, 0),   # Gold
                (255, 140, 0),   # Dark Orange
                (220, 20, 60),   # Crimson
                (128, 0, 128),   # Purple
                (75, 0, 130)     # Indigo
            ]
        }
        
        # Healing frequencies (Hz)
        self.frequencies = {
            '396hz': 396,  # Liberating Guilt and Fear
            '417hz': 417,  # Undoing Situations and Facilitating Change
            '528hz': 528,  # Love frequency, DNA repair
            '639hz': 639,  # Connecting/Relationships
            '741hz': 741,  # Awakening Intuition
            '852hz': 852,  # Returning to Spiritual Order
            '963hz': 963   # Crown Chakra
        }

    def create_healing_video(self, theme='chakra', frequency='432hz', duration=300):
        """Create a healing video with specified parameters"""
        print(f"🎨 Creating {theme} video with {frequency} frequency")
        
        # Create temporary file for video
        temp_video = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)
        temp_video.close()
        
        try:
            # Generate visual frames
            frames = self.generate_visual_frames(theme, duration)
            
            # Create video from frames
            self.create_video_from_frames(frames, temp_video.name)
            
            # Add healing frequency audio
            self.add_healing_audio(temp_video.name, frequency, duration)
            
            print(f"✅ Video created: {temp_video.name}")
            return temp_video.name
            
        except Exception as e:
            print(f"❌ Error creating video: {e}")
            if os.path.exists(temp_video.name):
                os.unlink(temp_video.name)
            raise

    def generate_visual_frames(self, theme, duration):
        """Generate healing visual frames"""
        total_frames = duration * self.fps
        colors = self.color_themes.get(theme, self.color_themes['chakra'])
        frames = []
        
        print(f"🎬 Generating {total_frames} frames...")
        
        for frame_num in range(total_frames):
            frame = self.create_healing_frame(frame_num, total_frames, colors, theme)
            frames.append(frame)
            
            # Progress indicator
            if frame_num % (total_frames // 10) == 0:
                progress = (frame_num / total_frames) * 100
                print(f"📊 Progress: {progress:.1f}%")
        
        return frames

    def create_healing_frame(self, frame_num, total_frames, colors, theme):
        """Create individual healing frame based on theme"""
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        if theme == 'chakra':
            frame = self.create_chakra_frame(frame_num, total_frames, colors)
        elif theme == 'sacred_geometry':
            frame = self.create_sacred_geometry_frame(frame_num, total_frames, colors)
        elif theme == 'ocean_waves':
            frame = self.create_wave_frame(frame_num, total_frames, colors)
        elif theme == 'mandala_flow':
            frame = self.create_mandala_frame(frame_num, total_frames, colors)
        else:
            frame = self.create_gradient_frame(frame_num, total_frames, colors)
        
        return frame

    def create_chakra_frame(self, frame_num, total_frames, colors):
        """Create chakra-themed healing frame"""
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        # Cycle through chakra colors
        color_cycle_length = total_frames // len(colors)
        current_color_index = (frame_num // color_cycle_length) % len(colors)
        next_color_index = (current_color_index + 1) % len(colors)
        
        # Smooth color transition
        progress = (frame_num % color_cycle_length) / color_cycle_length
        current_color = colors[current_color_index]
        next_color = colors[next_color_index]
        
        # Interpolate colors
        blended_color = [
            int(current_color[i] * (1 - progress) + next_color[i] * progress)
            for i in range(3)
        ]
        
        # Create radial gradient
        center_x, center_y = self.width // 2, self.height // 2
        max_distance = math.sqrt(center_x**2 + center_y**2)
        
        for y in range(self.height):
            for x in range(self.width):
                distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                intensity = 1 - (distance / max_distance)
                
                # Add breathing effect
                breathing = 0.8 + 0.2 * math.sin(frame_num * 0.1)
                intensity *= breathing
                
                frame[y, x] = [int(blended_color[i] * intensity) for i in range(3)]
        
        return frame

    def create_sacred_geometry_frame(self, frame_num, total_frames, colors):
        """Create sacred geometry patterns"""
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        # Create PIL image for better drawing
        pil_image = Image.fromarray(frame)
        draw = ImageDraw.Draw(pil_image)
        
        center_x, center_y = self.width // 2, self.height // 2
        
        # Rotating sacred geometry
        rotation = (frame_num / total_frames) * 360 * 2  # 2 full rotations
        
        # Draw flower of life pattern
        radius = 80
        num_circles = 7
        
        for i in range(num_circles):
            angle = (i * 60) + rotation
            offset_x = radius * math.cos(math.radians(angle))
            offset_y = radius * math.sin(math.radians(angle))
            
            color_index = i % len(colors)
            color = colors[color_index]
            
            # Draw circle
            x = center_x + offset_x - radius//2
            y = center_y + offset_y - radius//2
            draw.ellipse([x, y, x + radius, y + radius], outline=color, width=3)
        
        # Convert back to numpy array
        return np.array(pil_image)

    def create_wave_frame(self, frame_num, total_frames, colors):
        """Create ocean wave patterns"""
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        time = frame_num / self.fps
        
        for y in range(self.height):
            for x in range(self.width):
                # Create wave pattern
                wave1 = math.sin((x * 0.01) + (time * 2)) * 0.5 + 0.5
                wave2 = math.sin((y * 0.008) + (time * 1.5)) * 0.5 + 0.5
                wave3 = math.sin(((x + y) * 0.005) + (time * 1)) * 0.5 + 0.5
                
                # Combine waves
                combined_wave = (wave1 + wave2 + wave3) / 3
                
                # Map to colors
                color_index = int(combined_wave * (len(colors) - 1))
                color = colors[color_index]
                
                frame[y, x] = color
        
        return frame

    def create_mandala_frame(self, frame_num, total_frames, colors):
        """Create mandala patterns"""
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        center_x, center_y = self.width // 2, self.height // 2
        time = frame_num / total_frames * 2 * math.pi
        
        for y in range(self.height):
            for x in range(self.width):
                # Convert to polar coordinates
                dx = x - center_x
                dy = y - center_y
                distance = math.sqrt(dx*dx + dy*dy)
                angle = math.atan2(dy, dx)
                
                # Create mandala pattern
                pattern = math.sin(distance * 0.02 + time) * math.sin(angle * 8 + time)
                pattern = (pattern + 1) / 2  # Normalize to 0-1
                
                # Map to colors
                color_index = int(pattern * (len(colors) - 1))
                color = colors[color_index]
                
                frame[y, x] = color
        
        return frame

    def create_gradient_frame(self, frame_num, total_frames, colors):
        """Create simple gradient frame"""
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        # Cycle through colors
        progress = frame_num / total_frames
        color_index = int(progress * len(colors)) % len(colors)
        next_index = (color_index + 1) % len(colors)
        
        blend_progress = (progress * len(colors)) % 1
        current_color = colors[color_index]
        next_color = colors[next_index]
        
        # Create vertical gradient
        for y in range(self.height):
            gradient_progress = y / self.height
            
            # Blend colors based on position and time
            final_color = [
                int(current_color[i] * (1 - gradient_progress) + next_color[i] * gradient_progress)
                for i in range(3)
            ]
            
            frame[y, :] = final_color
        
        return frame

    def create_video_from_frames(self, frames, output_path):
        """Convert frames to video"""
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, self.fps, (self.width, self.height))
        
        for frame in frames:
            # Convert RGB to BGR for OpenCV
            bgr_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(bgr_frame)
        
        out.release()

    def add_healing_audio(self, video_path, frequency_name, duration):
        """Add healing frequency audio to video"""
        frequency = self.frequencies.get(frequency_name, 432)
        
        # Generate sine wave audio
        temp_audio = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        temp_audio.close()
        
        # Create audio using ffmpeg
        cmd = [
            'ffmpeg', '-y',
            '-f', 'lavfi',
            '-i', f'sine=frequency={frequency}:duration={duration}',
            '-ar', '44100',
            '-ac', '1',
            temp_audio.name
        ]
        
        subprocess.run(cmd, check=True, capture_output=True)
        
        # Combine video and audio
        temp_final = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)
        temp_final.close()
        
        cmd = [
            'ffmpeg', '-y',
            '-i', video_path,
            '-i', temp_audio.name,
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-shortest',
            temp_final.name
        ]
        
        subprocess.run(cmd, check=True, capture_output=True)
        
        # Replace original video
        os.replace(temp_final.name, video_path)
        
        # Cleanup
        os.unlink(temp_audio.name)
