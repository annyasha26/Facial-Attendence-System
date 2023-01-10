import cv2
import numpy as np
import face_recognition
from handle_sheet_index import update_col_index, get_current_index
from google_sheet import invoke_present, get_sheet_name
import sys
import joblib



def markAttendance(student_id,current_index):
    invoke_present(student_id,current_index)
       

def attendence_process(instruct,section,subject,col_idx):
    get_sheet_name(section,subject) #set the sheet name 
    print("starting attendence process")
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    if instruct==None:

        print("inside if")
        classNames, encodeListKnown = joblib.load(f'models/{section}_model')

        # images, classNames = prepare_images(section)
        # encodeListKnown = findEncodings(images)
        attended_student = []

        while True:
            success, img = cap.read()
            #img = captureScreen()
            imgS = cv2.resize(img,(0,0),None,0.25,0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
            
            for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                # print(f"matches: {matches}")
                faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                # print("facedistance",faceDis)
                matchIndex = np.argmin(faceDis)
                # print("distance value",faceDis[matchIndex])
                if faceDis[matchIndex] < 0.35:
                    
                    print("inside first if")
                    print("distance value",faceDis[matchIndex])
                    # print(f"matchIndex: {matchIndex}")
                    
                    if matches[matchIndex]:
                        student_info = classNames[matchIndex]
                        student_id = student_info[1]
                        student_name = student_info[0]
                        y1,x2,y2,x1 = faceLoc
                        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(img,student_name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                        if student_id not in attended_student:
                            cv2.putText(img,student_name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                            attended_student.append(student_id)
                            print(f"attendence of student {student_name} is going to happen")
                            markAttendance(student_id, col_idx)
                        
                        else:
                            cv2.putText(img,"Present",(x1+6,y1+5),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.imshow('Webcam',img)
            cv2.waitKey(1)
           
    elif instruct=="Next":
        print("inside Next section")
        cap.release()
        cv2.destroyAllWindows()
        update_col_index(subject, section)
        return
    else:
        print("inside stop section")
        cap.release()
        cv2.destroyAllWindows()
        update_col_index()
        sys.exit()

        

        
