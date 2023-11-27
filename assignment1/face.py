import cv2
face=cv2.CascadeClassifier( r"C:\Users\Rafie\Downloads\haarcascade_frontalface_default (2).xml")
cap=cv2.VideoCapture(0)
print(cv2.CascadeClassifier.empty(face))
images=cv2.imread(r"C:\Users\Rafie\Downloads\440px-Twemoji_1f600.svg.png")

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.1 ,4)
    for (x,y,w,h) in faces:
        
        imgag=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)
        my_image=cv2.resize(images,(w,h))
        img[x:x+w,y:y+h] = my_image 
        
        cv2.imshow('lil00',img)
    if cv2.waitKey(30)  & 0xff == ord('q'): 
        break
cap.release()
cv2.destroyWindow()