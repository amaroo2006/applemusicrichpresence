import rumps
import os

class StatusBarApp(rumps.App):
    def __init__(self, name, icon, music):
        super(StatusBarApp, self).__init__(name=name, icon=icon)
        self.music = music
        self.menu.update([])
        
    @rumps.timer(1)
    def updateMenu(self,_):
        trackInfo = self.music.getTrackInfo()

        self.menu.values()[0].title = trackInfo[0] + " - " + trackInfo[1]
        self.menu.values()[0].icon = str(os.path.join(os.getenv("HOME"), ".applemusicrp", "albumcover.png"))
        self.menu.values()[0].dimensions=(35,35)

        self.menu.update([])
    
    
    @rumps.clicked("Play/Pause")
    def playPause(self,_):
        # playing
        playing = self.music.getPlayerState()[1]
        if(playing):
            self.menu.values()[1].title="Play"
            self.updateMenu(_)
            
        # paused
        else:
            self.menu.values()[1].title="Pause"
            self.updateMenu(_)

        self.music.playPause()

    @rumps.clicked("Skip")
    def skip(self, _):
        self.music.skip()
        self.updateMenu(_)
    
    @rumps.clicked("Backtrack")
    def shuffle(self, _):
        self.music.backtrack()
        self.updateMenu(_)