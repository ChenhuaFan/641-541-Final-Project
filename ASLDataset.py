from torch.utils.data import Dataset
import os
from torchvision.io import read_image
from matplotlib.image import imread
import random

class ASLDataset(Dataset):
    
    def __init__(self, set_type, preprocess=False, transform=None, size_per_class=2075, target_transform=None, local_classes=None, scource=True): # 3000 target_transform=None,  classes=[], ranges=None, 
 
        self.preprocess = preprocess
        self.transform = transform
        self.target_transform = target_transform
        
        self.paths  = []
        self.categories = []
        self.scource = scource
        
        # custom_classes: bool = len(classes) != 29

        # print(classes)
        classes = local_classes if local_classes != None else ([chr(x) for x in range(ord('A'),ord('Z')+1)] + ['del', 'nothing','space']) # if custom_classes == False else classes

        start_range = 1
        end_range = 1
        # if custom_classes:
        #     for idx, cat in enumerate(classes):
        #         print(idx, cat)
        #         start_range = ranges[idx][0]
        #         end_range = ranges[idx][1]
        #         img_file_prefix = 'shadow_removal_image_' if preprocess else ''
        #         self.paths.extend([f'{cat}/{img_file_prefix}{cat}{n}.jpg' for n in range(start_range, end_range)])
        #         self.categories.extend([(ord(cat) - ord('A')) for j in range(end_range-start_range)])
        # else:
        if set_type == 'train':
            end_range = int(size_per_class * 0.85)
        elif set_type == 'test':
            start_range = int(size_per_class * 0.85)
            end_range = size_per_class + 1
        prefix = 'shadow_removal_image_' if scource else ''
        # random
        ran = random.randint(0, 100)
        random.seed(ran)
        if local_classes != None:
            a_ord = ord('A')
            labels = [(ord(c) - a_ord) for c in local_classes]
            for idx, cat in enumerate(classes):
                self.paths.extend([f'{cat}/{prefix}{cat}{n}.jpg' for n in range(start_range, end_range)])
                self.categories.extend([labels[idx] for j in range(end_range-start_range)])
        else:
            for idx, cat in enumerate(classes):
                self.paths.extend([f'{cat}/{prefix}{cat}{n}.jpg' for n in range(start_range, end_range)])
                self.categories.extend([idx for j in range(end_range-start_range)])
            
            
    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        
        img_path = './imgs_outputs/' if self.scource else './asl_alphabet_train/asl_alphabet_train/asl_alphabet_train/' # if self.preprocess else './imgs_outputs/' # './asl_alphabet_train/asl_alphabet_train/asl_alphabet_train/' 
        
        img_path = os.path.join(img_path, self.paths[idx])
        image = imread(img_path)
        label = self.categories[idx]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
