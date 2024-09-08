from ultralytics import YOLO
import cv2
from datetime import datetime
from email.mime.image import MIMEImage
import time
from send_email import EmailSender
from local_sql import CaptureDatabase

sender_email = "sici3902@gmail.com"
password = "euck qnjq kobv isro"  
police=False
security=False
gun=False
knife=False
notify_count=0
police_email="robinsond993@gmail.com"
security_email="robinsond993@gmail.com"



danger_zone = [116, 165, 600, 479 ]#NEED TO FIX DANGER ZONE

#FUNCTION TO DETERMINE DANGER ZONE
def CompLoc(list1, list2):
    for x in range(4):
        if abs(list1[x] - list2[x]) > 75:
            return False
    return True

def take_image(cv2,cap):
     cv2.imwrite("Suspect_image.jpg",frame_)
     #cap.release()
     with open("Suspect_image.jpg","rb") as img:
          image_data=img.read()
     image=MIMEImage(image_data,name="Suspect_image.jpg")
     return image

db_manager =  CaptureDatabase(host="localhost", user="root", password="damc18", database="Capture")
db_manager.empty_table()
lst=[]
location_danger=0
# load yolov8 model
model = YOLO('yolov8n.pt')
model2 = YOLO('last.pt')

# load video
video_path = './test.mp4'
cap = cv2.VideoCapture(0)

ret = True
# read frames
while ret:
    ret, frame_ = cap.read()

    if ret:

        
        results = model.track(frame_, persist=True,tracker="bytetrack.yaml")
        results2 = model2.track(frame_,persist=True,tracker="bytetrack.yaml")
        
        #frame_ = results[0].plot()
        info = results[0]

        
        cv2.rectangle(frame_, (116, 165), (600,479), (0,100,300), 3)#MIN X MIN Y MAX X MAX Y
        cv2.putText(frame_, "Danger Zone", (160, 124), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        
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
                count_area=0
                for id in numpy_ids:
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
                         id_list=db_manager.get_ids()
                         if(id not in id_list):
                             new_info=[int(id),0,0,False]#fix_time
                             db_manager.insert_info(new_info)
                         elif(CompLoc(co_ordinates,danger_zone)):
                             count_area+=1
                             zone_test=False
                             location_danger=1
                             if(count_area<=3):
                                  score=db_manager.get_score([int(id)])#Here
                                  score=score+location_danger
                                  if(score>=10):
                                       score=10
                                       new_info=[int(score),int(id)]
                                       db_manager.update_threat(new_info)
                         if((not zone_test)and(notify_count==0)):
                              notify_count=1
                              email_sender = EmailSender(sender_email, security_email, password)
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
                              email_sender = EmailSender(sender_email, security_email, password)
                              subject = "POTENTIAL THREAT IN BANK"
                              body = "XXXXXX ALERT XXXXXX\
                                \n\nIndividual in bank for four hours .\
                                \n\nIt is advised to approach individual "
                              email_sender.send_email(subject, body,None)
                              time_danger=1
                              score=db_manager.get_score([int(id)])
                              score=score+time_danger
                              if(score>=10):
                                      score=10
                              new_info=[int(score),int(id)]
                              print("Second cycle reached, danger score increased")
                              db_manager.update_threat(new_info)
                         elif((time_cycle==100)):#SEND LOCATION INFORMATION
                              email_sender = EmailSender(sender_email, security_email, password)
                              subject = "POTENTIAL THREAT IN BANK"
                              body = "XXXXXX ALERT XXXXXX\
                                \n\nIndividual in bank for two hours .\
                                \n\nPlease exercise caution. "
                              email_sender.send_email(subject, body,None)
                              time_danger=1
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



                    b+=1


                for b2 in box2:
                    if item_scores_list[0]>0.65 and item_ID_list[0]==0:
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
                            gun=True
                            image=take_image(cv2,cap)
                            email_sender = EmailSender(sender_email, police_email, password)
                            subject = "THREAT IN BANK"#SEND LOCATION
                            body = "XXXXXX ALERT XXXXXX\
                                \n\nARMED PERSON WITH GUN AT SCOTIABANK JUNCTION BRANCH\
                                \n\nAPPROACH WITH CAUTION "
                            email_sender.send_email(subject, body,image)
                            print("Image sent")
                            
                            
                        if (clID[e] == 0 and item_ID[class_] == 1 and (not knife)):
                            #print("Person owns Knife")#SEND LOCATION
                            knife = True
                            """image=take_image(cv2,cap)
                            email_sender = EmailSender(sender_email, police_email, password)
                            subject = "THREAT IN BANK"
                            body = "XXXXXX ALERT XXXXXX\
                                \n\nARMED PERSON IS AT SCOTIABANK JUNCTION BRANCH\
                                \n\nAPPROACH WITH CAUTION "
                            email_sender.send_email(subject, body,image)"""
                    class_ += 1
                    
            except AttributeError as e:
                          print("Error:", e)
        else:
            print("tensor_ids is None. Cannot proceed.")
        

     
        
        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("Closed manually")
            db_manager.close_connection()
            break
cap.release()
cv2.destroyAllWindows()

