from Foundation import *
from ScriptingBridge import *
import pypresence
from pypresence import Presence
import coverpy
import time
import requests

client_id = "PUT-CLIENT-ID-HERE"  # find your client ID by creating an application through the discord developer portal
music = SBApplication.applicationWithBundleIdentifier_("com.apple.Music")

RPC = Presence(client_id)
RPC.connect()
limit = 1
c = coverpy.CoverPy()


while True:
    try:
        result = c.get_cover(music.currentTrack().album(), limit)

    except coverpy.exceptions.NoResultsException:
        print("Nothing found.")
    except requests.exceptions.HTTPError:
        print("Could not execute GET request")

    RPC.update(
        large_image=result.artwork(100),
        details=music.currentTrack().name() + " - " + music.currentTrack().album(),
        state=music.currentTrack().artist(),
    )
    #
    # print(music.currentTrack().name() + " - " + music.currentTrack().artist())

    time.sleep(0.5)
