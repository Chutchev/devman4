from itertools import groupby
from tinytag import TinyTag
from tinytag import TinyTagException
import os


def get_song_info_from_mp3_tags(filename):
    try:
        tag = TinyTag.get(filename)
    except TinyTagException:
        tag = "Нет тегов"
    return tag


def make_list_path_tags(filename):
    music_list = []
    tree = os.walk(os.path.dirname(os.path.dirname(filename)))
    for dir, subdir, files in tree:
        for file in files:
            path = os.path.join(dir, file)
            song = [path, get_song_info_from_mp3_tags(path)]
            music_list.append(song)
    return music_list


def sorted_artist_name(music_list, artist):
    sorted_music_list = []
    albums = []
    for path, tag in music_list:
        if tag.artist == artist:
            item = [path, tag]
            if tag.album not in albums:
                albums.append(tag.album)
            sorted_music_list.append(item)
    return sorted_music_list


filename = "E:\GIT\music\music\Eminem - Revival\\04. Untouchable.mp3"
music_list = make_list_path_tags(filename)
sorted_music_list = sorted_artist_name(music_list, 'Eminem')

sorted_music_list = sorted(sorted_music_list, key=lambda sorted_music: sorted_music_list[20][1].album)

for key, group in groupby(sorted_music_list, key=lambda sorted_music: sorted_music_list[20][1].album):
    print(key)
    for item in list(group):
        print(item)