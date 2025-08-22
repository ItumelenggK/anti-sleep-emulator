from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Anti Sleep Emulator Running Successfully!"

@app.route('/dummy_sensor')
def dummy_sensor():
    # Simulate accelerometer data (g's)
    accel_x = round(random.uniform(-1.0, 1.0), 2)
    accel_y = round(random.uniform(-1.0, 1.0), 2)
    accel_z = round(random.uniform(0.8, 1.2), 2)  # gravity usually ~1g

    # Simulate gyroscope data (degrees/s)
    gyro_x = round(random.uniform(-180, 180), 1)
    gyro_y = round(random.uniform(-180, 180), 1)
    gyro_z = round(random.uniform(-180, 180), 1)

    # Simulate IR sensor: 0 = eyes open, 1 = eyes closed
    ir_state = random.choice(["eyes_open", "eyes_closed"])

    # Simple rule for drowsiness (just example):
    if ir_state == "eyes_closed" and abs(gyro_x) < 10:
        drowsiness = "Drowsy"
    else:
        drowsiness = "Awake"

    return jsonify({
        "accel": {"x": accel_x, "y": accel_y, "z": accel_z},
        "gyro": {"x": gyro_x, "y": gyro_y, "z": gyro_z},
        "ir": ir_state,
        "drowsiness": drowsiness
    })

if __name__ == '__main__':
    app.run(debug=True)