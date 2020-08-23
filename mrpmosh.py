import subprocess
import os
import tobias

class mrpmosh():
    def __init__(self):
        self.jason = tobias.JSON()

    def mrp(self,justone=False):
        videos = []
        for each in os.listdir('./videos'):
            os.system('cmd /c "do_the_mosh.py {0}"'.format('./videos/'+each))
            if justone==True:
                break

if __name__ == '__main__':
    mrpmosh = mrpmosh()
    mrpmosh.mrp(justone=True)