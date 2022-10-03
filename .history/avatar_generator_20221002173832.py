import os
import random
from typing import List
from PIL import Image 
from layer import Layer


class AvatarGenerator:
    def __init__(self, images_path: str):
        self.layers: List[Layer] = self.load_image_layers(images_path)
        pass
    
    def load_image_layers(self, images_path: str):
        sub_paths = sorted(os.listdir(images_path))
        print(sub_paths)
        layers = []
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            layer = Layer(layer_path)
            layers.append(layer)
        return layers 
    
    def generate_avatar(self):
        image_path_sequence =[]
        for layer in self.layers:
            image_path = layer.get_random_image_path
            image_path_sequence.append(image_path)
            
        print (image_path_sequence)    