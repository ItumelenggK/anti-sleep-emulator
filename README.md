# Anti-Sleep Glasses Emulator (Flask App)

## Overview
This repository contains the **Flask emulator** for the Anti-Sleep Glasses project.  
It simulates sensor data from the Arduino (MPU6050 and IR sensors) and predicts drowsiness using dummy AI logic.  
This allows testing the system **without the hardware**.

## Features
- Simulates accelerometer, gyroscope, and eye-state data.
- REST endpoints:
  - `/dummy_sensor` → Returns dummy sensor data and drowsiness state.
  - `/` → Home/status endpoint.
- Prepares the system for integration with real Arduino data via Bluetooth.

## Requirements
- Python 3.12 or higher
- Flask
- Other Python dependencies listed in `requirements.txt`

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/ItumelenggK/anti-sleep-emulator.git
cd anti-sleep-emulator
