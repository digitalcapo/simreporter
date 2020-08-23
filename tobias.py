import json
import os

class JSON(object):
    '''
    Class to write and read JSON files
    '''
    def __init__(self):
        pass

    def saveThis(self, data, path):
        try:
            filename = os.path.abspath(path)
            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
                outfile.close()
                print("Booyah! This file was saved"
                       ": {0}".format(filename))
        except Exception as e:
            print ("I believe I just 'blue' myself"
                   ": {0}".format(e))

    def loadThis(self, path):
        try:
            filename = os.path.abspath(path)
            with open(filename, 'r') as readfile:
                data = json.load(readfile)
                readfile.close()
                print("That's a huge load!"
                   ": {0}".format(filename))
                return data
        except Exception as e:
            print ("I prematurely shot my load"
                   ": {0}".format(e))