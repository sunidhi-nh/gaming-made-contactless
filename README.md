# Contactless Gaming

**Turn your hand into a game controller.**

![ESP32](https://img.shields.io/badge/ESP32-MicroPython-9C27B0?logo=espressif&logoColor=white)
![Sensor](https://img.shields.io/badge/Sensor-MPU6050-blue)
![Status](https://img.shields.io/badge/status-working%20prototype-brightgreen)

A wearable gesture controller — tilt your hand to move, jump, or duck in any endless-runner game. Built with an ESP32, an MPU6050 accelerometer, and a Wi-Fi socket bridge to your laptop.

🎬 **[Watch the demo on LinkedIn](https://www.linkedin.com/posts/sunidhi-n-ab2aa72a8_innovation-wearabletech-embeddedsystems-ugcPost-7438618818509406209-bwp6/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEozV2YB24hK3k4rIOQC_fvPT8c20eLBeO0)**

---

## How It Works

| Step | What Happens |
|------|--------------|
| 1 | Glove (ESP32 + MPU6050) reads tilt on X and Y axes |
| 2 | Tilt past a calibrated threshold triggers a gesture: `LEFT`, `RIGHT`, `JUMP`, or `DUCK` |
| 3 | ESP32 sends the gesture over Wi-Fi (TCP socket) to a laptop |
| 4 | Laptop script maps the gesture to a keypress via `pyautogui` |

Tilt left/right to steer, tilt up/down to jump or duck — no controller, no touch.

## Hardware
- ESP32 (MicroPython)
- MPU6050 accelerometer/gyroscope
- Wi-Fi hotspot for ESP32 ↔ laptop communication

## Files
| File | Role |
|------|------|
| `glove_sender.py` | Runs on the ESP32 — reads MPU6050, sends gesture over Wi-Fi |
| `pc_receiver.py` | Runs on the laptop — listens for gestures, fires keypresses |

## Setup

1. Flash `glove_sender.py` to your ESP32 (MicroPython)
2. Update the Wi-Fi SSID/password in the script to match your hotspot
3. On your laptop, install the dependency and run the receiver:
   - `pip install pyautogui`
   - `python pc_receiver.py`
4. Power on the glove — hold it straight when prompted to calibrate
5. Tilt to play

## Notes
- Gesture thresholds and cooldown are tunable in `glove_sender.py` if your glove is more/less sensitive than expected
- Jump and duck are swapped on purpose, felt funnier that way
- Built solo as a side project exploring wearables + IoT

---
**Built by [Sunidhi N](https://github.com/sunidhi-nh)**
