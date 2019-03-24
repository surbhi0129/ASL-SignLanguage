import os
import tempfile
import base64
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
   # imgdata = request.form['imgData']
    #header, encoded = imgdata.split(",", 1)
    # data = base64.b64decode(encoded)

    #with open('zzzz.jpg', 'wb') as f:
     #   f.write(base64.b64decode(encoded + "========"))

    # print(imgdata);
   from watson_developer_cloud import VisualRecognitionV3

   visual_recognition = VisualRecognitionV3(
       version='2018-03-19',
       iam_apikey="NoQwzU5M7xLLvfSCs02WhCGmXFzPicNEz3gmEOd22I9P"
   )

   import json


   with open('E:/Hack/HackASL/Test.JPG', 'rb') as images_file:
       classes = visual_recognition.classify(
           images_file,
           threshold='0.5',
           classifier_ids='DefaultCustomModel_437973371').get_result()
   #print(json.dumps(classes, indent=2))
   return jsonify(classes)

   #return render_template('index.html')

if __name__ == "__main__":
    app.run()
