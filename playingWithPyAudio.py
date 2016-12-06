import pyaudio
import wave
import time
import random

from multiprocessing import Process 

def play(wave_filename):
    """
        Plays a WAV file
    """
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


#play('zeroSounds/0.wav')

