from pynput.mouse import Listener
#import logging
import server_classm
import imp

#ALL MESSAGES FORMAT
"""
Mouse_moved
Mouse_pressed
Mouse_scroll
KEY_PRESSED

"""


server = server_classm.Server()
print(server.U_id)
server_classm.start_thread(server.accept_clients )
server_classm.start_thread(server.prnt)

# logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
prev_pos = (0,0)
def on_move(x, y):
    global prev_pos
    new_pos = (x,y)
    if len(server.server_msg) < 5 and prev_pos !=new_pos:
        server.add_msg("Mouse_moved",new_pos)
        prev_pos = new_pos

def on_click(x, y, button, pressed):
    if pressed:
        #server.is_running = False
        #imp.reload(server_classm)
        button = str(button)
        print(button)
        server.add_msg("Mouse_pressed",{"buttons":button,"position":[x, y]})

def on_scroll(x, y, dx, dy):
    # logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    server.add_msg("Mouse_scroll",[x, y, dx, dy])
def mouse():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener :
        listener.join()

from pynput.keyboard import Listener as K_Listener
keys = []
def on_press(key):
    global keys
    if len(server.server_msg) < 8:
        server.add_msg("KEY_PRESSED",keys)
        keys = []
    else:
        keys.append(key)
    #print("Pressed {} keys".format(key))
def keyboard():
    with K_Listener(on_press=on_press) as listener :
        listener.join()

server_classm.start_thread(mouse )
server_classm.start_thread(keyboard )