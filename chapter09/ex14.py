import os
from os import path

base = 'images'

def get_category_images(base):
    images = {}

    for dir in os.listdir(base):
        dir_path = path.join(base,dir)
        images[dir] =os.listdir(dir_path)

    return images

category_images = get_category_images(base)

#파일명 변경
for dir, fnames in category_images.items():
    for ix, fname in enumerate(fnames, 1):
        src_path = path.join(base, dir, fname)
        dst_path = path.join(base, dir, f'{ix:04}.jpg')
        print(f'{src_path} => {dst_path}')
        os.rename(src_path, dst_path)
        
#파일의 확장자 분리
#path.splitext("images/dog/aaa.png") => ('images/dog/aaa', '.png)