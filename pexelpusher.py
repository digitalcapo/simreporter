
import tobias

tobiasj = tobias.JSON()
api_key = tobiasj.loadThis('api_key.json')[0]

import os
from pypexels import PyPexels
import requests
import montaner
import shutil
from PIL import Image

# instantiate PyPexels object


class PexelPusher:
    def __init__(self):
        self.py_pexel = PyPexels(api_key=api_key)

        self.latestIDs = []

    def searchVideos(self, query='', qSize=10):
        selected_videos = []
        search_videos_page = self.py_pexel.videos_search(query=query, per_page=qSize)
        while True:
            for video in search_videos_page.entries:
                self.latestIDs.append(video.id)
                if video.width/video.height >= 1.33:
                    #print(video.id, video.user.get('name'), video.url)
                    image = video.image.split('?')
                    selected_videos.append(image[0])
            if not search_videos_page.has_next:
                break
            search_videos_page = search_videos_page.get_next_page()
        return selected_videos
        

    def getThumbs(self, querylist,qSize):
        nlist = 0
        root = '.\\cacheimages\\'
        for query in querylist:
            video_list = self.searchVideos(query, qSize)
            nlist = '{:04d}'.format(querylist.index(query)+1)
            cache_folder = ('./cacheimages/')
            if not os.path.exists(cache_folder):
                os.mkdir(cache_folder)
            for imageurl in video_list:
                r = requests.get(imageurl)
                filename = cache_folder+os.path.split(imageurl)[1]
                with open(filename, 'wb') as outfile:
                    outfile.write(r.content)
                    outfile.close()
                image = Image.open(filename)
                image.thumbnail((400,400))
                image.save(filename)

    def makeContactSheet(self):
        root = '.\\cacheimages\\'
        index = 1
        images = []
        for root, dirs, files in os.walk(root):
            #print(root)
            for file in os.listdir(os.path.join(root)):
                    images.append(os.path.join(root,file))
        outfile = os.path.join('.\\cs_{0}.jpg'.format(index))
        montaner.generate_montage(images, outfile)
        img = Image.open(outfile)
        img.show()
        self.saveVideoIDs()
        shutil.rmtree(root)

    def saveVideoIDs(self):
        file = '.\\latestIDs.json'
        if os.path.exists(file):
            os.remove(file)
            tobiasj.saveThis(self.latestIDs, file)
        else:
            tobiasj.saveThis(self.latestIDs, file)

    def downloadVideos(self):
        file = '.\\latestIDs.json'
        ids = tobiasj.loadThis(file)
        namelist = []
        for videoid in ids:
            video = self.py_pexel.single_video(video_id=videoid)
            for each in video.video_files:
                if 'hd' in each['quality']:
                    link = each['link']
                    name = 'ID{0}_{1}'.format(videoid,video.user.get('name'))
                    if name not in namelist:
                        namelist.append(name)
                    filename = './videos/{0}.mp4'.format(videoid)
                    if not os.path.isfile(filename):
                        r = requests.get(link)
                        with open(filename, 'wb') as outfile:
                            outfile.write(r.content)
                            outfile.close()
                        print('Downloaded this video: {0}'.format(filename))
                    else:
                        print('Skipping this video because it already exists: {0}'.format(filename))
        tobiasj.saveThis(namelist,'.\\credits.json')
            # print(video.id, video.user.get('name'), video.url)

if __name__ == '__main__':
    ppusher = PexelPusher()
    query = ['city', 'grass']
    ppusher.getThumbs(query, 6)
    ppusher.makeContactSheet()
    #ppusher.downloadVideos()