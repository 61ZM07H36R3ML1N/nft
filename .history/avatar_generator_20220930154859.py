from email.mime import image
import os
import random
from typing import List
from PIL import Image
from layer import Layer 

class AvatarGenerator: 
    def __init__(self, images_path: str):
        """
        This function takes in a path to a file containing a list of images and returns a list of layers
        
        :param images_path: The path to the file containing the image data
        :type images_path: str
        """
        self.layers: List[Layer] = self.load_image_layers(images_path)
        self.background_color = (50, 168, 82)
    
    def load_image_layers(self, images_path: str):
        """
        It takes a path to a directory of images, and returns a list of Layer objects, where each Layer
        object is a single image
        
        :param images_path: The path to the directory containing the images
        :type images_path: str
        :return: A list of Layer objects.
        """
        sub_paths = sorted(os.listdir(images_path))
        layers = []
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            layer = Layer(layer_path)
            layers.append(layer)
        return layers
        
        
    def generate_image_sequence(self):
        """
        It returns a list of image paths, where each image path is randomly selected from a different
        layer.
        :return: A list of image paths.
        """
        image_path_sequence = []
        for layer in self.layers:
                image_path = layer.get_random_image_path()
                image_path_sequence.append(image_path)
    
        return image_path_sequence
    
    def render_avatar_image(self, image_path_sequence: List[str]):
       image = Image.new("RGBA", (124, 231), self.background_color)
       return image  
    
    def generate_avatar(self):
       print("AvatarGenerator: Generating Avatar!")
       image_path_sequence = self.generate_image_sequence