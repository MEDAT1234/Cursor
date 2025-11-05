"""
وحدة معالجة الفيديوهات
تقوم بتطبيق تأثيرات وفلاتر على الفيديوهات لجعلها فريدة
"""

import os
import random
from pathlib import Path
from typing import Dict, List, Tuple
import cv2
import numpy as np
from moviepy.editor import (
    VideoFileClip, 
    CompositeVideoClip, 
    TextClip,
    vfx,
    AudioFileClip
)
from PIL import Image, ImageEnhance, ImageFilter
from colorama import Fore, Style, init

init(autoreset=True)


class VideoProcessor:
    """فئة لمعالجة وتعديل الفيديوهات"""
    
    def __init__(self, processed_folder: str = "processed"):
        self.processed_folder = Path(processed_folder)
        self.processed_folder.mkdir(exist_ok=True)
        self.processed_videos = []
        
    def apply_random_effects(self, input_path: str, output_path: str = None) -> str:
        """
        تطبيق تأثيرات عشوائية على الفيديو
        
        Args:
            input_path: مسار الفيديو الأصلي
            output_path: مسار الفيديو المعالج
            
        Returns:
            مسار الفيديو المعالج
        """
        if not output_path:
            filename = Path(input_path).stem
            output_path = self.processed_folder / f"{filename}_processed.mp4"
        
        print(f"{Fore.CYAN}🎬 معالجة الفيديو: {input_path}")
        
        try:
            clip = VideoFileClip(input_path)
            
            # قائمة التأثيرات المتاحة
            effects = []
            
            # 1. تغيير السرعة بشكل عشوائي (0.9x - 1.1x)
            speed_factor = random.uniform(0.90, 1.10)
            clip = clip.fx(vfx.speedx, speed_factor)
            effects.append(f"Speed: {speed_factor:.2f}x")
            
            # 2. قص الفيديو قليلاً من الحواف
            margin = 10
            w, h = clip.size
            clip = clip.crop(
                x1=margin, 
                y1=margin, 
                x2=w-margin, 
                y2=h-margin
            )
            effects.append("Cropped edges")
            
            # 3. تغيير السطوع والتباين
            brightness_factor = random.uniform(0.95, 1.05)
            clip = clip.fx(vfx.colorx, brightness_factor)
            effects.append(f"Brightness: {brightness_factor:.2f}")
            
            # 4. عكس أفقي عشوائي
            if random.random() > 0.5:
                clip = clip.fx(vfx.mirror_x)
                effects.append("Mirrored horizontally")
            
            # 5. تطبيق فلتر blur خفيف جداً ثم sharpen
            # هذا يجعل الفيديو مختلفاً قليلاً عن الأصل
            
            print(f"{Fore.GREEN}✅ التأثيرات المطبقة: {', '.join(effects)}")
            
            # حفظ الفيديو
            print(f"{Fore.CYAN}💾 حفظ الفيديو المعالج...")
            clip.write_videofile(
                str(output_path),
                codec='libx264',
                audio_codec='aac',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                fps=clip.fps,
                preset='medium',
                threads=4
            )
            
            clip.close()
            
            print(f"{Fore.GREEN}✅ تم حفظ الفيديو في: {output_path}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في معالجة الفيديو: {str(e)}")
            return None
    
    def add_watermark(self, input_path: str, watermark_text: str, 
                     output_path: str = None) -> str:
        """
        إضافة علامة مائية نصية على الفيديو
        
        Args:
            input_path: مسار الفيديو الأصلي
            watermark_text: النص المراد إضافته
            output_path: مسار الفيديو المعالج
            
        Returns:
            مسار الفيديو المعالج
        """
        if not output_path:
            filename = Path(input_path).stem
            output_path = self.processed_folder / f"{filename}_watermarked.mp4"
        
        print(f"{Fore.CYAN}💧 إضافة علامة مائية...")
        
        try:
            clip = VideoFileClip(input_path)
            
            # إنشاء نص العلامة المائية
            txt_clip = TextClip(
                watermark_text,
                fontsize=20,
                color='white',
                font='Arial',
                stroke_color='black',
                stroke_width=1
            )
            
            # وضع العلامة في الزاوية السفلية اليمنى
            txt_clip = txt_clip.set_position(('right', 'bottom')).set_duration(clip.duration)
            txt_clip = txt_clip.set_opacity(0.5)
            
            # دمج الفيديو مع النص
            final = CompositeVideoClip([clip, txt_clip])
            
            # حفظ الفيديو
            final.write_videofile(
                str(output_path),
                codec='libx264',
                audio_codec='aac',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True
            )
            
            clip.close()
            final.close()
            
            print(f"{Fore.GREEN}✅ تم إضافة العلامة المائية")
            
            return str(output_path)
            
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في إضافة العلامة المائية: {str(e)}")
            return None
    
    def apply_color_filter(self, input_path: str, filter_type: str = "random",
                          output_path: str = None) -> str:
        """
        تطبيق فلتر لوني على الفيديو
        
        Args:
            input_path: مسار الفيديو الأصلي
            filter_type: نوع الفلتر (warm, cool, vintage, random)
            output_path: مسار الفيديو المعالج
            
        Returns:
            مسار الفيديو المعالج
        """
        if not output_path:
            filename = Path(input_path).stem
            output_path = self.processed_folder / f"{filename}_filtered.mp4"
        
        print(f"{Fore.CYAN}🎨 تطبيق فلتر لوني: {filter_type}")
        
        try:
            clip = VideoFileClip(input_path)
            
            # اختيار فلتر عشوائي إذا لزم الأمر
            if filter_type == "random":
                filter_type = random.choice(["warm", "cool", "vintage"])
            
            def apply_filter(get_frame, t):
                frame = get_frame(t)
                
                if filter_type == "warm":
                    # فلتر دافئ (زيادة الأحمر والأصفر)
                    frame = frame.astype(np.float32)
                    frame[:, :, 0] = np.clip(frame[:, :, 0] * 1.1, 0, 255)  # Red
                    frame[:, :, 1] = np.clip(frame[:, :, 1] * 1.05, 0, 255)  # Green
                    
                elif filter_type == "cool":
                    # فلتر بارد (زيادة الأزرق)
                    frame = frame.astype(np.float32)
                    frame[:, :, 2] = np.clip(frame[:, :, 2] * 1.1, 0, 255)  # Blue
                    
                elif filter_type == "vintage":
                    # فلتر قديم
                    frame = frame.astype(np.float32)
                    frame = frame * 0.9
                    frame[:, :, 0] = np.clip(frame[:, :, 0] * 1.2, 0, 255)
                
                return frame.astype(np.uint8)
            
            filtered_clip = clip.fl(apply_filter)
            
            # حفظ الفيديو
            filtered_clip.write_videofile(
                str(output_path),
                codec='libx264',
                audio_codec='aac',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True
            )
            
            clip.close()
            filtered_clip.close()
            
            print(f"{Fore.GREEN}✅ تم تطبيق الفلتر: {filter_type}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"{Fore.RED}❌ خطأ في تطبيق الفلتر: {str(e)}")
            return None
    
    def process_video_complete(self, input_path: str, 
                               apply_filter: bool = True,
                               add_watermark_text: str = None,
                               output_path: str = None) -> Dict:
        """
        معالجة كاملة للفيديو (جميع التأثيرات)
        
        Args:
            input_path: مسار الفيديو الأصلي
            apply_filter: تطبيق فلتر لوني
            add_watermark_text: نص العلامة المائية
            output_path: مسار الفيديو المعالج
            
        Returns:
            معلومات الفيديو المعالج
        """
        if not output_path:
            filename = Path(input_path).stem
            output_path = self.processed_folder / f"{filename}_final.mp4"
        
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}🎥 بدء المعالجة الكاملة للفيديو")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        
        current_path = input_path
        
        # 1. تطبيق التأثيرات العشوائية
        temp_path1 = self.processed_folder / f"temp1_{Path(input_path).name}"
        current_path = self.apply_random_effects(current_path, str(temp_path1))
        
        if not current_path:
            return None
        
        # 2. تطبيق الفلتر اللوني
        if apply_filter:
            temp_path2 = self.processed_folder / f"temp2_{Path(input_path).name}"
            current_path = self.apply_color_filter(current_path, "random", str(temp_path2))
            
            if not current_path:
                return None
            
            # حذف الملف المؤقت الأول
            if temp_path1.exists():
                temp_path1.unlink()
        
        # 3. إضافة العلامة المائية
        if add_watermark_text:
            current_path = self.add_watermark(current_path, add_watermark_text, str(output_path))
            
            # حذف الملف المؤقت الثاني
            if apply_filter and temp_path2.exists():
                temp_path2.unlink()
        else:
            # نقل الملف النهائي
            if apply_filter:
                os.rename(current_path, output_path)
                current_path = str(output_path)
        
        if not current_path:
            return None
        
        # معلومات الفيديو المعالج
        video_info = {
            'original_path': input_path,
            'processed_path': current_path,
            'effects_applied': True,
            'filter_applied': apply_filter,
            'watermark_added': bool(add_watermark_text)
        }
        
        self.processed_videos.append(video_info)
        
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{Fore.GREEN}✅ اكتملت المعالجة بنجاح!")
        print(f"{Fore.GREEN}{'='*60}\n")
        
        return video_info
    
    def process_multiple_videos(self, video_paths: List[str], **kwargs) -> List[Dict]:
        """
        معالجة عدة فيديوهات
        
        Args:
            video_paths: قائمة مسارات الفيديوهات
            **kwargs: معاملات إضافية لـ process_video_complete
            
        Returns:
            قائمة معلومات الفيديوهات المعالجة
        """
        print(f"{Fore.CYAN}📊 معالجة {len(video_paths)} فيديو...\n")
        
        processed = []
        for i, path in enumerate(video_paths, 1):
            print(f"\n{Fore.YELLOW}[{i}/{len(video_paths)}] معالجة: {Path(path).name}")
            
            video_info = self.process_video_complete(path, **kwargs)
            
            if video_info:
                processed.append(video_info)
        
        print(f"\n{Fore.GREEN}✅ تمت معالجة {len(processed)} فيديو بنجاح!")
        return processed
    
    def get_processed_videos(self) -> List[Dict]:
        """الحصول على قائمة الفيديوهات المعالجة"""
        return self.processed_videos


if __name__ == "__main__":
    # مثال على الاستخدام
    processor = VideoProcessor()
    
    print(f"{Fore.YELLOW}⚠️  للاستخدام، قم بتوفير مسار الفيديو المراد معالجته")
    print(f"{Fore.YELLOW}   مثال:")
    print(f"{Fore.YELLOW}   processor.process_video_complete('downloads/video.mp4')")
