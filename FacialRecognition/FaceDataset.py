import cv2
import os

def main():
    if os.path.isdir("dataset"):
        pass
    else:
        os.mkdir("dataset")
    print("Sedang menjalankan kamera. Harap tunggu...")
    cam = cv2.VideoCapture(0)
    os.system("cls")
    cam.set(3, 640) 
    cam.set(4, 480) 

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    while True :
        face_id = input('\n Masukkan NIS : ')
        path = "dataset"
        if os.path.isdir("dataset"):   
            ids = set()
            imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
            for imagePath in imagePaths:
                id = int(os.path.split(imagePath)[-1].split(".")[1])
                ids.add(id)
            if int(face_id) in ids :
                input("NIS telah terdaftar...")
                os.system("cls")
            else :
                break
        else :
           break
    count = 0

    while(True):

        ret, img = cam.read()
        img = cv2.flip(img, 2) 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 2.8, 3)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            
        cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff
        if k == 27:
            break
        elif count >= 30: 
            break


    cam.release()
    cv2.destroyAllWindows()
    os.system("cls")



