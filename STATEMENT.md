## 1. Core Problem We are Trying to Solve

This project aimed to address a real-world limitation: reliance on physical input in places where touch is slow, unsanitary, or not possible. What was required was **hands-free and reliable control**. This gesture interface accomplishes exactly that-a rugged, accurate system that avoids physical touch altogether, converting simple hand postures into unambiguous digital commands.

## 2. Functional Requirements (FRs)

Here is a breakdown of what the system *must* do, mapped directly to the code components:

| ID | Requirement | Status | Module |
| :--- | :--- | :--- | :--- |
FR1 The system must capture and process each frame from a real-time video continuously. Complete `Camera.py`
| **FR2** | Accurately detect the hand and find all 21 key landmarks. | Complete | `HandDetector.py` |
| **FR3** | Must extract features from the landmarks. A 5-finger open/closed vector. | Complete | `FeatureExtractor.py` |
| **FR4** | The system shall classify the feature vector into a pre-defined gesture name. | Complete | `GestureClassifier.py` |

| **FR5** | Shall provide visual feedback by showing the tracking skeleton along with the gesture label.  | Complete | `OverlayManager.py` |

## 3. Non-functional Requirements (NFRs)

This is how we ensured the system isn't just functional, but *good*:
| ID | Requirement | Goal Achieved | How We Met It |
| :--- | :--- | :--- | :--- |
| **NFR1** | **Real-time Performance** | Processing below 100ms per frame. | Achieved by utilizing light-weight geometric classification rules instead of a heavy neural network. |
| **NFR2** | **Reliability** | Consistent accuracy above 85% for core gestures. | Achieved through precise coordinate analysis using NumPy.

| **NFR3** | **Usability** | Intuitive and comfortable for the user. | Provided through a mirrored video feed and text feedback immediately.

| **NFR4** | **Maintainability** | Highly modular codebase. | Achieved by strictly separating I/O (`vision_engine`), logic (`gesture_analyzer`), and rendering (`data_viz`). |

4. Summary of Implementation: The entire classification engine is based on a smart, simple trick: **relative Y-coordinate comparison**. Instead of complex distance metrics, we check if the **tip of a finger (e.g., landmark 8)** is vertically higher-i.e., a *smaller* Y-coordinate in screen space-than its **middle knuckle (landmark 7)**. If the tip is higher, then the finger is logically extended. This simple, fast check across all five fingers creates the feature vector, which the classifier reads in. This is, in fact, the very core of why the system runs so fast and directly satisfies the demanding **NFR1** goal.
