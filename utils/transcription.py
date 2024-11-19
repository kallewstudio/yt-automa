import whisper


def transcribe_video(video_path, log_callback=None):
    """
    Transcreve o vídeo e gera logs de progresso.
    """
    if log_callback:
        log_callback(f"Iniciando transcrição para {video_path}...")

    model = whisper.load_model("base")
    result = model.transcribe(video_path)

    segments = result.get("segments", [])
    if log_callback:
        log_callback(f"Transcrição concluída! {len(segments)} segmentos identificados.")
        for i, segment in enumerate(segments):
            log_callback(
                f"Segmento {i + 1}: Início={segment['start']:.2f}s, Fim={segment['end']:.2f}s, Texto={segment['text']}")

    return result['text'], segments


def identify_segments(segments, max_short_duration=59):
    """
    Separa os segmentos em shorts e clipes.
    """
    shorts = []
    clips = []
    for segment in segments:
        start, end = segment['start'], segment['end']
        duration = end - start
        if duration <= max_short_duration:  # Shorts: até 59 segundos
            shorts.append(segment)
        elif duration > 61:  # Clipes: mais de 1 minuto
            clips.append(segment)
    return shorts, clips
