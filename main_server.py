from server.rtp_server import RTPServer
import cv2

if __name__ == '__main__':
    import sys
    while True:
        server = RTPServer()
        try:
            server.setup()
            server.handle_rtsp_requests()
        except ConnectionError as e:
            server.server_state = server.STATE.TEARDOWN
            print(f"Connection reset: {e}")
        except KeyboardInterrupt:
            server.server_state = server.STATE.TEARDOWN
            break