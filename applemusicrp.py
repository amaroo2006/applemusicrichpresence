#!/usr/bin/env python3.11

from ScriptingBridge import SBObject, SBApplication
from pypresence import Presence
from rumps import *
from threading import Thread

import datetime
import time
import asyncio
import syslog
import requests

import StatusBar
import Music


def richPresenceLoop(musicInfo):
    # create asynchronous event loop for multithreaded execution
    try:
        asyncio.get_event_loop()
    except:
        asyncio.set_event_loop(asyncio.new_event_loop())

    # application info
    client_id = "1084641054055211128"
    RPC = Presence(client_id)

    # connect to discord
    while True:
        try:
            RPC.connect()
            
        except:
            time.sleep(2)

        else:
            break

    # update rich presence
    while True:
        try:
            trackName, album, artist, artURL = musicInfo.getTrackInfo()
            playerPosition = musicInfo.getPlayerState()[0]
            RPC.update(
                large_image = artURL,
                details=trackName
                + " - "
                + album,
                state="by "
                + artist
                + " - "
                + str(
                    datetime.timedelta(minutes=0, seconds=int(playerPosition))
                )[-5:])
            
        except:
             time.sleep(1)
             RPC.connect()

        else:
            time.sleep(1)

def main():

    # create music object, get initial info
    music = Music.Music()
    trackInfo = music.getTrackInfo()
    
    # start rich presence
    richPresence = Thread(target=richPresenceLoop, args=[music])
    richPresence.start()

    # create status bar app
    app = StatusBar.StatusBarApp(name="Apple Music Rich Presence", icon="imgs/trayIcon.png", music=music)

    try:
        app.menu.add(rumps.MenuItem(
                title = trackInfo[0] + " - " + trackInfo[1],
                icon='imgs/default_img.png',
                dimensions=(35,35)))
        app.run()
    
    except Exception as error:
        syslog.syslog(syslog.LOG_ALERT, str(error))
        syslog.syslog(syslog.LOG_ALERT, "except ran")

    
if __name__ == "__main__":
    main()
