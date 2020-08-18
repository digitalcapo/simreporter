
import argonauts

argonaut = argonauts.JSON()
api_key = argonaut.loadThis('api_key.json')[0]

import os
from pypexels import PyPexels
import requests
import contactsheet
import montaner

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
            nlist = nlist+1
            cache_folder = ('./cacheimages/{:04d}/').format(nlist)
            if not os.path.exists(cache_folder):
                os.mkdir(cache_folder)
            for imageurl in video_list:
                r = requests.get(imageurl)
                filename = cache_folder+os.path.split(imageurl)[1]
                with open(filename, 'wb') as outfile:
                    outfile.write(r.content)
                    outfile.close()

    def makeContactSheet(self):
        root = './cacheimages/'
        folderlist = []
        rfiles = []
        rfilename = []
        for folder in os.listdir(root):
            folderlist.append(folder)
            rfilename.append((os.path.join(root,folder,'cs_{0}.jpg')).format(folder))
        for sfolder in folderlist:
            for file in os.listdir('./cacheimages/'+sfolder):
                rfiles.append(os.path.join('./cacheimages',sfolder,file))
        return rfiles, rfilename[0]


if __name__ == '__main__':
    ppusher = PexelPusher()
    query = ['urban+night']
    ppusher.getThumbs(query, 10)
    rfiles, rfolder = ppusher.makeContactSheet()
    montaner.generate_montage(rfiles, rfolder)