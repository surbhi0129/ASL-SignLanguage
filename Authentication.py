from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    version = '2018-03-19',
    iam_apikey="NoQwzU5M7xLLvfSCs02WhCGmXFzPicNEz3gmEOd22I9P"
)

import json
from watson_developer_cloud import VisualRecognitionV3


with open('E:/Hack/HackASL/Test.JPG', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.5',
	classifier_ids='DefaultCustomModel_437973371').get_result()
print(json.dumps(classes, indent=2))
