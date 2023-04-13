from ultralytics import YOLO

yaml_loc = "../datasets/datasets.yaml"

# Load a model
model = YOLO('yolov8x.pt')  # load a pretrained model (recommended for training)

# # Use the model
results = model.train(data=yaml_loc, epochs=200, batch=16, save_period=5)  # train the model
results = model.val()  # evaluate model performance on the validation set
