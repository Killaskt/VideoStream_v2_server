import pickle
import socket
import struct
import base64
import numpy as np
import cv2
import time

# the ip will be whatever your computer's ip is,, any device on your wifi will be able to connect to it
HOST = '0.0.0.0'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('[INFO] Socket created')
s.bind((HOST, PORT))
print('[INFO] Socket bind complete')
s.listen(10)
print('[INFO] Socket now listening')

conn, addr = s.accept()

print('[CONNECTED] Connection made with {}:{}'.format(addr[0], addr[1]))

data = b'' ### CHANGED
payload_size = struct.calcsize("L") ### CHANGED

frame_total = 0
start = time.time()

print('[INFO] getting camera ready')
time.sleep(1)

while True:


    if frame_total and (frame_total % 30) == 0:
        print('[FPS] frames read: {}, FPS - {}'.format(frame_total, frame_total/(time.time() - start)))

    # Retrieve message size
    while len(data) < payload_size:
        data += conn.recv(4092)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += conn.recv(4092)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Extract frame
    # frame = pickle.loads(frame_data)
    raw = base64.b64decode(frame_data)
    # np_img = np.fromstring(raw, dtype=np.uint8) # Deprecated
    np_img = np.frombuffer(raw, dtype=np.uint8)
    frame = cv2.imdecode(np_img, 1)


    frame_total += 1

    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)