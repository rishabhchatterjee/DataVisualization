import pyaudio
import wave
import time
import random

w0 = wave.open('saxSounds/0.wav', 'rb')
w1 = wave.open('saxSounds/1.wav', 'rb')
w2 = wave.open('saxSounds/2.wav', 'rb')
w3 = wave.open('saxSounds/3.wav', 'rb')
w4 = wave.open('saxSounds/4.wav', 'rb')
w5 = wave.open('saxSounds/5.wav', 'rb')
w6 = wave.open('saxSounds/6.wav', 'rb')
w7 = wave.open('saxSounds/7.wav', 'rb')
w8 = wave.open('saxSounds/8.wav', 'rb')
w9 = wave.open('saxSounds/9.wav', 'rb')

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
