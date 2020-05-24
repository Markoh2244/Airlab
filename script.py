import pymap3d as pm
import os
import cv2
import numpy as np

x,y,z = pm.geodetic2ecef(5,5,5)
path="/Users/marko/Desktop/CMU/20S/Airlab/images"
frameCount=len(os.listdir(path))


#######################################################
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

#Sourced from: https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
########################################################

def readFile(path):
    with open(path, "rt") as f:
        return f.read()
    pass
cap = cv2.VideoCapture("/Users/marko/Desktop/CMU/20S/Airlab/video.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)      
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps


def extractInfo():
    final=[]
    the=[]
    new=dict()
    read = readFile('/Users/marko/Desktop/CMU/20S/Airlab/62.csv')
    split=read.split("\n")
    for i in split:
        final.append([i])
    final.pop(0)
    for i in range(0,len(final)-1):
        c=final[i][0].split(',')
        c[3]=c[3].replace("'","")
        c[3]=c[3].replace("]","")
        c[3]=c[3].replace('"',"")
        c[3]=c[3].strip()
        c[3]=float(c[3])
        the.append(c[3])
        new[c[3]]=[float(c[10]),float(c[11])]
    return the

def adjust():
    read = readFile('/Users/marko/Desktop/CMU/20S/Airlab/62.txt')
    split=read.split("\n")
    sTime=float(split[1].split(":")[2])
    tInterval=duration//frameCount
    times=[]
    info=extractInfo()
    for i in range(0,frameCount):
        times.append(sTime+(i*tInterval))
    return times



def produce():
    for i in range(0,frameCount):
        print(find_nearest(extractInfo(),adjust()[i]))
        f = open("/Users/marko/Desktop/CMU/20S/Airlab/images/file{}.txt".format(i),"w+")
        f.write("Time %d\r\n:" % (adjust()[i])) 
        # f.write("Location%d\r\n:" % (location)) 
        f.close() 
# produce()
# extractInfo()
produce()