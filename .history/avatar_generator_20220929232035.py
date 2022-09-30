import os
import random
from typing import List
from PIL import Image
from layer import Layer

class AvatarGenerator:
    def __init__(self, assets_path: str):
        self.layers : List[Layer] = self.load_assets_layers(assets_path)
        self.background_color =(120, 150, 180)
        self.output_path: str = "./output"
        os.makedirs(self.output_path, exist_ok=True)
    
    def load_assets_layers(self, assets_path: str):
        sub_paths = sorted(os.listdir(assets_path))
        layers = []
        for sub_path in sub_paths:
            assets_path = os.path.join(assets_path, sub_path)
            layer = Layer(assets_path)
            layers.append(layer)
        return layers
    
    def generate_assets_sequence(self):
        assets_path_sequence = []
        for layer in self.layers:
            assets_path = layer.get_random_assets_path(Image)
            assets_path_sequence.append(assets_path)
            
        return assets_path_sequence
    
    def render_avatar_image(self, assets_path_sequence: List[str]):
        image = Image.new("RGBA", (124, 231), self.background_color)
        for image_path in assets_path_sequence:
            layer_image = Image.open(image_path)
            image = Image.alpha_composite(image, layer_image)
            return image
    
    def save_image(self, image: Image.Image):
        image_file_name = "Pixeltar.png"
        image_save_path = os.path.join(self.output_path, image_file_name)
        image.save(image_save_path)
        
    def generate_avatar(self):
        print("AvatarGenerator: Generating Avatar!, Please Wait")
        assets_path_sequence = self.generate_assets_sequence()
        image = self.render_avatar_image(assets_path_sequence)
        self.save_image(image)