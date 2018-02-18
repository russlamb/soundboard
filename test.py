import os
from datetime import timedelta

from audio_extract import AudioExtracter


def test_save_clip():
    my_start = timedelta(minutes=15, seconds=44.5)
    my_end = timedelta(minutes=15, seconds=44.95)
    my_file = r"ep14.mp3"
    new_file = my_file + "-clip.mp3"

    path_to_converter = r"C:\ffmpeg-20180215-fb58073-win64-static\bin\ffmpeg.exe"
    ae = AudioExtracter(my_file, path_to_converter)
    ae.save_clip(new_file, my_start, my_end)
    os.startfile(new_file)