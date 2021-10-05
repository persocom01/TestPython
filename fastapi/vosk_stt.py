from vosk import Model, KaldiRecognizer, SetLogLevel
import os
import wave
import json


def text_from_sound_file(file, modelpath):
    SetLogLevel(0)

    if not os.path.exists(modelpath):
        print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit(1)

    wf = wave.open(file, 'rb')
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != 'NONE':
        print('Audio file must be WAV format mono PCM.')
        exit(1)

    model = Model(modelpath)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)
        # if rec.AcceptWaveform(data):
        #     print(rec.Result())
        # else:
        #     print(rec.PartialResult())

    return json.loads(rec.FinalResult())['text']
