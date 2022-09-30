import os

class AvatarGenerator: 
    def __init__(self, images_path: str):
        self.layers = self.load_image_layers(images_path)
        pass
    
    def load_image_layers(self, images_path: str):
        sub_paths = sorted(os.listdir(images_path))
        print(sub_paths)
        layers = []
        return layers
        
    
    def generate_avatar(self):
        print("AvatarGenerator: Generating Avatar!")