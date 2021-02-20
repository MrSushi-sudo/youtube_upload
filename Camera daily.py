import glob
import os
import time
import datetime


def last_modified_file(folder):
    files = list(filter(os.path.isfile, glob.glob(folder + "/*")))
    if len(files) > 0:
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return files[0]
    else:
        return None


def den_stroiki():
    first_date = '2020-05-18'
    first_date = first_date.split('-')
    first_date_first_date = datetime.date(int(first_date[0]), int(first_date[1]), int(first_date[2]))
    second_date = datetime.date.today()
    raznica = second_date - first_date_first_date
    result = str(raznica)
    return result.split()[0]


timestamp = int(time.time())
value = datetime.datetime.fromtimestamp(timestamp)
nazvanie1 = (value.strftime(f'Таунхаус 48 - День {den_stroiki()} - %d.%m.%Y'))
nazvanie2 = (value.strftime(f'Таунхаусы 23,24,48 - День {den_stroiki()} - %d.%m.%Y'))
nazvanie3 = (value.strftime(f'Таунхаус 49 - День {den_stroiki()} - %d.%m.%Y'))
nazvanie4 = (value.strftime(f'Таунхаус 27 - День {den_stroiki()} - %d.%m.%Y'))


file_name1 = last_modified_file("/mnt/nextcloud/geleon/files/video/daily/camera1")
if file_name1:
    os.system(f'/root/youtubeuploader_linux_amd64 -filename {file_name1} -language "ru" -description "Камера1 за день" -title "{nazvanie1}" -privacy "public" -metaJSON "/root/playlists1.json"')
file_name2 = last_modified_file("/mnt/nextcloud/geleon/files/video/daily/camera2")
if file_name2:
    os.system(f'/root/youtubeuploader_linux_amd64 -filename {file_name2} -language "ru" -description "Камера2 за день" -title "{nazvanie2}" -privacy "public" -metaJSON "/root/playlists2.json"')
file_name3 = last_modified_file("/mnt/nextcloud/geleon/files/video/daily/camera3")
if file_name3:
    os.system(f'/root/youtubeuploader_linux_amd64 -filename {file_name3} -language "ru" -description "Камера3 за день" -title "{nazvanie3}" -privacy "public" -metaJSON "/root/playlists3.json"')
file_name4 = last_modified_file("/mnt/nextcloud/geleon/files/video/daily/camera4")
if file_name4:
    os.system(f'/root/youtubeuploader_linux_amd64 -filename {file_name4} -language "ru" -description "Камера4 за день" -title "{nazvanie4}" -privacy "public" -metaJSON "/root/playlists4.json"')