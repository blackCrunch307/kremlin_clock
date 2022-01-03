import sys
import time
import vlc

player_hours = vlc.MediaPlayer("hour.mp3")
player_quarters = vlc.MediaPlayer("quarter.mp3")
hours = int(sys.argv[1])
mins = int(sys.argv[2])


def strike_hours(times):
    for i in range(times):
        player_hours.play()
        time.sleep(0.1)
        time.sleep(player_hours.get_length() / 1000)
        player_hours.stop()


def chime_quarters(times):
    for i in range(times):
        player_quarters.play()
        time.sleep(0.1)
        time.sleep(player_quarters.get_length() / 1000)
        player_quarters.stop()


if mins == 15:
    chime_quarters(1)
if mins == 30:
    chime_quarters(2)
if mins == 45:
    chime_quarters(3)
if mins == 0:
    chime_quarters(4)
    strike_hours(hours)
