# https://towardsdatascience.com/rendering-text-on-video-using-python-1c006519c0aa

import moviepy.editor as mp
my_video = mp.VideoFileClip('/home/majid/Downloads/test.mp4', audio=True)
w,h = moviesize = my_video.size

my_text = mp.TextClip('The Art of Adding Text on Video', font='Amiri-regular', color='white', fontsize=34)
#my_text = mp.TextClip('The Art of Adding Text on Video', fontsize=34)

#txt_col = my_text.on_color(size=(my_video.w + my_text.w, my_text.h+5), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)

#txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),max(5*h/6,int(100*t))) )
txt_mov = my_text.set_pos('center').set_duration(10) 

final = mp.CompositeVideoClip([my_video,txt_mov])

#final.subclip(0,1180).write_videofile('/home/majid/Downloads/test1.mp4',fps=24,codec='libx264')
final.subclip(0,1180).write_videofile('/home/majid/Downloads/test1.mp4')