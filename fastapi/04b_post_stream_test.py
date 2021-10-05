import queue
import sys
import sounddevice as sd
import os
import vosk

params = {
    'filename': None,
    'model': './fastapi/vosk-model-small-en-us-0.15',
    'device': 1,
    'samplerate': None
}


class AttribDict(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])


args = AttribDict(params)

# Seach for microphone device id.
# print(sd.query_devices())

q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


try:
    if args.model is None:
        args.model = 'model'
    if not os.path.exists(args.model):
        print('Please download a model for your language from https://alphacephei.com/vosk/models')
        print("and unpack as 'model' in the current folder.")
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])

    model = vosk.Model(args.model)

    if args.filename:
        dump_fn = open(args.filename, 'wb')
    else:
        dump_fn = None

    with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device, dtype='int16', channels=1, callback=callback):
        print('#' * 80)
        print('Press Ctrl+C to stop the recording')
        print('#' * 80)

        rec = vosk.KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                print(rec.Result())
            else:
                print(rec.PartialResult())
            if dump_fn is not None:
                dump_fn.write(data)

except KeyboardInterrupt:
    print('\nDone')
except Exception as e:
    print(type(e).__name__ + ': ' + str(e))
