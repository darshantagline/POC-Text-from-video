# POC-Text-from-video
extract text from receipt contains in video


### Installation:

```
Clone the repository from github
```
```
cd to repository
```
create virtual environment
```
pyhton3 -m venv env
```

now activate virtual environment
```
. env/bin/activated
```

install all dependency for project:
```
pip install -r requirements.txt
```


To run:
```
export FLASK_APP = main.py
flask run
Go to postman and request with post "http://127.0.0.1:5000" in search bar
pass video in form data as videoFile
```

Demo: