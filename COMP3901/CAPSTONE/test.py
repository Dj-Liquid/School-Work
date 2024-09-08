from ultralytics import YOLO
import cv2
from datetime import datetime
from email.mime.image import MIMEImage
import time
from test_email_sender import EmailSender
from local_database import CaptureDatabase
from email_database import Emails
import os

host = "localhost"
user = "root"
password2 = "damc18"
database = "Capture"

sender_email = "sici3902@gmail.com"
password = "euck qnjq kobv isro"  
police=False
security=False
gun=False
knife=False
notify_count=0
police_email="robinsond993@gmail.com"
security_email="robinsond993@gmail.com"


#db = Emails(host, user, password2, database)

#A=db.get_emails()

#db.close_connection()

#receiver_emails=["robinsond993@gmail.com","sici3902@gmail.com"]
receiver_emails=[]
#receiver_emails+= A
print(receiver_emails)


danger_zone = [10, 0, 270, 479 ]#NEED TO FIX DANGER ZONE

#FUNCTION TO DETERMINE DANGER ZONE
def CompLoc(list1, list2):
    for x in range(4):
        if abs(list1[x] - list2[x]) > 100:
            return False
    return True

"""def CompLoc2(euclidean_midpoints):
     for eu in euclidean_midpoints[0][1]: 
        cv2.rectangle(frame_, (eu[0], eu[1]), (eu[0]+3, eu[1]+3), (50,200,50), 3)
        if eu[0] >= 0 and eu[0] <= 270 and eu[1] >= 0 and eu[1] <= 480:
            cv2.putText(frame_, "In Zone", (eu[0], eu[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 100), 2, cv2.LINE_AA)"""

def take_image(cv2,cap):
     cv2.imwrite("Suspect_image.jpg",frame_)
     #cap.release()
     with open("Suspect_image.jpg","rb") as img:
          image_data=img.read()
     image=MIMEImage(image_data,name="Suspect_image.jpg")
     return image

#db_manager =  CaptureDatabase(host="localhost", user="root", password="damc18", database="Capture")
#db_manager.empty_table()
#db_manager.create_table()
lst=[]
location_danger=0
# load yolov8 model
model = YOLO('yolov8n.pt')
model2 = YOLO('last36.pt')

VIDEOS_DIR = os.path.join('.', 'videos')
cap = cv2.VideoCapture(0)
ret, frame_ = cap.read()
H, W, _ = frame_.shape
# load video
video_path = './test.mp4'
video_path_out = '{}_out.mp4'.format(os.path.join(VIDEOS_DIR, 'Restrcited_Area_Test')) # Output video file path
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))


