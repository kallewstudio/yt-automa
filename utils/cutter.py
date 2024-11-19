import moviepy.video.io.VideoFileClip as mpy
import os
from datetime import datetime
import random

def generate_unique_filename():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_number = random.randint(100, 999)
    return f"{timestamp}_{random_number}"

def export_clips(video_path, segments, output_dir, title):
    """
    Exporta os segmentos de vídeo detectados para uma pasta com o título do vídeo.
    """
    # Criar pasta com o título do vídeo
    title_dir = os.path.join(output_dir, title)
    if not os.path.exists(title_dir):
        os.makedirs(title_dir)

    for i, (start, end) in enumerate(segments):
        output_path = os.path.join(title_dir, f"{generate_unique_filename()}.mp4")
        clip = mpy.VideoFileClip(video_path).subclip(start, end)
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Clip exportado: {output_path}")
