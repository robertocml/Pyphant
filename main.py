import pytube as pt



video_url = 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
video =  pt.YouTube(video_url)
video = video.streams.first()
video.download('C:\Users\\rober\Desktop\Github Repos\Pyphant')