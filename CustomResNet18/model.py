from torchvision.models.resnet import ResNet, BasicBlock
import torch.nn as nn


class CustomResNet18(ResNet):
    def __init__(self):
        super(CustomResNet18, self).__init__(BasicBlock, [2, 2, 2, 2])
        num_ftrs = self.fc.in_features
        self.fc = nn.Linear(num_ftrs, 29)
