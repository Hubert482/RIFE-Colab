import os
import subprocess
import sys
import addInstalldirToPath
from addInstalldirToPath import *

REQUIRED_PACKAGES = ['numpy>=1.16', 'tqdm>=4.35.0', 'opencv-python>=4.1.2', 'pyqt5', 'requests']


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def downloadFile(url,outFile):
    import requests
    r = requests.get(url, allow_redirects=True)
    open(outFile, 'wb').write(r.content)

def extractArchive(archiveFile,exclusions:list = []):
    sevenZip = "7z"
    if os.name == 'nt':
        sevenZip = r"C:\Program Files\7-Zip\7z.exe"

    sevenZipExclusions = []
    for exclusion in exclusions:
        sevenZipExclusions.append('-xr!' + exclusion)

    success = False
    while not success:
        try:
            subprocess.run([sevenZip,'e',archiveFile,'-aoa'] + sevenZipExclusions)
            success = True
        except:
            print('Cannot execute 7-zip to extract archive. Do you have x64 7-zip installed?')
            print('If not, please do so now before hitting enter: https://www.7-zip.org/a/7z1900-x64.exe')
            input('...')

def mainInstall():
    pathCWD = os.path.realpath(__file__)
    pathCWD = pathCWD[:pathCWD.rindex(os.path.sep)]
    pathCWD += os.path.sep + 'arXiv2020RIFE' + os.path.sep + 'model' + os.path.sep
    print(pathCWD)

    rifeCodeFiles = os.listdir(pathCWD)

    for file in rifeCodeFiles:
        if not os.path.isfile(pathCWD + file):
            continue
        print(pathCWD + file)
        fileObj = open(pathCWD + file,'r')

        fileStr = fileObj.read()
        fileObj.close()
        fileStr = fileStr.replace('from model.','from arXiv2020RIFE.model.')

        outFileObj = open(pathCWD + file,'w')
        outFileObj.write(fileStr)
        outFileObj.close()

    #return

    for package in REQUIRED_PACKAGES:
        install(package)

    # Get torch
    try:
        import torch

        versionString = torch.__version__
        subversions = versionString.split('.')

        if int(subversions[0]) < 1:
            # Torch less than 1.0.0
            raise Exception
        if '+cpu' in subversions[2]:
            # Torch CPU only version
            raise Exception
        print('Found torch', torch.__version__)
    except:
        # Install torch
        print("Pytorch not found, getting 1.7.1 CUDA 11")
        if os.name == 'nt':
            # On windows
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', 'torch===1.7.1+cu110', 'torchvision===0.8.2+cu110',
                 'torchaudio===0.7.2', '-f', 'https://download.pytorch.org/whl/torch_stable.html'])
        else:
            # On linux
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', 'torch==1.7.1+cu110', 'torchvision==0.8.2+cu110',
                 'torchaudio===0.7.2', '-f', 'https://download.pytorch.org/whl/torch_stable.html'])


    # Check ffmpeg
    ffmpegExists = False
    ffprobeExists = False
    while not ffmpegExists or not ffprobeExists:
        try:
            subprocess.run(['ffmpeg'])
            ffmpegExists = True
            subprocess.run(['ffprobe'])
            ffprobeExists = True
        except:
            print("Can't find ffmpeg/ffprobe - Downloading")
            downloadFile(r'https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z','ffmpeg.7z')
            extractArchive('ffmpeg.7z',['doc'])

    print('----DEPENDENCY INSTALLATION COMPLETE----')

mainInstall()
