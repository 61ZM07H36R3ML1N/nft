from email.mime import image
import os
import random
from typing import List
from PIL import Image 
from layer import Layer


class AvatarGenerator:
    def __init__(self, images_path: str):
        self.layers: List[Layer] = self.load_image_layers(images_path)
        self.background_color = (235, 64, 52)
    
    def load_image_layers(self, images_path: str):
        sub_paths = sorted(os.listdir(images_path))
        print(sub_paths)
        layers = []
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            layer = Layer(layer_path)
            layers.append(layer)
        return layers 
    
    def generate_image_sequence(self):
        image_path_sequence =[]
        for layer in self.layers:
            image_path = layer.get_random_image_path
            image_path_sequence.append(image_path)
            
        return image_path_sequence
    
    def render_avatar_image(self, image_path_sequence: List[str]):
      image = Image.new("RGBA" (124, 231), self.background_color)
      return image
    
    def generate_avatar(self):
        image_path_sequence = self.generate_image_sequence