import cv2
face=cv2.imread(r"C:\Users\Rafie\Downloads\lili.jpg")
image=cv2.imread(r"D:\IMG_20231012_133327_774.jpg")
image[170:320,190:350]=face
cv2.imshow('lil',image)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()


 