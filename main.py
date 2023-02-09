import cv2
import pytesseract
from flask import Flask,request
from math import floor
from io import BytesIO
from tempfile import NamedTemporaryFile
from collections import OrderedDict

app = Flask(__name__)

#Extract text from frame(images)
def extract_text(frame):
    text = pytesseract.image_to_string(frame)
    return text

@app.route("/extract_text",methods=["POST",])
def extract_text_from_video():
    file = request.files["videoFile"]
    file_bytes = BytesIO(file.read())
    with NamedTemporaryFile(delete=True) as temp_file:
        temp_file.write(file_bytes.getvalue())
        temp_file.seek(0)
        cap = cv2.VideoCapture(temp_file.name)
    #Framerate of video
    fps = cap.get(cv2.CAP_PROP_FPS)

    frames = []
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if i % floor(fps) == 0:  
            frames.append(frame)
        i += 1

    texts = []
    #Append extracted text from every frames(images) in texts
    for frame in frames:
        texts.append(extract_text(frame))

    result = "".join(texts)
    #Remove duplicate data
    result = "\n".join(list(OrderedDict.fromkeys(result.split("\n"))))
    return result


if __name__ == "__main__":
    app.run(debug=True)
