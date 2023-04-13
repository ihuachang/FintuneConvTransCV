from ultralytics import YOLO
import json

model_dir = ""
pred_dir = ""

model = YOLO(model_dir)
results = model.predict(pred_dir)

dic = {}
for result in results:
    dic[result.path.split('/')[-1]]={
        "boxes":result.boxes.xyxy.tolist(),
        "labels":[int(label) for label in result.boxes.cls.tolist()],
        "scores":result.boxes.conf.tolist()
    }

with open('output.json', 'w') as f:
    json.dump(dic, f)