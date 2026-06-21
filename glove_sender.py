from machine import Pin, I2C
import time
import network
import socket

# WIFI
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("GestureHotspot", "12345678")

while not wifi.isconnected():
    time.sleep(0.5)

print("WiFi connected")

# SOCKET
LAPTOP_IP = "192.168.137.1"
PORT = 5000

def send(msg):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((LAPTOP_IP, PORT))
        s.send(msg.encode())
        s.close()
        print("SENT:", msg)
    except:
        pass

# MPU6050
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
MPU = 0x68
i2c.writeto_mem(MPU, 0x6B, b'\x00')

def read_word(reg):
    data = i2c.readfrom_mem(MPU, reg, 2)
    value = (data[0] << 8) | data[1]

    if value > 32767:
        value -= 65536

    return value

def read_avg(reg, samples=5):
    total = 0

    for _ in range(samples):
        total += read_word(reg)
        time.sleep(0.003)

    return total // samples

# CALIBRATION
print("Hold glove straight...")

sum_x = 0
sum_y = 0

for _ in range(40):
    sum_x += read_avg(0x3B)
    sum_y += read_avg(0x3D)
    time.sleep(0.03)

base_x = sum_x // 40
base_y = sum_y // 40

print("Baseline:", base_x, base_y)

# SETTINGS
THRESHOLD_X = 3000
THRESHOLD_Y = 3000

COOLDOWN = 1000

last_action = 0

# MAIN LOOP
while True:

    ax = read_avg(0x3B)
    ay = read_avg(0x3D)

    dx = ax - base_x
    dy = ay - base_y

    now = time.ticks_ms()

    # RIGHT
    if dx > THRESHOLD_X:

        if time.ticks_diff(now, last_action) > COOLDOWN:

            send("RIGHT")
            last_action = now

    # LEFT
    elif dx < -THRESHOLD_X:

        if time.ticks_diff(now, last_action) > COOLDOWN:

            send("LEFT")
            last_action = now

    # JUMP
    elif dy > THRESHOLD_Y:

        if time.ticks_diff(now, last_action) > COOLDOWN:

            send("JUMP")
            last_action = now

    # DUCK
    elif dy < -THRESHOLD_Y:

        if time.ticks_diff(now, last_action) > COOLDOWN:

            send("DUCK")
            last_action = now

    time.sleep(0.08)
