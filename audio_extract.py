import pydub


class AudioExtracter():
    """Load a file and extract audio clips from it.
    Parameters are the path to the ffmpeg converter and the file to parse."""

    def __init__(self, file_path, path_to_converter=None):
        self.file_path = file_path
        if path_to_converter is not None:
            self.converter = path_to_converter
            pydub.AudioSegment.converter = path_to_converter

    def trim_audio(self, delta_start, delta_end):
        song = pydub.AudioSegment.from_mp3(self.file_path)

        start_ms = delta_start.total_seconds() * 1000.0
        end_ms = delta_end.total_seconds() * 1000.0
        clip = song[start_ms:end_ms]
        return clip

    def save_clip(self, save_path, start, end):
        my_clip = self.trim_audio(start, end)
        my_clip.export(save_path, format="mp3")
