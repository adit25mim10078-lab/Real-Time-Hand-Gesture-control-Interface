# Real-Time Hand Gesture Control Interface

**Adapted and maintained by: Adit Patidar**

A real-time hand gesture recognition interface using Python, OpenCV, MediaPipe, and NumPy.
The project detects hand landmarks through a webcam and classifies common static hand gestures.

## Project Author / Maintainer

**Adit Patidar**

This repository is an adapted version of the publicly available project:

**Original repository:** https://github.com/KushagraCloud/-Real-Time-Hand-Gesture-Control-Interface

The original project structure and core implementation are retained where applicable.
Changes in this version include project metadata, documentation, application labeling, and cleanup for personal/academic use.

## Requirements

- Python 3.11 recommended
- Webcam
- OpenCV
- MediaPipe
- NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Press `q` to exit.

## Recognized Gestures

- All Open / Hi
- Closed Fist
- Thumbs Up
- Index Point
- Peace / V
- Three Fingers
- Other supported gesture patterns

## Project Structure

```text
vision_engine/
    Camera.py
    HandDetector.py

gesture_analyzer/
    FeatureExtractor.py
    GestureClassifier.py

data_viz/
    OverlayManager.py

main.py
STATEMENT.md
requirements.txt
```

## How It Works

1. The webcam captures live video.
2. MediaPipe detects the hand and its 21 landmarks.
3. Finger-extension features are extracted from landmark coordinates.
4. The gesture classifier maps those features to a gesture name.
5. OpenCV displays the hand skeleton and detected gesture.

## Academic Note

For academic submission, the user should understand and be able to explain the implementation and should follow their institution's rules regarding reuse of public repositories.
