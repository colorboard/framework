class Button:
    def __init__(self, id):
        self.id = id

right = Button(0)
left = Button(1)
up = Button(2)
down = Button(3)
action = Button(4)

def pressed_buttons() -> list:
    from bridge import get_pressed_buttons
    
    pressed_buttons = []
    for button in get_pressed_buttons():
        if button == 0: pressed_buttons.append(right)
        elif button == 1: pressed_buttons.append(left)
        elif button == 2: pressed_buttons.append(up)
        elif button == 3: pressed_buttons.append(down)
        elif button == 4: pressed_buttons.append(action)

    return pressed_buttons