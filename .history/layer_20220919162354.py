from importlib.resources import path
import os
import random


class Layer:
    
    def __init__(self, assets_path: str):
        self.path = path
        
    def get_random_assets_path(self, assets_path: str):
        assets_path = os.listdir(self.path)
        random_assets_path = random.choice(assets_path)
        return os.path.join(self.path, random_assets_path)
        
        