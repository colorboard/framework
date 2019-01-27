## Structure

The default code structure looks like this:

```python
from matrix import *

def setup():
  pass
  
def frame():
  pass
```

The `setup` function will called only on application starting.  
And the `frame` function will calls every frame. By default it's 15 calls per second.

## Colors

We have `colors.Color` class. Using it you can generate color you want.  
Every color has three intager values (from 0 to 255):

- red
- green
- blue

The constructor of this class looks like this `colors.Color(red, green, blue)`.  

Like this:

```python
my_color = colors.Color(red=255, green=255, blue=0)

my_color.green
# 255

my_color.blue
# 0
```

You can use your own colors like for setting pixels using it.

Also `colors` module has pre-created colors:

```python
colors.red # red color
colors.green # green color
colors.blue # blue color
colors.white # white color
colors.black # black color
```

## Buttons

We have five buttons objects:

```python
buttons.right # right button
buttons.left # left button
buttons.up # up button
buttons.down # down button
buttons.action # action button (a)
```

If you need to get list of currently pressed buttons, you can call the `buttons.pressed_buttons()` function. It will return the `list` with the buttons objects.

```python
pressed = buttons.pressed_buttons() # list with the pressed buttons objects
```

And if you need to do action when specific button is pressed, you can use this construction:

```python
for btn in pressed:
  if btn == buttons.right:
    print('Right is the better way for us.')
  elif btn == buttons.left:
    print('We need to go left!')
```

## Pixels

You can set the pixel color using `put_pixel(x, y, color)` function.

```python
put_pixel(x=0, y=0, color=colors.red) # setting first pixel color to red
```

Also, you can fill all screen using `fill(color)` function.

```python
fill(color=colors.green) # filling all screen pixels color to green
```

You can get current pixel color using `get_pixel(x, y)` function.  
It will return the `colors.Color` object.

```python
pixel_color = get_pixel(x=0, y=0) # getting first pixel color object
print(pixel_color.green) # printing green value from rgb
```

**this function is not supported yet**
