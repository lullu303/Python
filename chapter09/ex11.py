import os
from os import path

base = 'images'

def get_category_images(base):
    images = {}

    for dir in os.listdir(base):
        #dir에 대한 경로가 필요
        dir_path = path.join(base,dir)
        #print(dir, dir_path)
        #dir이 키가 됨
        images[dir] =os.listdir(dir_path)

    return images

import pickle       #다른 언어와 호환성은 없음.(binary의 특징)

def save(fpath, data):
    try:
        with open(fpath, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다.")
        print(e)

def load(fpath):
    try:
        with open(fpath, 'rb') as file:
            data = pickle.load(file)
            return data
    except:
        print(f"{fpath} 파일 읽기에 실패했습니다.")

category_images = get_category_images(base)

save('category.dat', category_images)   # .dat =>데이터의 약자.

data = load('category.dat')
print(type(data))
print(data)

# for dir, fnames in category_images.items():
#     for fname in fnames:
#         print(dir, fname)
#         file_path = path.join(base, dir, fname)
#         print(file_path)

# print(category_images) 
    