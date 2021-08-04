# pyAudio gender recognition models

This folder contains pretrained models that can be used to classify audio voice samples as originating from an English speaking human male or female.

Each zipfile contains all the files needed for each type of model, and must be unzipped before use.

## Model training

The models were trained on a subset of the IMDA National Speech Corpus, found here: https://www.imda.gov.sg/programme-listing/digital-services-lab/national-speech-corpus

Each speaker in the dataset was manually classified into male or female before the models were trained on their voice samples.

In total, the dataset comprised approximately 10,000 audio samples.

## Available models

There are in total 5 models available, but not all models were created equal. `gradientboosting` and `svm` based models were found to be the most accurate and are recommended for use.

| Model name | Model type |
| ------ | ------ |
| extraTreesMaleFemale | extratrees |
| gradientBoostMaleFemale | gradientboosting |
| knnMaleFemale | knn |
| rfMaleFemale | randomforest |
| svmMaleFemale | svm |

These model names and model types are part of the parameters needed to use the models.

## Tests

To test for accuracy, the models were tested on English voice samples from a Singaporean male, an American male, a Singaporean female, and an American female, that were not included in the training data.

The Singaporean voice samples were either self recorded by the author or from parts of the IMDA National Speech Corpus not used to train the model. The American voice samples come from the CMU_ARCTIC database found here: http://festvox.org/cmu_arctic/

The results, rounded down to the nearest percent were as follows:

| Model name | Speaker | Prediction | Prediction certainty |
| ------ | ------ | ------ | ------ |
| extraTreesMaleFemale | Singaporean male | male | 80% |
| extraTreesMaleFemale | American male | male | 60% |
| extraTreesMaleFemale | Singaporean female | female | 97% |
| extraTreesMaleFemale | American female | female | 95% |
| gradientBoostMaleFemale | Singaporean male | male | 99% |
| gradientBoostMaleFemale | American male | male | 99% |
| gradientBoostMaleFemale | Singaporean female | female | 99% |
| gradientBoostMaleFemale | American female | female | 99% |
| knnMaleFemale | Singaporean male | male | 100% |
| knnMaleFemale | American male | male | 53% |
| knnMaleFemale | Singaporean female | female | 92% |
| knnMaleFemale | American female | female | 100% |
| rfMaleFemale | Singaporean male | male | 79% |
| rfMaleFemale | American male | male | 65% |
| rfMaleFemale | Singaporean female | female | 98% |
| rfMaleFemale | American female | female | 90% |
| svmMaleFemale | Singaporean male | male | 99% |
| svmMaleFemale | American male | male | 99% |
| svmMaleFemale | Singaporean female | female | 99% |
| svmMaleFemale | American female | female | 99% |

While the tests suggest that `gradientBoostMaleFemale` and `svmMaleFemale` are most accurate models, the tests were limited in nature, and I would advise that one test on their own audio dataset before use.

## Usage

To use a model, unzip it into the project folder and run a python file with basic code as follows:

```
from pyAudioAnalysis import audioTrainTest as aT

aT.file_classification('file_to_be_tested', 'model_name', 'model_type')
```

The `file_classification()` function will return a tuple with values as follows:

```
(prediction, prediction_array, training_folder_list)
```

Of interest to us are the `prediction` and `prediction_array`.

`prediction` is a float representing the input audio's predicted class, where in this case:
* 0.0 = male
* 1.0 = female

`prediction_array` is an array of the prediction probabilities of each class. In this case, the array is only 2 elements long, for example:

```
array([0.6, 0.4])
```

Where `0.6` is the probability that the predicted class is class `0.0`, while `0.4` is the probability that the predicted class is class `1.0`.
