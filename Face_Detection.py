#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[2]:


pip install opencv-python-headless


# In[ ]:


import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default (5).xml')

cap = cv2.VideoCapture(0)

while True :
    c=0
    _,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces : 
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,253,255), 2)
        c = c+1
        cv2.putText(img,"Face : "+str(c),(x-12,y-12),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,253,255),2)

    cv2.imshow('img',img)
    
    k = cv2.waitKey(30) & 0xff
    if(k==27) :
        break

cap.release()


# In[ ]:




