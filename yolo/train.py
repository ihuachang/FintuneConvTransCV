from ultralytics import YOLO

yaml_loc = "../datasets/datasets.yaml"

# Load a model
model = YOLO('yolov8x.pt')  # load a pretrained model (recommended for training)

# # Use the model
results = model.train(data=yaml_loc, epochs=500, batch=30, seed=323, lrf=1e-4, lr0=5e-2, warmup_epochs = 10)  # train the model
results = model.val()  # evaluate model performance on the validation set
