import glob
import os
import time
import datetime
import locale


def last_modified_file(folder):
    files = list(filter(os.path.isfile, glob.glob(folder + "/*")))
    if len(files) > 0:
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return files[0]
    else:
        return None


locale.setlocale(locale.LC_ALL, "ru")
timestamp = int(time.time())
value = datetime.datetime.fromtimestamp(timestamp)
nazvanie1 = (value.strftime(f'Таунхаус 48 - %B %Y'))
nazvanie2 = (value.strftime(f'Таунхаусы 23,24,48 - %B %Y'))
nazvanie3 = (value.strftime(f'Таунхаус 49 - %B %Y'))
nazvanie4 = (value.strftime(f'Таунхаус 27 - %B %Y'))

file_name1 = last_modified_file("/mnt/nextcloud/geleon/files/video/monthly/camera1")
if file_name1:
    os.system(
        f'/root/youtubeuploader_linux_amd64 -filename {file_name1} -language "ru" -description "Камера1 за месяц" -title "{nazvanie1}" -privacy "public" -metaJSON "/root/playlists5.json"')
file_name2 = last_modified_file("/mnt/nextcloud/geleon/files/video/monthly/camera2")
if file_name2:
    os.system(
        f'/root/youtubeuploader_linux_amd64 -filename {file_name2} -language "ru" -description "Камера2 за месяц" -title "{nazvanie1}" -privacy "public" -metaJSON "/root/playlists6.json"')
file_name3 = last_modified_file("/mnt/nextcloud/geleon/files/video/monthly/camera3")
if file_name3:
    os.system(
        f'/root/youtubeuploader_linux_amd64 -filename {file_name3} -language "ru" -description "Камера3 за месяц" -title "{nazvanie1}" -privacy "public" -metaJSON "/root/playlists7.json"')
file_name4 = last_modified_file("/mnt/nextcloud/geleon/files/video/monthly/camera4")
if file_name4:
    os.system(
        f'/root/youtubeuploader_linux_amd64 -filename {file_name4} -language "ru" -description "Камера4 за месяц" -title "{nazvanie1}" -privacy "public" -metaJSON "/root/playlists8.json"')
