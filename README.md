# FintuneConvTransCV
This repository includes code and documentation for fine-tuning models on new datasets and evaluating model performance.

## Environment
To set up the environment, run the following command in the terminal:

```bash
python -m venv finetuneconv_env
source ./finetuneconv_env/bin/activate
pip install -r requirement.txt
```

## Downloading the Dataset
To download the dataset, please visit https://drive.google.com/file/d/1jjuI7Me9VFhpMHp2QP5gHKU5NPkzCQZk/view?usp=sharing, and follow the commands below.
```bash
gdown https://drive.google.com/uc?id=1jjuI7Me9VFhpMHp2QP5gHKU5NPkzCQZk
unzip hw1_data.zip -d ./datasets
cd datasets
mkdir images labels labels/train labels/valid
mv -r ./hw1_dataset/test ./hw1_dataset/train ./hw1_dataset/valid images
rm -r hw1_dataset
python3 transfer.py
```

## Modify yaml file
modify train and val path to absolute path in your computer.

## Running YOLO
To run YOLO, please follow the instructions below.
```bash
cd yolo
python3 train.py
```
The results will stored in the 'run' folder

