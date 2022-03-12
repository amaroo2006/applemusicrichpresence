# applemusicrichpresence
Discord Rich Presence for Apple Music on macOS

Usage:

Install required libraries:

 `pip3 install pyobjc`
 `pip3 install pypresence`
 `pip3 install coverpy`
 
Go to Advanced settings on your Discord profile. Enable Application Test Mode. A prompt should appear asking for an Application ID
Create an application through the Discord Developer Portal, name it whatever you want. Copy the client ID and paste it into the code. Copy the Application ID and paste it into the prompt on Discord.

Open Apple Music on your Mac and start playing some music and make sure Discord is open, with Activity Status on. Then run the Python script using 
 `python3 applemusicrc.py`
