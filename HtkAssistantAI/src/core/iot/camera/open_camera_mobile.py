import cv2

class MobileCamera:
    def __init__(self, stream_url, save_interval=30, window_name='HTK Assistant AI - Mobile Camera'):
        self.stream_url = stream_url
        self.save_interval = save_interval
        self.window_name = window_name
        self.cap = cv2.VideoCapture(self.stream_url)
        self.frame_count = 0

    def start_stream(self):
        if not self.cap.isOpened():
            print("Unable to open the camera stream.")
            return

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame. Exiting...")
                break

            try:
                # Display the frame
                cv2.imshow(self.window_name, cv2.resize(frame, (600, 400)))
                key = cv2.waitKey(1)

                # Save the frame every `save_interval` frames
                if self.frame_count % self.save_interval == 0:
                    cv2.imwrite(f"frame_{self.frame_count}.jpg", frame)

                # Exit the loop if 'q' is pressed
                if key == ord('q'):
                    break

                self.frame_count += 1
            except cv2.error:
                print("Stream ended...!")
                break

        self.stop_stream()

    def stop_stream(self):
        self.cap.release()
        cv2.destroyAllWindows()