ret = True
# read frames
while ret:
    ret, frame_ = cap.read()

    if ret:

        #out.write(frame)
        results = model.track(frame_, persist=True,tracker="bytetrack.yaml")
        results2 = model2.track(frame_,persist=True,tracker="bytetrack.yaml")
        
        #frame_ = results[0].plot()
        info = results[0]

        
        cv2.rectangle(frame_, (0, 0), (240,480), (0,100,300), 3)#MIN X MIN Y MAX X MAX Y
        cv2.putText(frame_, "Restricted Area", (160, 124), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        
        box = results[0].boxes.xywhn  
        box2=results2[0].boxes.xywhn
        clID = results[0].boxes.cls 
        item_ID = results2[0].boxes.cls
        item_scores=results2[0].boxes.conf
        tensor_ids = info.boxes.id  

        coordinates_to_check = [
            [160, 134, 231, 264],
            [160, 134, 231, 264],
            [160, 134, 232, 264]
        ]
        

        
        if tensor_ids is not None:
            try:
                numpy_ids = tensor_ids.numpy()
                euclidean_midpoints, euclidean_midpoints2 = [],[]
                b = 0
                #b2=0
                item_scores_list,item_ID_list=item_scores, item_ID
                b2=box2
                
                for id in numpy_ids:
                    count_area=0
                    if(clID[b] == 0):#TESTING IF HUMAN
                         zone_test=True
                         
                         start_time = time.time()
                         x_min, y_min, x_max, y_max=box[b]

                         x_min, x_max = (int(x_min*640), int(x_max*640))
                         y_min, y_max = (int(y_min*480), int(y_max*480))

                         x_min = x_min - int(x_max/2)
                         y_min = y_min - int(y_max/2)
                         x_max = x_min + x_max
                         y_max = y_max + y_min


                         #current_time = datetime.now().strftime("%H:%M:%S")
                         #lst=(id,"has an object",current_time)
                         cv2.rectangle(frame_, (x_min, y_min), (x_max,y_max), (b*150,b*50,0), 3)
                         cv2.putText(frame_, f"id:{id}", (x_min, y_min), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
                         euclidean_midpoints+=[[int(x_min+(x_max-x_min)/2) , int(y_min+(y_max-y_min)/2)]]

                         co_ordinates=[x_min, y_min, x_max, y_max]
                         print(co_ordinates)
                         query=f"""
                         SELECT ID FROM CAPTURE 
                         WHERE ID ={id}
                         """
                         #id_list=db_manager.get_ids()
                         id_list=[]
                         if(id not in id_list):
                             new_info=[int(id),False,0,0]#fix_time
                             #db_manager.insert_info(new_info)
                         ######################################## 
                         #count_area = db_manager.get_count([int(id)])
                         #print("DB_Count_Area",count_area)   
                         if(CompLoc(co_ordinates,danger_zone)):
                         #if(CompLoc2(euclidean_midpoints)):
                             cv2.putText(frame_, "Restricted Entrance", (co_ordinates[0], co_ordinates[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 100), 2, cv2.LINE_AA, False)
                             print("Restricted")
                               # Pass ID as a tuple
                             #count_area=db_manager.get_count(int(id))
                             #count_area=count_area+1
                             new_info=[int(id),int(count_area)]#fix_time
                             #db_manager.update_count([int(id)])
                             #count_area = db_manager.get_count([int(id)])
                             #print("Count_area",count_area)
                             zone_test=False
                             location_danger=1
                             """if(count_area<=3):###UPDATE THREAT
                                  score=db_manager.get_score([int(id)])#Here
                                  score=score+location_danger
                                  if(score>=10):q
                                       score=10
                                       new_info=[int(score),int(id)]
                                       db_manager.update_threat(new_info)"""
                         else:
                            pass
                            #db_manager.reset_count([int(id)])
                              #RESET HIS SCORE
                         
                         ###REVISIT
                         '''
                         if((not zone_test)and(count_area==0)):#USE ZONE VARIABLE IN DATABASE
                              notify_count=1
                              #email_sender = EmailSender(sender_email, security_email, password)
                              email_sender = EmailSender(sender_email, receiver_emails, password)
                              subject = "POTENTIAL THREAT IN BANK"
                              body = "XXXXXX ALERT XXXXXX\
                                \n\nPERSON IN RESTRICTED AREA .\
                                \n\nSEARCH AND APPREHEND "
                              print("Person In restricted area")
                              email_sender.send_email(subject, body,None)
                             
                             
                         time_cycle=db_manager.get_time([int(id)])
                         time_cycle+=1
                         time_info=[int(time_cycle),int(id)]
                         print("time_cycle ", time_cycle)


                         db_manager.update_time(time_info)
                         if(time_cycle>=201):
                              pass
                         elif((time_cycle==200)):#SEND LOCATION INFORMATION
                              email_sender = EmailSender(sender_email, receiver_emails, password)
                              subject = "POTENTIAL THREAT IN BANK"
                              body = "XXXXXX ALERT XXXXXX\
                                \n\nIndividual in bank for four hours .\
                                \n\nIt is advised to approach individual "
                              email_sender.send_email(subject, body,None)
                              time_danger=1
                              print("Second cycle reached, guard contacted")
                              """score=db_manager.get_score([int(id)])
                              score=score+time_danger
                              if(score>=10):
                                      score=10
                              new_info=[int(score),int(id)]
                              print("Second cycle reached, danger score increased")
                              db_manager.update_threat(new_info)"""
                         elif((time_cycle==100)):#SEND LOCATION INFORMATION
                              email_sender = EmailSender(sender_email, receiver_emails, password)
                              subject = "POTENTIAL THREAT IN BANK"
                              body = "XXXXXX ALERT XXXXXX\
                                \n\nIndividual in bank for two hours .\
                                \n\nPlease exercise caution. "
                              email_sender.send_email(subject, body,None)
                              time_danger=1
                              print("First cycle reached, danger score increased")
                              score=db_manager.get_score([int(id)])
                              score=score+time_danger
                              if(score>=10):
                                      score=10
                              new_info=[int(score),int(id)]
                              print("First cycle reached, danger score increased")
                              db_manager.update_threat(new_info)
                         SCORE=db_manager.get_score([int(id)])
                         if((SCORE>=6)and(not security)):
                              security=True
                              email_sender = EmailSender(sender_email, security_email, password)
                              subject = "POTENTIAL THREAT IN BANK"
                              body = "XXXXXX ALERT XXXXXX\
                                \n\nBE ALERT AS POSSIBLE THREAT IS IN BANK"
                              email_sender.send_email(subject, body,None)
                              print("Score 6, guards alerted")
                              #pass
                         # ALERT GUARDS
                         elif((SCORE>=9)and(not police)): 
                              police=True
                              email_sender = EmailSender(sender_email, police_email, password)
                              subject = "POTENTIAL THREAT IN BANK"
                              body = "XXXXXX ALERT XXXXXX\
                                \n\nAttention! CONTACT THE SCOTIABANK JUNCTION BRANCH IMMEDIATELY AND CONFIRM ORDER .\
                                \n\nSuspicious Individual Detected In Bank "
                              email_sender.send_email(subject, body,None)
                              print("Score 9, police alerted")



                    #b+=1

                '''
                for b2 in box2:
                    if item_scores_list[0]>0.5 and item_ID_list[0]==0:
                         #x_min2, y_min2, x_max2, y_max2 = box2[b2%len(box2)]
                             x_min2, y_min2, x_max2, y_max2 = box2[0]

                             x_min2, x_max2 = (int(x_min2*640), int(x_max2*640))
                             y_min2, y_max2 = (int(y_min2*480), int(y_max2*480))

                             x_min2 = x_min2 - int(x_max2/2)
                             y_min2 = y_min2 - int(y_max2/2)
                             x_max2 = x_min2 + x_max2
                             y_max2 = y_max2 + y_min2
                        
                             cv2.rectangle(frame_, (x_min2, y_min2), (x_max2,y_max2), (0,b*150,b*50), 3)
                             #b2+=1
                             b2=b2[1:]
                             item_scores_list=item_scores_list[1:]
                             item_ID_list=item_ID_list[1:]
                             euclidean_midpoints2+=[[int(x_min2+(x_max2-x_min2)/2) , int(y_min2+(y_max2-y_min2)/2)]]

                    else:
                         item_scores_list=item_scores_list[1:]
                         item_ID_list=item_ID_list[1:]
                                               
                         

                         
                         #b+=1

                         

                    #b+=1

                        
                         
                         
                         
                
                class_ = 0
                item_ID=[e for e in item_ID if e==0]
                for eu2 in euclidean_midpoints2:
                    euclidian_distances = []
                    for eu in euclidean_midpoints:
                        euclidian_distances += [abs(((eu2[0]-eu[0])/2 + (eu2[1]-eu[1])/2)**0.5)]
                    if euclidian_distances!=[]:
                         min_eu=min(euclidian_distances)
                    else:
                         min_eu = 999
                    if min_eu<14: 
                        cv2.rectangle(frame_, (eu2[0], eu2[1]), (eu[0], eu[1]), (50,200,50), 3)
                        e = 0
                        while euclidian_distances[e] != min_eu:
                            e +=1 
                        if ((clID[e] == 0) and (item_ID[class_] == 0) and (not gun)):
                            cv2.putText(frame_, "Handgun Detected", (euclidean_midpoints[e][0], euclidean_midpoints[e][0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 100), 2, cv2.LINE_AA, False)
                            gun=True
                            image=take_image(cv2,cap)
                            email_sender = EmailSender(sender_email, receiver_emails, password)
                            subject = "THREAT IN BANK"#SEND LOCATION
                            body = "XXXXXX ALERT XXXXXX\
                                \n\nARMED PERSON WITH GUN AT SCOTIABANK JUNCTION BRANCH\
                                \n\nAPPROACH WITH CAUTION "
                            email_sender.send_email(subject, body,image)
                            print("Image sent")
                    class_ += 1
                    
            except AttributeError as e:
                          print("Error:", e)
        else:
            print("tensor_ids is None. Cannot proceed.")
        

     
        out.write(frame_)
        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("Closed manually")
            #db_manager.close_connection()
            break
cap.release()
out.release()
cv2.destroyAllWindows()

