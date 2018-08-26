import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_api_key="Y1vjfKM6SKbS0rUuuZtWCgxtliV7MOaySdk51_LQWZv2")
filename = 'download.jpeg'
with open(filename, 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        classifier_ids='Wedding_1786151371')

print(json.dumps(classes, indent=2))
