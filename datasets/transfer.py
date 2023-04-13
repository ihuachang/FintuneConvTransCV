import json

dataset = "train"
annotation = f"./annotations/instances_{dataset}.json"
# Load the COCO annotations
with open(annotation, 'r') as f:
    coco_annotations = json.load(f)

# Load the label names
label_names = [cat['name'] for cat in coco_annotations['categories']]

# Convert the annotations to YOLO format
for img in coco_annotations['images']:
    yolo_labels = []
    for ann in coco_annotations['annotations']:
        if ann['image_id'] == img['id']:
            label_id = ann['category_id']
            x_center = (ann['bbox'][0] + ann['bbox'][2]/2) / (img['width'])
            y_center = (ann['bbox'][1] + ann['bbox'][3]/2) / (img['height'])
            width = (ann['bbox'][2]) / img['width']
            height = (ann['bbox'][3]) / img['height']
            yolo_labels.append(f"{label_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    with open(f"./labels/{dataset}/{img['file_name'][:-4]}.txt", 'w') as f:
        f.write('\n'.join(yolo_labels))
