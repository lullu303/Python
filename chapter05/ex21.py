file_names = [
    'song1.mp3',
    'image1.JPG',
    'image2.JPG',
    'song2.MP3',
    'video1.mp4',
    'song3.MP3',
]

# 전달된 파일명 리스트에서 mp3 파일만 담긴
# 튜플을 반환하는 함수(find_song)을 만드세요

def find_song(names) :
    songs =[]
    for name in names:
        test_name = name.lower()
        if test_name.endswith('.mp3'):  #startswidth()
            songs.append(name)
    return tuple(songs)

songs = find_song(file_names)
for song in songs:
    print(song)