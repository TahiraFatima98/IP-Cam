import urllib.request
import cv2
import numpy as np

url='http://192.168.1.127:8080/shot.jpg'

while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    Frame = cv2.resize (img, (700,500))

    # all the opencv processing is done here
    
    cv2.imshow('test',Frame)
    
    if ord('q')==cv2.waitKey(10):
        exit(0)


 

 

