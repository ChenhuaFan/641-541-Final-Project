"""
Module for image classification default handler
"""
from torchvision import transforms
from ts.torch_handler.image_classifier import ImageClassifier


class ImageClassifier(ImageClassifier):

    image_processing = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((224, 224)),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    def preprocess(self, data):
        return super().preprocess(data)