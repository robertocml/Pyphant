import pytube as pt

# I made the fix of bennyb518.. on next link to make mixins.py inside the pytube library works..
# https://github.com/nficano/pytube/issues/467#issuecomment-567560796


# Basic example to start with
video_url = 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
youtube =  pt.YouTube(video_url)
video = youtube.streams.first()
video.download()