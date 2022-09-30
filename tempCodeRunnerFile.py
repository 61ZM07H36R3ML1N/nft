import os

class AvatarGenerator:
    def __init__(self, assets_path: str):
        self.layers = self.load_assets_layers(assets_path)
    
    def load_assets_layers(self, assets_path: str):
        sub_paths = os.listdir(assets_path)
        print(sub_paths)
        layers = []
        return layers
        
    
    def generate_avatar(self):
        print("AvatarGenerator: Generating Avatar!, Please Wait")