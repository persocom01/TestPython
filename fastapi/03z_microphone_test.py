# This file uses the microphone to generate a wav file.
import speech_recognition as sr
import pyaudio

file = './files/test_wav.wav'
device_index = -1

def get_microphone_device_index():
    device_index = -1
    pa = pyaudio.PyAudio()
    try:
        pa.get_host_api_info_by_index(0)['defaultInputDevice']
    except KeyError:


try:
    mic = sr.Microphone(device_index=device_index)

    r = sr.Recognizer()

    with mic as source:
        print('recording')
        audio = r.listen(source)
        with open(file, 'wb') as f:
            f.write(audio.get_wav_data())

    # Built in speech recognition not recommended for deployment use.
    # print(r.recognize_google(audio))

except OSError:
    print('check device list if the device index of your microphone is correct:')
    print(sr.Microphone.list_microphone_names())
