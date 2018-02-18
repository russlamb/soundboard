import playsound
from pydub import AudioSegment
from pydub.playback import play

def play_sound():
    """play a sound file.  Uses playsound module, but if there's an OS error use pydub.
    (OSx has issues with playsound)"""
    try:

        file_name = r"sound.mp3"
        playsound.playsound(file_name)
    except OSError:
        AudioSegment.converter=r"/Users/russelllamb/Downloads/ffmpeg"
        sound=AudioSegment.from_mp3(r"sound.mp3")
        play(sound)
