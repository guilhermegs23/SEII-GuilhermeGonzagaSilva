#Guilherme Gonzaga Silva 11621EMT021 
#prog14.py

import os

os.chdir("C:\\Users\guilh\Documents\GitHub\SEIII-GuilhermeGonzagaSilva\Semana02\prog14")

for f in os.listdir():
    f_name, file_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
     
    #print('{}-{}-{}{}'.format(f_num, f_course, f_title, file_ext))
    new_name = '{}-{}{}'.format(f_num, f_title, file_ext)

    os.rename(f, new_name)