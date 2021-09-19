############################
# Created by Timeo Bossuet #
############################

from moviepy.editor import *
from random import*

# Video path
clip = VideoFileClip("D:\echocloud/eats.mp4")
duration = clip.duration
# Number of clips will be generate
outputClips = 2
# Where files are saved
savePath = "D:\echocloud/"

clipsDuration = duration / outputClips
clipsCount = 0
clipStart = 0
clipEnd = clipsDuration
chiffre = randint(10000,99999)

while clipsCount < outputClips:

    clipsCount = clipsCount + 1
    newfile = clip.subclip(clipStart, clipEnd)

    clipEnd = clipEnd + clipsDuration
    clipStart = clipStart + clipsDuration

    savePathF = savePath + str(clipsCount) + "MVS" + str(chiffre) + ".mp4"
    newfile.write_videofile(savePathF)

print("All done")

