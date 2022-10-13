import cv2
import numpy as np
import base64

class VideoStream:
    FRAME_HEADER_LENGTH = 5
    DEFAULT_IMAGE_SHAPE = (380, 280)
    DEFAULT_FPS = 60

    # if it's present at the end of chunk,
    # it's the last chunk for current jpeg (end of frame)
    JPEG_EOF = b'\xff\xd9'

    def __init__(self):
        # for simplicity, mjpeg is assumed to be on working directory
        # self._stream = open(file_path, 'rb')
        # frame number is zero-indexed
        # after first frame is sent, this is set to zero
        self._stream = cv2.VideoCapture(0)
        self.current_frame_number = -1

    def close(self):
        self._stream.release()
        cv2.destroyAllWindows()

    def get_next_frame(self) -> bytes:
        # sample video file format is as follows:
        # - 5 digit integer `frame_length` written as 5 bytes, one for each digit (ascii)
        # - `frame_length` bytes follow, which represent the frame encoded as a JPEG
        # - repeat until EOF
        ret, frame = self._stream.read()
        frame = cv2.resize(frame, self.DEFAULT_IMAGE_SHAPE)
        self.current_frame_number += 1
        encoded, buf = cv2.imencode('.jpg', frame)
        return bytes(buf)
