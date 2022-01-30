import time
import sys
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play




print("Hello World")
#input("Path to Billy?")
today = datetime.today().weekday()
n = 0
dayCheck = 0
billy = AudioSegment.from_mp3("BillyJoel.mp3")
time.sleep(5)

while(today != 5):
    print("Not time for Billy")
    time.sleep(43200)

while(today == 5):
    now = time.localtime()
    print(now[3],now[4])
    
    if(dayCheck == 0):
     print("Right Day  for Billy!")
     dayCheck = dayCheck+1
    
    if(now[3]<20):
        print("Too Early for Billy!")
        time.sleep(3600)

    if(now[3]==20 and now[4]<45):
        print("Getting Closer!")
        time.sleep(600)
    
    if(now[3]==20 and 45< now[4] and now[4]<55):
        print("He's Warming Up Backstage!")
        time.sleep(120)
    if(now[3]==20 and 55  < now[4] and now[4]<59):
        print("Almost Time!")
        time.sleep(30)
    if(now[3]==20 and now[4]==59 and now[5]>30):
        print("Here he is!!!")
        print(now[3])
        play(billy)
    if(now[3]>=21):
        print(now[3],now[4])
        print("Not time for Billy")
        time.sleep(43200)