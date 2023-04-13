# FintuneConvTransCV
This repository includes code and documentation for fine-tuning models on new datasets and evaluating model performance.

## Environment
To set up the environment, run the following command in the terminal:

```bash
pip install -r requirements.txt
```

## Downloading the Dataset
To download the dataset, please visit 'https://drive.google.com/file/d/1jjuI7Me9VFhpMHp2QP5gHKU5NPkzCQZk/view?usp=sharing', and follow the commands below.
```bash
unzip hw1_dataset -d ./datasets
cd datasets
mkdir images labels labels/train labels/valid
mv -r test train valid images
python3 transfer.py
```

## Running YOLO
To run YOLO, please follow the instructions below.
```bash
cd yolo
python3 yolo
```
The results will stored in the 'run' folder

