from moviepy.editor import *
import time

# python video_edit.py

startTime = time.time()

clip = VideoFileClip("first_video.avi")  # Dönüştürülecek video
newclip = clip.resize((1138, 640))  # olması istenilen boyut
newclip.write_videofile("converted_video.mp4", fps=10)  # dönüştürülmüş video adı ve olması istenilen fps değeri

clip.reader.close()

endTime = time.time()

print(f'Toplam işlem süresi: {endTime - startTime}')
