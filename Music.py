from ScriptingBridge import SBObject, SBApplication
import os
import requests
import syslog


class Music:
    def __init__(self):
        self.musicApp = SBApplication.applicationWithBundleIdentifier_("com.apple.Music")
        print(self.musicApp.currentTrack().name())
    def getArtURL(self, album, artist):
        searchTerm = album.replace(" ", "+") + "+" + artist.split(",")[0].replace(" ", "+")
        data = requests.get("https://itunes.apple.com/search?term=" + searchTerm + "&country=us&entity=album&limit=4")
        url = ""

        for item in data.json()['results']:
            #print(item)
            if(item['collectionName'] == album and (item['artistName'] in artist or artist in item['artistName'])):
                url = item['artworkUrl100']

        if url == "":
            url = "https://www.iphonefaq.org/files/styles/large/public/apple_music.jpg"

        return url

    def getTrackInfo(self):
        # get track info
        trackName = str(self.musicApp.currentTrack().name())
        album = str(self.musicApp.currentTrack().album())
        artist = str(self.musicApp.currentTrack().artist())
        year = str(self.musicApp.currentTrack().year())

        # get image url as well as local copy of image
        artURL = self.getArtURL(album, artist)
        try:
            art = self.musicApp.currentTrack().artworks()[0].rawData().get().data()
            if (os.path.exists(os.path.join(os.getenv("HOME"), ".applemusicrp", "albumcover.png")) == False):
                os.mkdir(os.path.join(os.getenv("HOME"), ".applemusicrp/"))
            art.writeToFile_atomically_(os.path.join(os.getenv("HOME"), ".applemusicrp", "albumcover.png"), False)
            
        except Exception as e:
            print(e)

        return [trackName, album, artist, artURL]
    
    def getPlayerState(self):
        # get player state
        playerPosition = self.musicApp.playerPosition()
        playing = True if self.musicApp.playerState() == 1800426320 else False

        return [playerPosition, playing]
    
    def skip(self):
        self.musicApp.nextTrack()
    
    def playPause(self):
        self.musicApp.playpause()
    
    def backtrack(self):
        self.musicApp.backTrack()