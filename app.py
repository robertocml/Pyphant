import pytube as pt
from flask import Flask, escape, request, render_template,url_for


# I made the fix of bennyb518.. on next link to make mixins.py inside the pytube library works..
# https://github.com/nficano/pytube/issues/467#issuecomment-567560796

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def video_url_post():
    video_url = request.form['video_url']
    try:
        youtube = pt.YouTube(video_url)
        video = youtube.streams.first()
        video.download() 
        return render_template('sucess.html')
    except:
        return render_template('failed.html')


if __name__ == "__main__":
    app.run(debug=True)