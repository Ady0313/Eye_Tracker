import tkinter as tk
from tkinter import messagebox
import threading

def start_eye_tracking():
    try:
        # Call the main eye tracking script here
        eye_tracking_script()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eye_tracking_script():
    import cv2

    # Initialize components
    cap = initialize_camera()
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the frame
        gray_frame = preprocess_frame(frame)

        # Detect eyes
        eyes = detect_eyes(gray_frame, eye_cascade)

        # Track eyes and update frame
        frame = track_eyes(frame, eyes)

        # Display the resulting frame
        display_frame(frame)

        # Check for exit key
        if check_for_exit():
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# Setting up the GUI
root = tk.Tk()
root.title("Eye Tracker System")

start_button = tk.Button(root, text="Start Eye Tracking", command=lambda: threading.Thread(target=start_eye_tracking).start())
start_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

root.mainloop()