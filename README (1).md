# -Real-Time-Hand-Gesture-Control-Interface

##  Hey there! Welcome to my Computer Vision project!

This is the **Real-Time Hand Gesture Control Interface**, a system I built to explore touchless Human-Computer Interaction (HCI). Think of it as a super low-latency way to control a computer using just your hands, without touching a single button.

The coolest part? It's all done using a standard webcam and some smart geometric rules—no heavy machine learning models needed, which keeps it snappy and fast!

---
### What You Need

* Python 3.x
* A working webcam (make sure your OS allows access!)

### Setup Steps

1.  **Clone the Repo:** Grab all the files from GitHub.
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd [YOUR_PROJECT_FOLDER]
    ```

2.  **Install Dependencies:** We're relying on OpenCV for video, MediaPipe, and NumPy for quick calculations.
    ```bash
    pip install opencv-python mediapipe numpy
    ```

3. 
    ```bash
    python main.py
    ```
    *Hit the **`q`** key to shut down the window when you're done.*

---
4. *Make sure you have lower version of python for example: Python 3.11 for better support of Dependencies*
---
## What It Can Recognize

Place your hand clearly in front of the camera and try these static gestures. The system uses geometric logic to classify them instantly:

| Gesture | What it is |
| :--- | :--- |
| **`Thumbs Up`** | Standard approval gesture. |
| **`Peace Sign (V)`** | Two fingers extended. |
| **`Index Up`** | Simple pointing gesture. |
| **`Closed Fist`** | All fingers curled in. |
| **`All Open`** | The classic "five" hand. |

---

## The System's Brains

I designed the architecture to be clean and modular. If I ever want to update the classification rules, I don't have to touch the camera module, which keeps the whole thing really robust.

| Folder | Core Classes | What It Handles (The "Why") |
| :--- | :--- | :--- |
| `vision_engine/` | `Camera.py`, `HandDetector.py` | Getting the video in and tracking the 21 finger landmarks. |
| `gesture_analyzer/` | `FeatureExtractor.py`, `GestureClassifier.py` | Calculating *which* fingers are up and translating that into a *name* (like "Thumbs Up"). |
| `data_viz/` | `OverlayManager.py` | Drawing the cool skeleton overlay and displaying the gesture name on the screen. |

---

## Formal Stuff

Need the full academic breakdown? Check out the `statement.md` file for the official Problem Statement, Functional Requirements (FRs), and Non-functional Requirements (NFRs).

Let me know if you have any questions.
