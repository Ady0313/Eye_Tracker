# Eye Tracker

A real-time eye-tracking system using OpenCV, designed to detect and track eyes through a webcam feed. This project demonstrates the use of object detection and tracking algorithms to accurately follow the movement of a person's eyes.

## Features
- Eye detection using Haar cascades.
- Real-time eye tracking with the MOSSE tracker.
- OpenCV integration for image processing and detection.
- Supports live webcam feed for eye detection and tracking.

## Prerequisites

To run this project, you'll need the following installed:

- Python 3.x
- OpenCV
- A webcam or video feed

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/Eye_Tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Eye_Tracker
   ```

3. Install the required Python packages:

   ```bash
   pip install opencv-python
   ```

4. Ensure you have the `haarcascade_eye.xml` file in your working directory. If not, download it from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

### Usage

1. Connect a webcam or use a video feed.
2. Run the Python script:

   ```bash
   python Eye_Tracker.py
   ```

3. The system will open a video feed window and track your eyes in real-time. Press 'q' to exit.

### Code Explanation

- **Eye Detection**: The project uses Haar cascade classifiers (`haarcascade_eye.xml`) to detect the eyes in a frame.
- **Tracking**: The MOSSE tracker tracks the detected eyes through the video stream. It updates the bounding box around the eyes as they move.
- **User Interface**: The bounding boxes and labels for the eyes are shown in yellow for better visibility.

### Project Structure

```
Eye_Tracker/
│
├── haarcascade_eye.xml  # Haar cascade model for eye detection
├── Eye_Tracker.py       # Main script for eye detection and tracking
└── README.md            # Project documentation
```

### Known Issues

- The tracking may become less accurate with fast movements.
- The system works best in good lighting conditions.

### Future Improvements

- Implement better tracking algorithms for improved performance with faster movements.
- Add support for multiple eye pairs detection.
- Integrate more sophisticated tracking algorithms like GOTURN or correlation filters.
