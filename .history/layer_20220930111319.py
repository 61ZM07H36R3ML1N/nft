import os
import random

class Layer:
    def __init__(self, path: str):
        self.path = path
    
    def get_random_image_path(self):
        image_file_names = os.listdir(self.path)
        print(image_file_names)