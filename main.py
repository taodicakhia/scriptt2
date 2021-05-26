from mediafire_dl import mediafire_dl
import zipfile
import rarfile
import shutil
import os
import subprocess
import random


def main(link):
    filename = link.split('/')[-2]
    fol_tmp = str(random.randint(1000000, 100000000))
    mediafire_dl.download(link, filename, quiet=False)
    path_copy = os.path.abspath(filename[:-4] + '/Firmware')
    if '.zip' in filename:
        file = zipfile.ZipFile(filename)
        file.extractall()
    else:
        file = rarfile.RarFile(filename)
        file.extractall()
    shutil.move(path_copy, fol_tmp)
    shutil.rmtree(filename[:-4])
    os.rename(fol_tmp, filename[:-4])
    files = os.listdir(filename[:-4] + '/')
    if 'naijarom.com.url' in files:
        os.remove(filename[:-4] + '/naijarom.com.url')
    elif 'firmwarefile.com.url' in files:
        os.remove(filename[:-4] + '/firmwarefile.com.url')
    subprocess.run(['7z', 'a', '-t7z', filename[:-4] +
                    '.7z', filename[:-4] + '/', '-m0=lzma2', '-mx=9', '-md=128m', '-mfb=128', '-aoa'])


if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('link.txt')]
    for link in lines:
        main(link)
