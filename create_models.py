import joblib
import cv2
import os
import face_recognition



def prepare_images(section):
    path = f'images/{section}'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(tuple(os.path.splitext(cl)[0].split(" ")))
        print(classNames)
    return images,classNames

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def create_model():
    images, classNames = prepare_images("L3C1")
    encoding_list = findEncodings(images)

    model = classNames, encoding_list

    joblib.dump(model,"L3C1_model")

    print("sucessfully created a model")


create_model()

