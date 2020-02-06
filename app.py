import pytube as pt
from flask import Flask, escape, request, render_template,url_for, send_from_directory


# I made the fix of bennyb518.. on next link to make mixins.py inside the pytube library works..
# https://github.com/nficano/pytube/issues/467#issuecomment-567560796
# https://www.youtube.com/watch?v=jNQXAC9IVRw
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
        video.download('C:\\Users\\rober\\Desktop\\Github Repos\\Pyphant\\uploads') 
        filename = video.title + ".mp4"
        print(filename)
        return send_from_directory(directory='uploads', filename=filename, as_attachment=True)
    except:
        print('failed')
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)