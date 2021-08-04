# Sample code for model training.
from pyAudioAnalysis import audioTrainTest as aT

class1_dir_name = './audio/pyaudio_train/male'
class2_dir_name = './audio/pyaudio_train/female'

# aT.extract_features_and_train([class1_dir_name, class2_dir_name], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'svm', 'svmMaleFemale', False)

# aT.extract_features_and_train([class1_dir_name, class2_dir_name], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'knn', 'knnMaleFemale', False)

# aT.extract_features_and_train([class1_dir_name, class2_dir_name], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'extratrees', 'extraTreesMaleFemale', False)

aT.extract_features_and_train([class1_dir_name, class2_dir_name], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'gradientboosting', 'gradientBoostMaleFemale', False)

# aT.extract_features_and_train([class1_dir_name, class2_dir_name], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'randomforest', 'rfMaleFemale', False)
