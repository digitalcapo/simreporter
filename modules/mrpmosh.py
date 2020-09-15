import subprocess
import os
import tobias

"""
This module is called mrpmosh. I don't know how to properly document this.
It will datamosh a video from a file or list of files using an unique ID
That's it. Everything is hardcoded. Welcome to programming hell.
"""
class mrpmosh():
    def __init__(self, vname):
        self.tobias = tobias.JSON()
        self.vname = vname
        self.ids = self.tobias.loadThis('.\\config\\{0}_IDs.json'.format(vname))
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def mrp(self,customID=''):
        root = self.root+'\\media\\videos\\'.format(self.vname)
        if not os.path.exists(root):
            os.mkdir(root)
        for video in self.ids:
            videoname = ''
            brk = False
            if len(customID) > 2:
                videoname = customID
                brk = True
            else:
                videoname = video
            filename = root+'{0}.mp4'.format(videoname)
            print("Let's mosh this MF {0}".format(filename))
            os.system('cmd /c "python do_the_mosh.py {0}"'.format(filename))
            if brk == True:
                break

if __name__ == '__main__':
    vname = 'fungui'
    mrpmosh = mrpmosh(vname)
    mrpmosh.mrp(customID='')