from mlflow import MlflowClient
import mlflow
import torch

model_G1 = torch.load('checkpoints/ST-CGAN_G1_1260.pth',
                      map_location=torch.device('cpu'))
model_G2 = torch.load('checkpoints/ST-CGAN_G2_1260.pth',
                      map_location=torch.device('cpu'))

mlflow.pytorch.log_model(
    pytorch_model=model_G1, artifact_path='gan', registered_model_name='g1')
mlflow.pytorch.log_model(
    pytorch_model=model_G1, artifact_path='gan', registered_model_name='g2')

# client = MlflowClient()
# client.create_registered_model("sk-learn-random-forest-reg-model")
