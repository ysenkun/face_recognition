import cv2
import time 

cap = cv2.VideoCapture(0)

cascade_file = "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_file)


user_name = input("\n Input your name \n")
finish_num = 1

# print("撮影を開始します")
# time.sleep(2)
# print("3")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")


i = 0
n = 1
while True:

    ret, frame = cap.read()

    cv2.rectangle(frame,(400,100),(1000,600),(0, 255, 0),thickness=3)
    
    cv2.imshow('cap', frame)

    key = cv2.waitKey(33)
    if key == ord('a'):
        num = format(n,'03')
        cv2.imwrite('./src/data/images/{}{}.jpg'.format(user_name,num), frame)
        n += 1
        i += 1
    i += 1

    if key == 27 or  n == finish_num + 1:
        break

print("撮影が完了しました")
cap.release()
cv2.destroyAllWindows()
