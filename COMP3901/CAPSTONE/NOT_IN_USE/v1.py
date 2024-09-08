from ultralytics import YOLO
import cv2
from datetime import datetime
from torch import IntTensor
from pymongo import MongoClient
from python_sql import connect_to_database

connect_to_database

uri = "mongodb+srv://SICI_ADMIN:JykKRTankchklZhJ@cluster0.nputgqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri) #Client Initiallize


db = client.SICI_DATA #database creation/selection if exists
cvdb = db.Records #collection creation/selection if exists

lst=[]
# load yolov8 model
model = YOLO('yolov8n.pt')

# load video
video_path = './test.mp4'
cap = cv2.VideoCapture(0)

ret = True
# read frames
while ret:
    ret, frame = cap.read()

    if ret:

        # detect objects
        # track objects
        results = model.track(frame, persist=True,tracker="bytetrack.yaml")
        

        # plot results
        # cv2.rectangle.(frame_
        # cv2.putText
        frame_ = results[0].plot()
        info = results[0]
        
        box = results[0].boxes.xywhn  # Assuming you want the first detected object
        clID = results[0].boxes.cls
        #print("clID",clID)
        #print("name",results[0].names[int(clID)])
        
        #cvdb.insert_one({"Info": {info}, "BBoxes": {box}})

# Extract individual coordinates
        #x_min, y_min, x_max, y_max = box

# Print the coordinates
        #print("Bounding box coordinates:")
        #print("BOX:", box)
        
        


        tensor_ids = info.boxes.id  # Example tensor

        
        #print(f"INFO!!:{tensor_ids}")

        # Convert tensor to NumPy array
        if tensor_ids is not None:
            try:
                numpy_ids = tensor_ids.numpy()
                li, lb, lID = [],[],[]
                #print(f"INFO!!:{numpy_ids}")
                # Extract individual IDs and boxes
                b = 0
                for id in numpy_ids:
                    #box = result.boxes.xywhn
                    #numpy_boxes = box.numpy()#co-ordinates
                    #print("BOX:", numpy_boxes)
                    x_min, y_min, x_max, y_max = [int(s*200) for s in box[b]]#extract box vaues and convert them to usable int numbers
                    #print("TBox",str(box[b]))
                    b+=1
                    #print("Thing is ", results[0].plot()) #Stores item's nameresults[0].names[results[0].id]
                    #create the second coords 
                    x_max = x_min + x_max
                    y_max = y_max + y_min
                    #print("ID:", id)
                    current_time = datetime.now().strftime("%H:%M:%S")
                    lst=(id,"has an object",current_time)
                    #print("INFO:", lst)
                    cv2.rectangle(frame_, (x_min, y_min), (x_max,y_max), (0,0,0), 1)
                    li+=[[x_min, y_min, x_max, y_max]]
                    lb+=[[(x_max-x_min)/2, (y_max-y_min)/2]]
                    cvdb.insert_one({"ID": int(id), "Car_ID": "", "Score": "", "Critical": "No", "Threat": "No", "Time": current_time,"V_Coordinates": [x_min, y_min, x_max, y_max]})
               
                n=0
                for l in lb: #finds if objects are close together
                    seen=[]
                    xl, yl, xl1, yl1 = 0,0,0,0
                    nb = -1
                    for l2 in lb:
                        if l2 != l:
                            xl, yl, xl1, yl1 =  l[0],l[1],l2[0],l2[1] #Euclidian Line
                        nb+=1
                    #""""""makes a frame around the ownership
                    al = abs(((xl1-xl)/2 + (yl1-yl)/2)**0.5)#Eucledian Distance between each item
                    
                    #frames Items if close enough together
                    if al < 8 and al not in seen:
                        seen += [al]
                        xm3, ym3, xm4, ym4 = min(li[n][0],li[nb][0]),min(li[n][1],li[nb][1]),max(li[n][2],li[nb][2]),max(li[n][3],li[nb][3])
                        cv2.rectangle(frame_, (xm3,ym3), (xm4,ym4), (200,0,0), 3)
                        #print("someone has something")
                    #print("Eu: ", al)
                    n+=1
                    
            except AttributeError as e:
                          print("Error:", e)
        else:
            print("tensor_ids is None. Cannot proceed.")
        

        """
        for info in results:
            print(f"INFO!!:{info.boxes.id}")

            temp_id=info.boxes.id
            # Convert tensor to NumPy array
            numpy_ids = temp_id.numpy()

            # Extract individual IDs
            for id in numpy_ids:
                print("ID:", id)
                """

        # visualize
        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
# release the capture
cap.release()
cv2.destroyAllWindows()

def calculate_score(id,points):
     return 0
