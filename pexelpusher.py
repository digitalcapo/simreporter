
import argonauts

argonaut = argonauts.JSON()
api_key = argonaut.loadThis('api_key.json')[0]

import os
from pypexels import PyPexels
import requests
import montaner
from PIL import Image

# instantiate PyPexels object


class PexelPusher:
    def __init__(self):
        self.py_pexel = PyPexels(api_key=api_key)

    def searchVideos(self, query='', qSize=10):
        selected_videos = []
        search_videos_page = self.py_pexel.videos_search(query=query, per_page=qSize)
        while True:
            for video in search_videos_page.entries:
                #print(video.id, video.user.get('name'), video.url)
                image = video.image.split('?')
                selected_videos.append(image[0])
            if not search_videos_page.has_next:
                break
            search_videos_page = search_videos_page.get_next_page()
        return selected_videos
        

    def getThumbs(self, querylist,qSize):
        nlist = 0
        for query in querylist:
            video_list = self.searchVideos(query, qSize)
            nlist = '{:04d}'.format(querylist.index(query)+1)
            cache_folder = ('./cacheimages/{1}_{0}/').format(query,nlist)
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
        for root, dirs, files in os.walk(root):
            for folder in dirs:
                images = []
                for file in os.listdir(os.path.join(root,folder)):
                    images.append(os.path.join(root,folder,file))
                outfile = os.path.join(root,'cs_{0}.jpg'.format(folder))
                montaner.generate_montage(images, outfile)

if __name__ == '__main__':
    ppusher = PexelPusher()
    query = ['urban+night', 'city', 'buildings']
    ppusher.getThumbs(query, 10)
    ppusher.makeContactSheet()