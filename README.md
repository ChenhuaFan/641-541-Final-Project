# 641 Final project

**Author:**

- Bhumi Godiwala (godiwala@usc.edu)
- Chenhua Fan (chenhuaf@usc.edu)
- Qiwei Chen (qiweic@usc.edu)

## Quick Start

install the `requirements.txt` by pip, then go through the `*.ipynb`.

Or using mlflow to start mlops UI. `mlflow server --backend-store-uri sqlite:///641.db --host 0.0.0.0 --port 5000` SQLite required.

## Files

All necessary files can accesse at the [google drive](https://drive.google.com/drive/u/1/folders/1fRewkkPJ_-huQXFKB7dzuzB_cuPkU5oF).

This repository is the main workspace of our final project. It includes:

- `/GAN` is the main GAN model we used and trained.
- `*.ipynb` **Jupyter notebooks of model we used** (main work).
- `ASLDataset.py` the initialization of dataset.
- `/trained_models` the models we trained (Models **not included** in the zip file on the Canvas).
- `/imgs_outputs` is the images generated from GAN.

## Models details

All models **not included** in the zip file **on the Canvas**. Additional upload required.

- `model` ResNet model.
- `ST-CGAN_G1_1260.pth` GAN model. 111.6MB
- `ST-CGAN_G2_1260.pth` GAN model. 111.6MB

## MLOPS

the mlops based on `mlflow`. data stored in the 641.db (sqlite)
