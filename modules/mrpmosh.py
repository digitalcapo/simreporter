import subprocess
import os
import tobias

class mrpmosh():
    def __init__(self):
        self.tobias = tobias.JSON()
        self.ids = self.tobias.loadThis('.\\config\\latestIDs.json')
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def mrp(self,customID=''):
        for video in self.ids:
            videoname = ''
            brk = False
            if len(customID) > 2:
                videoname = customID
                brk = True
            else:
                videoname = video
            filename = self.root+'\\media\\videos\\{0}.mp4'.format(videoname)
            print(filename)
            os.system('cmd /c "python do_the_mosh.py {0}"'.format(filename))
            if brk == True:
                break

if __name__ == '__main__':
    mrpmosh = mrpmosh()
    mrpmosh.mrp(customID='2818546')