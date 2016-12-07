import pyaudio
import wave
import time
import random

# adapted from 
# http://code.activestate.com/recipes/579116-use-pyaudio-to-play-a-list-of-wav-files/
# to play a single .wav file whenever '0' hit

def play(wave_filename):                               
    wf = wave.open(wave_filename, 'rb')
    p = pyaudio.PyAudio()
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)
    stream.start_stream()

    while stream.is_active():
        time.sleep(0.0)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()

