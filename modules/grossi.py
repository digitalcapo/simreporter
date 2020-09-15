import os
import tobias
import random
from moviepy.editor import *

mosh_path = 'X:/cloud/Dropbox/capo_dev/simreporter/simreporter/media/videos/fungui'
output_path = 'X:/cloud/Dropbox/capo_dev/simreporter/simreporter/media/edits/fungui'

if not os.path.exists(output_path):
    os.mkdir(output_path)

class Grossi(object):
    """An automated editor using analaudio.py as EDL"""
    def __init__(self, vname):
        super(Grossi, self).__init__()
        self.vname = vname
        self.tobias = tobias.JSON()
        self.ids = self.tobias.loadThis('.\\config\\{0}_IDs.json'.format(vname))
        
    def theGathering(self, path):
        thechosen = []
        for file in os.listdir(path):
            for id in self.ids:
                if str(id) in str(file):
                    thechosen.append(file)
                    print('You have been selected: {0}'.format(file))
                else:
                    continue
        print('There are {0} videos in your selection'.format(len(thechosen)))
        return thechosen

    def theFiltering(self, thechosen, audiolen):
        theseeder = int((audiolen / 7) +  random.randint(1,5))
        print(theseeder)
        thelucky = []
        for x in range(0,theseeder):
            thelucky.append(thechosen[random.randint(0,len(thechosen)-1)])
        print(thelucky)
        print(len(thelucky))
        return thelucky

    def theEditing(self, thelucky):
        thelist = []
        root = mosh_path
        for lucky in thelucky:
            filename = os.path.join(root, lucky)
            try:
                clip = VideoFileClip(filename, audio=False)
                duration = int(clip.duration)
                clipin = 1+(random.randint(1,2))
                clipout = clipin+random.randint(1,2)
                clip = clip.subclip(clipin, clipout)
                thelist.append(clip)
            except Exception as e:
                print(e)
                continue
        thefinal  = concatenate_videoclips(thelist)
        thefinalfinal = (thefinal.fx( vfx.speedx, 1.25)
                 .fx( vfx.resize, width=1920))
                 # .fx( vfx.blackwhite))
        rgn = random.randint(1,4999)                 
        thefinalfinal.write_videofile(output_path+"/comp_{0}_{1}.mp4".format(self.vname, rgn))


if __name__ == '__main__':
    grossi = Grossi('fungui')
    thegather = grossi.theGathering(mosh_path)
    thefilter = grossi.theFiltering(thegather, 360)
    grossi.theEditing(thefilter)