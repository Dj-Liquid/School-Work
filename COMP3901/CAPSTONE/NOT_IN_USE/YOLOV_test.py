from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
#model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
#model.train(data="config.yaml", epochs=1)  # train the model
#metrics = model.val()  # evaluate model performance on the validation set
#results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
#path = model.export(format="onnx")  # export the model to ONNX format


'''
Load a YOLO model from a specified YAML configuration file.
Args:
    "yolov8n.yaml" (str): The path to the YAML configuration file for the YOLO model.
Returns:
    model: An instance of the YOLO model loaded with the specified configuration.
'''
model = YOLO("yolov8n.yaml")


'''
Print the contents of the loaded dataset configuration file for debugging purposes.
Args:
    "config.yaml" (str): The path to the configuration file to be read.
Outputs:
    None. Prints the configuration data to the console.
'''
with open("config.yaml", "r") as config_file:
    config_data = config_file.read()
print("Loaded Dataset Configuration:")
print(config_data)


'''
Train the YOLO model using the specified configuration and for a specified number of epochs.
Args:
    data (str): The path to the YAML configuration file containing training data specifications.
    epochs (int): The number of epochs (training iterations) to run during training.
Returns:
    None.
'''
model.train(data="config.yaml", epochs=150)

