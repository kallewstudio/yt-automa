import os
from utils.processor import extract_audio, detect_segments
from utils.cutter import export_clips


def main():
    print("Bem-vindo ao Video Cutter!")
    video_path = input("Insira o caminho do vídeo: ")
    cut_type = input("Escolha o tipo de corte (Short ou Clipe): ").strip().lower()

    if not os.path.exists(video_path):
        print("Arquivo de vídeo não encontrado.")
        return

    # Diretório de saída
    output_dir = "./output"
    prefix = "short" if cut_type == "short" else "clip"

    # Extraindo áudio
    print("Extraindo o áudio...")
    audio_path = "temp_audio.wav"
    extract_audio(video_path, audio_path)

    # Detectando segmentos
    print("Detectando segmentos de áudio...")
    max_duration = 59 if cut_type == "short" else 300  # Shorts: 59s, Clips: até 5min
    segments = detect_segments(
        audio_path,
        silence_thresh=-40,
        min_silence_len=700,
        min_duration=4
    )

    # Filtrar segmentos pela duração
    filtered_segments = [
        (start, end) for start, end in segments if (end - start) <= max_duration
    ]

    if not filtered_segments:
        print(f"Nenhum segmento encontrado para {cut_type}s.")
        return

    # Exportar clipes
    print(f"Exportando {len(filtered_segments)} {cut_type}(s)...")
    export_clips(video_path, filtered_segments, output_dir, prefix)
    print("Processo concluído!")


if __name__ == "__main__":
    main()
