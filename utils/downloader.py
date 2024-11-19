import yt_dlp
import os
from utils.utils import sanitize_filename

def download_video(link, output_dir="./output"):
    """
    Baixa o vídeo do YouTube, salva no diretório e retorna o título e o caminho do arquivo.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            raw_title = info.get("title", "video")
            title = sanitize_filename(raw_title)  # Sanitizar o título
            downloaded_file = ydl.prepare_filename(info)
            return title, downloaded_file
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
        return None, None
