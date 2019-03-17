
import os.path
from subprocess import check_output, STDOUT 
 


def getDuration(filename):

    command = [
        'ffprobe', 
        '-v', 
        'error', 
        '-show_entries', 
        'format=duration', 
        '-of', 
        'default=noprint_wrappers=1:nokey=1', 
        filename
      ]

    output = check_output( command, stderr=STDOUT )
    return float(output)


paths = raw_input("enter path = ")
time = 0


for(path, dire, files) in os.walk(paths):
    for f in files:
        if f.find(".mp4") != -1 or f.find(".mkv") != -1:
            name = path + "/" + f
            
            time = time + getDuration(name)
            pass
        pass
    pass


hour = (int)(time/3600)
minute = ((int)(time % 3600) ) / 60
print ("total time = " + str(hour) + " hours and " + str(minute) + " minutes")

