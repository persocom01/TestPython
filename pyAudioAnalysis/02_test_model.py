# Sample code for model testing.
from pyAudioAnalysis import audioTrainTest as aT


def test_function(model_name, model_type):
    test_samples = [
        'audio/test/male/arctic_a0014.wav',
        'audio/test/male/U5.wav',
        'audio/test/female/007030085.wav',
        'audio/test/female/arctic_a0006.wav'
    ]
    for sample in test_samples:
        print(aT.file_classification(sample, model_name, model_type))


model_name = 'svmMaleFemale'
model_type = 'svm'
print('svm test')
test_function(model_name, model_type)

model_name = 'knnMaleFemale'
model_type = 'knn'
print('knn test')
test_function(model_name, model_type)

model_name = 'extraTreesMaleFemale'
model_type = 'extratrees'
print('extra trees test')
test_function(model_name, model_type)

model_name = 'gradientBoostMaleFemale'
model_type = 'gradientboosting'
print('gradient boost test')
test_function(model_name, model_type)

model_name = 'rfMaleFemale'
model_type = 'randomforest'
print('random forest test')
test_function(model_name, model_type)
