from directorynav import getfiles_folder
from pathlib import Path
from pydub import AudioSegment

def make_mono(segment: AudioSegment): #* split_to_mono works regardless, we can just do this inline
    if segment.channels>1:
        return segment.split_to_mono[0]

def audiosegments_from_pathset(pathset: set, segformat="as_is") -> set:
    segset = set()
    for file in pathset:
        match file.suffix:
            case ".wav":
                seg = AudioSegment.from_wav(file)
            case ".mp3":
                seg = AudioSegment.from_mp3(file)
            case _:
                seg = AudioSegment.from_file(file) #uncertain how the ffmpeg ver works
        if segformat == "mono":
            seg = seg.split_to_mono()[0]
        segset.add(seg)
    return segset

#* Wanted to add tkinter filedialog to pick these but tkinter broken rn
#** -EXECUTED LINES---
sourcedir = Path(r'D:\coding\Dpython\ex-audio')
destiation = Path(r'D:\coding\Dpython\ex-audio-converted')

fileSet = getfiles_folder(sourcedir,{'.wav','.mp3'})
audioSet = audiosegments_from_pathset(fileSet, segformat = "mono")
#-testing-
print(fileSet)
print(audioSet)



