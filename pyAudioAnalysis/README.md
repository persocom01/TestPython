# pyAudioAnalysis

pyAudioAnalysis is a Python library for audio feature extraction, classification, segmentation and applications. The github repo is found here: https://github.com/tyiannak/pyAudioAnalysis

## Pre-requisites

* [python](https://www.python.org/downloads/)
* [FFmpeg encoder](https://ffmpeg.org/)
* [7-zip](https://www.7-zip.org/)

1. After downloading a suitable `FFmpeg` build, extract the folder with `7-zip`.

2. Copy and paste the folder to a suitable location, such as `C:\Program Files\ffmpeg`

3. Add the location, such as `C:\Program Files\ffmpeg\bin` to windows environmental variables.

## Installation

1. Clone the pyAudioAnalysis github repo

```
git clone https://github.com/tyiannak/pyAudioAnalysis.git
```

2. Inside the project folder, install requirements

```
pip install -r ./requirements.txt
```

3. pip install the module

```
pip install -e .
```
