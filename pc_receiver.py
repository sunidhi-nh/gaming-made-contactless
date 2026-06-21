import socket
import pyautogui

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

server.listen(5)

print("Listening...")

while True:

    try:

        conn, addr = server.accept()

        data = conn.recv(1024).decode().strip()

        print("Received:", data)

        if data == "LEFT":
            pyautogui.press("left")

        elif data == "RIGHT":
            pyautogui.press("right")

        elif data == "JUMP":
            pyautogui.press("up")

        elif data == "DUCK":
            pyautogui.press("down")

        conn.close()

    except Exception as e:
        print("ERROR:", e)
