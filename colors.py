class Color:
    def __init__(self, red, green, blue):
        if red > 255 or green > 255 or blue > 255: raise Exception('Color values bigger then 255')
        self.red = red
        self.green = green
        self.blue = blue

red = Color(255, 0, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)
white = Color(255, 255, 255)
black = Color(0, 0, 0)
