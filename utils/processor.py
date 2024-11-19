from pydub import AudioSegment, silence
import moviepy.editor as mp

def extract_audio(video_path, output_audio_path="temp_audio.wav"):
    """
    Extrai o áudio de um vídeo.
    """
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)
    return output_audio_path

def detect_segments(audio_path, silence_thresh=-40, min_silence_len=700, min_duration=4):
    """
    Detecta segmentos de áudio com base em silêncio.
    """
    audio = AudioSegment.from_file(audio_path)
    non_silent_ranges = silence.detect_nonsilent(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh
    )
    segments = [
        (start / 1000, end / 1000)  # Convertendo para segundos
        for start, end in non_silent_ranges
        if (end - start) / 1000 >= min_duration
    ]
    return segments
