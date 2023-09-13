# Hand-Gesture-Mouse-Controller
A computer vision project that enables users to control the mouse cursor using hand gestures. Powered by MediaPipe and OpenCV.

## Overview
This project captures live video feed from the user's webcam to track hand landmarks in real-time. The software then translates these landmarks into mouse movements, clicks, and other actions, providing an intuitive interface for controlling the system.

## Features
- Real-time hand landmark detection using MediaPipe's Hand Solutions.
- Move the cursor using the index finger.
- Left-click by bringing the index and middle fingers close together.
- Right-click by bringing the index, middle, and ring fingers close together.
- Configurable smoothening factor for natural movement.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x
- Webcam

## Installation and Setup

### Clone the repository:

```bash
git clone https://github.com/gauravanand7870/Hand-Gesture-Mouse-Controller.git
```

### Navigate to the project directory:
```bash
cd Hand-Gesture-Mouse-Controller
 ```

### Install the required packages:
```bash
pip install -r requirements.txt
```

### Run the main script:
```bash 
python main.py
```

## Usage
- Show your hand in front of the webcam.
- Move the index finger to control the cursor.
- Bring the index and middle fingers together for a left-click.
- Bring the index, middle, and ring fingers together for a right-click.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements
- MediaPipe: For providing the robust solutions for hand tracking.
- OpenCV: For image and real-time video processing capabilities.
- autopy: For simulating mouse events.


## Feedback
If you have any feedback or issues, please open an issue in this repository.
