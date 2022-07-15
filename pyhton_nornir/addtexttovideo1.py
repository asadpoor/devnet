# https://towardsdatascience.com/rendering-text-on-video-using-python-1c006519c0aa

import moviepy.editor as mp
import os

directory = '/home/majid/Downloads/original/'

############ to be changed###########
textinput="Majid:Asadpoor:1111111111:info@rayka-co.ir:0911111111"
newdir = "Majid_Asadpoor"
############ to be changed###########


parent_dir = "/home/majid/Downloads/"
path = os.path.join(parent_dir, newdir)
isExist = os.path.exists(path)
if not isExist:
    os.mkdir(path)

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
#    print(f)
    my_video = mp.VideoFileClip(f, audio=True)
    duration=my_video.duration
#    print("duration=", duration)
    w,h = moviesize = my_video.size
    my_text = mp.TextClip(textinput, font='Amiri-regular', color='white', fontsize=34)
    txt_col = my_text.on_color(size=(my_video.w + my_text.w, my_text.h+5), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
    txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),max(5*h/6,int(100*t))) )
    final = mp.CompositeVideoClip([my_video,txt_mov])
    output=path+"/"+filename
    final.subclip(0,duration).write_videofile(output, fps=10,codec='libx264')
#    final.subclip(0,15).write_videofile('/home/majid/Downloads/testfps10.mp4', fps=10,codec='libx264')
