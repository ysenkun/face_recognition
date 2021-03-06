import cv2
import time 

cap = cv2.VideoCapture(0)

user_name = input("\n Input your name \n")
print("Press A for the photo shoot")
finish_num = 1

i = 0
n = 1
while True:

    ret, frame = cap.read()

    #cv2.rectangle(frame,(450,130),(800,500),(0, 255, 0),thickness=3)
    
    cv2.imshow('cap', frame)

    key = cv2.waitKey(33)
    
    if key == ord('a'):
        num = format(n,'03')
        cv2.imwrite('./src/data/images/{}{}.jpg'.format(user_name,num), frame)

        #cv2.imwrite('./src/data/images/{}.jpg'.format(user_name), frame)
        n += 1
        i += 1
    i += 1

    if key == 27 or  n == finish_num + 1:
        break

print("Finish")
cap.release()
cv2.destroyAllWindows()
