class Color:
    NoColor = -1
    White = 0
    Black = 1
    Red = 2
    Green = 3
    Blue = 4

    def colorValue(self, color):

        if color == 0:
            return "#FFFFFF"
        elif color == 1:
            return "#000000"
        elif color == 2:
            return "#FF0000"
        elif color == 3:
            return "#00FF00"
        elif color == 4:
            return "#0000FF"
        else:
            return ""

class ColorType:
    def allColorPattern(self):
        return {Color.White, Color.Black, Color.Red, Color.Green, Color.Blue}