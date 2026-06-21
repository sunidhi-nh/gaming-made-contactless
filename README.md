```markdown
# Contactless Gaming

A wearable controller that turns hand tilts into game inputs — built with an ESP32, an MPU6050 accelerometer, and a bit of socket programming.

🎥 Demo: <https://www.linkedin.com/posts/sunidhi-n-ab2aa72a8_innovation-wearabletech-embeddedsystems-ugcPost-7438618818509406209-bwp6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEozV2YB24hK3k4rIOQC_fvPT8c20eLBeO0>

## How it works

1. The glove (ESP32 + MPU6050) reads accelerometer tilt on the X and Y axes
2. Tilting past a calibrated threshold in a direction triggers a gesture: LEFT, RIGHT, JUMP, or DUCK
3. The ESP32 sends that gesture over Wi-Fi (TCP socket) to a Python script running on a laptop
4. The laptop script maps each gesture to a keypress using `pyautogui` — turning your hand into a controller for endless-runner style games (Subway Surfers, Temple Run, etc.)

## Hardware
- ESP32 (running MicroPython)
- MPU6050 accelerometer/gyroscope
- Wi-Fi hotspot for ESP32 ↔ laptop communication

## Files
- `glove_sender.py` — runs on the ESP32, reads MPU6050, sends gesture over Wi-Fi
- `pc_receiver.py` — runs on the laptop, listens for gestures, triggers keypresses

## Setup

1. Flash `glove_sender.py` to your ESP32 (MicroPython)
2. Update the Wi-Fi SSID/password in the script to match your hotspot
3. Run `pc_receiver.py` on your laptop:
   - Install the dependency: `pip install pyautogui`
   - Then run it: `python pc_receiver.py`
4. Power on the glove — hold it straight when prompted to calibrate
5. Tilt to play

## Notes
- Gesture thresholds and cooldown are tunable in `glove_sender.py` if your glove is more/less sensitive than expected
- Built solo as a side project exploring wearables + IoT
