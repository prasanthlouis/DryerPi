# Dryer Pi

## Overview
This project uses a Raspberry Pi Zero 2 W and an SW-420 Vibration Sensor to detect when your dryer or washer has stopped. The code monitors vibration and, after 5 minutes of no vibration, sends a push notification via Pushbullet to let you know when the laundry is done.

## Components
- **Raspberry Pi Zero 2 W**
- **SW-420 Vibration Sensor**

## How it Works
-The code continuously monitors the SW-420 sensor for vibration. If no vibration is detected for 5 minutes, it triggers a Pushbullet notification to alert you that your dryer/washer cycle is complete.
-If it detects 10 vibrations within 5 mins, it assumes the washer + dryer is on and sends you a notification

## Code Status
The code is functional but a bit rough. Feel free to edit and improve it to fit your needs!

## Enjoy! ❤️

## Screenshots

I know it looks super janky, but it works hahaha.

![20241108_100432](https://github.com/user-attachments/assets/8c4a28f5-7a97-4fdf-9ed6-f64af5086588)
![20241108_100428](https://github.com/user-attachments/assets/56b0a308-9c53-4d68-8d29-1230980c5146)
![Screenshot_20241107_212229_Niagara Launcher](https://github.com/user-attachments/assets/55125a5c-3620-44ae-9554-cf4b25b579ac)
