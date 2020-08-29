import subprocess
import os
import tobias

class mrpmosh():
    def __init__(self):
        self.tobias = tobias.JSON()
        self.ids = self.tobias.loadThis('.\\config\\latestIDs.json')
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def mrp(self,justone=False):
        for video in self.ids:
            filename = self.root+'\\media\\videos\\{0}.mp4'.format(video)
            print(filename)
            os.system('cmd /c "python do_the_mosh.py {0}"'.format(filename))

if __name__ == '__main__':
    mrpmosh = mrpmosh()
    mrpmosh.mrp(justone=True)