import os
import time
import cv2

path="Images"

images=[]

for file in os.listdir(path):
    name , ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path + "/" + file
        images.append(file_name)

print(len(images))
count = len(images)
frame = cv2.imread(images[0])

height , width , channels = frame.shape
size = (width , height)
print(size)

out=cv2.VideoWriter("Project.mp4" , cv2.VideoWriter_fourcc(*'DIVX') , 0.8 , size)

for i in range(0 , count):
    img=cv2.imread(images[i])
    out.write(img)

out.release()
print("Done....!!")