from auto_capture import AutoCapture
from video_writer import VideoWriter

if __name__ == "__main__":



    interval = 10
    duration = 25200
    num_frames = int(duration/interval)
    print(num_frames)
    cap = AutoCapture(interval, duration, '../images/test', (1920,1080))
    cap.capture()
    writer = VideoWriter('../images/test', '../videos/test', (1920,1080), num_frames, 15)
    writer.write()
