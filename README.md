# 541 final project

**Author:**

- Rongzhe Liu (rongzhel@usc.edu)
- Chenhua Fan (chenhuaf@usc.edu)

## Files

This repository is the main workspace of our final project. It includes:

- `*.ipynb` **Jupyter notebooks of model we used** (main work).
- `ASLDataset.py` the initialization of dataset.
- `/trained_models` the models we trained (Models **not included** in the zip file on the Canvas).
- `/CustomResNet18` the web application (demo with fully functional, model **not included** in the zip file on the Canvas).
  - `/backend` the backend files for `torchserve`.
  - `/frontend` the frontend React app.
- `541 final report.mp4` **the demo of our application. Welcome to [checkout](https://youtu.be/8BdOX08LUug)**.

## Models details

All models **not included** in the zip file **on the Canvas**. Additional upload required.

- `CustomResNet18` 42.8 MB, the main network we used in the application, Report section 4.
- `baselineModel_model.pth` 4.31 MB, Report section 3.1, A plain CNN.
- `efficientnet_b0_rwightman-3dd342df.pth` 20.5 MB, Report section 4.
- `inception_raw.pth` 96.4 MB, Report section 4.
- `mobilenet_v3_small-047dcff4.pth` 9.83 MB, Report section 4.

## Web application

![App](./app.png)

install required packages

```shell
pip install -r requirements.txt
```

`torchserve` must be installed. [quick start](https://github.com/pytorch/serve/blob/master/README.md#-quick-start-with-torchserve)

```shell
pip install torchserve torch-model-archiver torch-workflow-archiver
```

`Nginx` must be installed, and add the redirection rules to the configuration.

```
location ^~ / {
    proxy_pass http://localhost:3000/;
}

location ^~ /api/ {
    proxy_pass http://localhost:8080/;
}
```

Start the nginx

```shell
nginx
```

Run the application

```shell
git clone https://github.com/ChenhuaFan/541-Final-Project---Gesture-Recognition.git
cd 541-Final-Project---Gesture-Recognition/CustomResNet18/backend
# start the torchserve (torchserve must be installed)
torchserve --start --ncs --model-store model_store --models CustomResNet18.mar
# run the frontend (npm must be installed)
cd ../frontend
npm i
npm start
```

Visit `http://localhost:port` (Nginx listen port, default is 8080).

to stop torch serve

```shell
torchserve --stop
```

Can't run the torchserve? check the log files!
`CustomResNet18/backend/logs/model_log.log`
