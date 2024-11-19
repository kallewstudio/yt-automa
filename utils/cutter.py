from moviepy.video.VideoClip import ImageClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from PIL import Image, ImageFilter
import numpy as np
import os
from datetime import datetime
import random


def generate_unique_filename():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_number = random.randint(100, 999)
    return f"{timestamp}_{random_number}"


def create_vertical_video(clip, output_width=1080, output_height=1920):
    """
    Cria um vídeo vertical com o vídeo original centralizado e um fundo desfocado.
    """
    # Extrair um frame do vídeo para criar o fundo desfocado
    frame = clip.get_frame(0)  # Obtém o primeiro frame do vídeo
    frame_image = Image.fromarray(frame)

    # Aplicar desfoque no frame
    blurred_image = frame_image.filter(ImageFilter.GaussianBlur(50))

    # Converter a imagem desfocada de volta para um array NumPy
    blurred_array = np.array(blurred_image)

    # Criar o fundo desfocado e ajustá-lo para a proporção 1080x1920
    blurred_background = ImageClip(blurred_array).resize(
        height=output_height, width=output_width
    ).set_duration(clip.duration)

    # Redimensionar o vídeo original para caber no centro (altura fixa 1080px)
    centered_video = clip.resize(height=1080)  # Mantém proporção original 16:9

    # Compor o vídeo com o fundo desfocado
    final_video = CompositeVideoClip(
        [blurred_background, centered_video.set_position("center")],
        size=(output_width, output_height)  # Saída 1080x1920
    )

    return final_video


def export_clips(video_path, segments, output_dir, title, is_short=False):
    """
    Exporta os segmentos de vídeo detectados.
    Se `is_short` for True, ajusta para a proporção 1080x1920 com fundo desfocado.
    """
    # Criar pasta com o título do vídeo
    title_dir = os.path.join(output_dir, title)
    if not os.path.exists(title_dir):
        os.makedirs(title_dir)

    for i, (start, end) in enumerate(segments):
        output_path = os.path.join(title_dir, f"{generate_unique_filename()}.mp4")
        clip = VideoFileClip(video_path).subclip(start, end)

        # Ajustar para proporção vertical se for short
        if is_short:
            clip = create_vertical_video(clip)

        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Clip exportado: {output_path}")
