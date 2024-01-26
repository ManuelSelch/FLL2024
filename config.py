import yaml

class Length:
    min: int
    max: int
    
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max
    
class Canvas:
    width: int
    height: int
    border: int
    
    def __init__(self, width: int, height: int, border: int):
        self.width = width
        self.height = height
        self.border = border
        
class Colors:
    showDefault: bool
    default: str
    dic: [int, str]
    
    def __init__(self, showDefault: bool, default: str, dict: [int, str]):
        self.showDefault = showDefault
        self.default = default
        self.dict = dict
    
class Config:
    key: str
    length: Length
    canvas: Canvas
    camera_source: int
    colors: Colors
    
    def __init__(self):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
            self.key = config["key"]
            self.length = Length(
                min=config["length"]["min"],
                max=config["length"]["max"]
            )
            self.canvas = Canvas(
                width = config["canvas"]["width"],
                height = config["canvas"]["height"],
                border = config["canvas"]["border"]
            )
            self.camera_source = config["camera_source"]
            self.colors = Colors(
                showDefault = config["colors"]["showDefault"],
                default = config["colors"]["default"],
                dict=config["colors"]["dict"]
            )
            
    
    

