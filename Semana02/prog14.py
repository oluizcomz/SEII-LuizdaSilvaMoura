#application create files and organize
import os
import shutil
files = ['The Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
const = ' - Our Solar System - #'
def Create_files():
    os.mkdir('pasta')
    os.chdir('./pasta')
    for index, name in enumerate (files, start=1):
        namec = name + const + str(index)+'.mp4' 
        f = open(namec,'wb')
        f.close()
    pass

def Delet_files():
    os.chdir('..')
    print(os.getcwd())
    shutil.rmtree('pasta')
    pass
def Organize():
    for fi in os.listdir():
        f_name, f_ext = os.path.splitext(fi)
        f_title, f_course , f_num = f_name.split('-')
        f_title = f_title.strip()  
        f_course = f_course.strip()
        f_num = f_num.strip()[1:].zfill(2)
        new_name = ('{}-{}-{}{}'.format(f_num, f_course,f_title , f_ext))
        os.rename(fi,new_name)
        pass


Create_files()

print('\n Created files:')
for fi in os.listdir():
    print(fi)
print('\n Organize files:')
Organize()
for fi in os.listdir():
    print(fi)

Delet_files()