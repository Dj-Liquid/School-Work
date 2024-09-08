from ultralytics import YOLO
import cv2
from datetime import datetime
from local_sql import CaptureDatabase
from send_email import EmailSender

sender_email = "sici3902@gmail.com"
password = "euck qnjq kobv isro"
police = False
security = False
notify_count = 0
police_email = "robinsond993@gmail.com"
security_email = "robinsond993@gmail.com"

danger_zone = [116, 165, 600, 479]  # NEED TO FIX DANGER ZONE

db_manager = CaptureDatabase(host="localhost", user="robin", password="password123", database="Capture")
db_manager.empty_table()
lst = []
location_danger = 0

model = YOLO('yolov8n.pt')
model2 = YOLO('last.pt')

video_path = './test.mp4'
cap = cv2.VideoCapture(0)

ret = True

def CompLoc(list1, list2):#RETURNS TRUE IF IN DANGER ZONE
    for x in range(4):
        if abs(list1[x] - list2[x]) > 75:
            return False
    return True

while ret:
    ret, frame = cap.read()

    if ret:
        results = model.track(frame, persist=True, tracker="bytetrack.yaml")
        results2 = model2.track(frame, persist=True, tracker="bytetrack.yaml")

        frame_ = results[0].plot()
        info = results[0]

        cv2.rectangle(frame_, (116, 165), (600, 479), (0, 100, 300), 3)
        cv2.putText(frame_, "Danger Zone", (160, 124), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

        box = results[0].boxes.xywhn
        box2 = results2[0].boxes.xywhn
        clID = results[0].boxes.cls

        tensor_ids = info.boxes.id
        coordinates_to_check = [
            [160, 134, 231, 264],
            [160, 134, 231, 264],
            [160, 134, 232, 264]
        ]

        if tensor_ids is not None:
            numpy_ids = tensor_ids.numpy()
            euclidean_midpoints, euclidean_midpoints2 = [], []
            b, b2 = 0, 0

            for id in numpy_ids:
                if clID[b] == 0:
                    zone_test = True

                    x_min, y_min, x_max, y_max = box[b]
                    x_min, x_max = (int(x_min * 640), int(x_max * 640))
                    y_min, y_max = (int(y_min * 480), int(y_max * 480))

                    x_min = x_min - int(x_max / 2)
                    y_min = y_min - int(y_max / 2)
                    x_max = x_min + x_max
                    y_max = y_max + y_min

                    current_time = datetime.now().strftime("%H:%M:%S")
                    lst = (id, "has an object", current_time)
                    cv2.rectangle(frame_, (x_min, y_min), (x_max, y_max), (b * 150, b * 50, 0), 3)

                    if len(box2) > 0:
                        x_min2, y_min2, x_max2, y_max2 = box2[b2 % len(box2)]
                        x_min2, x_max2 = (int(x_min2 * 640), int(x_max2 * 640))
                        y_min2, y_max2 = (int(y_min2 * 480), int(y_max2 * 480))

                        x_min2 = x_min2 - int(x_max2 / 2)
                        y_min2 = y_min2 - int(y_max2 / 2)
                        x_max2 = x_min2 + x_max2
                        y_max2 = y_max2 + y_min2

                        cv2.rectangle(frame_, (x_min2, y_min2), (x_max2, y_max2), (0, b * 150, b * 50), 3)
                        b2 += 1

                        euclidean_midpoints2 += [[int(x_min2 + (x_max2 - x_min2) / 2), int(y_min2 + (y_max2 - y_min2) / 2)]]

                    euclidean_midpoints += [[int(x_min + (x_max - x_min) / 2), int(y_min + (y_max - y_min) / 2)]]
                    b += 1

                    co_ordinates = [x_min, y_min, x_max, y_max]
                    print(co_ordinates)

                    id_list = db_manager.get_ids()
                    if id not in id_list:
                        new_info = [int(id), 0, 0, False]
                        db_manager.insert_info(new_info)
                    elif CompLoc(co_ordinates, danger_zone):
                        zone_test = False
                        location_danger = 1
                        score = db_manager.get_score([int(id)])
                        score = score + location_danger
                        if score >= 10:
                            score = 10
                        new_info = [int(score), int(id)]
                        print("Danger Updated")
                        db_manager.update_threat(new_info)

                    if (not zone_test) and (notify_count == 0):
                        count = 1
                        email_sender = EmailSender(sender_email, security_email, password)
                        subject = "POTENTIAL THREAT IN BANK"
                        body = "XXXXXX ALERT XXXXXX\
                                \n\nPERSON IN RESTRICTED AREA .\
                                \n\nSEARCH AND APPREHEND "
                        email_sender.send_email(subject, body)

                    time_cycle = db_manager.get_time([int(id)])
                    time_cycle += 1
                    time_info = [int(time_cycle), int(id)]
                    print(time_cycle)
                    db_manager.update_time(time_info)

                    if time_cycle >= 201:
                        pass
                    elif time_cycle == 200:
                        time_danger = 1
                        score = db_manager.get_score([int(id)])
                        score = score + time_danger
                        if score >= 10:
                            score = 10
                        new_info = [int(score), int(id)]
                        print("Danger Updated")
                        db_manager.update_threat(new_info)
                    elif time_cycle == 100:
                        time_danger = 1
                        score = db_manager.get_score([int(id)])
                        score = score + time_danger
                        if score >= 10:
                            score = 10
                        new_info = [int(score), int(id)]
                        print("Danger Updated")
                        db_manager.update_threat(new_info)

                    SCORE = db_manager.get_score([int(id)])
                    if SCORE >= 6 and (not security):
                        security = True
                        email_sender = EmailSender(sender_email, security_email, password)
                        subject = "POTENTIAL THREAT IN BANK"
                        body = "XXXXXX ALERT XXXXXX\
                                \n\nBE WARY AS POSSIBLE THREAT IS IN BANK"
                        email_sender.send_email(subject, body)
                    elif SCORE >= 9 and (not police):
                        police = True
                        email_sender = EmailSender(sender_email, police_email, password)
                        subject = "POTENTIAL THREAT IN BANK"
                        body = "XXXXXX ALERT XXXXXX\
                                \n\nAttention! CONTACT THE SCOTIABANK JUNCTION BRANCH IMMEDIATELY AND CONFIRM ORDER .\
                                \n\nSuspicious Individual Detected In Bank "
                        email_sender.send_email(subject, body)
                b += 1

    cv2.imshow('frame', frame_)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        db_manager.close_connection()
        break

cap.release()
cv2.destroyAllWindows()
