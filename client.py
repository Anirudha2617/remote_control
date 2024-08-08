import client_class
import pyautogui
from pynput.mouse import Listener


screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.


currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

client = client_class.Client()

def process_message( messages ):
	#print(len(messages))
	for msg in messages:
		message = msg["msg"]
		print(msg)
		if msg["prpse"][0] == 0:
			print(msg["msg"] ,"from",msg["from"])
		else:
			if msg["from"] not in client.clients_list :       
				print("Player created")
				client.clients_list.append(msg["from"])
				
			elif msg["prpse"] == "Mouse_moved":
				pyautogui.moveTo(message[0],message[1], duration=0.4, tween=pyautogui.easeInOutQuad)
				pyautogui.moveTo()
				print("Player moved")
				

			elif msg["prpse"] == "Mouse_pressed":
				if message["buttons"] == "button.left":
					pyautogui.click(message["position"][0],message["position"][1])
					print("Left mouse button pressed")

			elif msg["prpse"] == "Mouse_scroll":
				pyautogui.moveTo(message[0],message[1],duration=0)
				pyautogui.scroll(message[3])
				print("Mouse is scrolled")

			elif msg["prpse"] == "KEY_PRESSED":
				for i in message:
					pyautogui.press(i)
					print( i ,"is pressed now.")

				#print("Received:",msg["msg"])
		client.received_message.remove(msg)

client_class.start_thread(client.screen)
while True:
	process_message(client.received_message)