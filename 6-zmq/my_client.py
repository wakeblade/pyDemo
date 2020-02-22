import zmq
import sys

context =zmq.Context()
print("Connecting to server......")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
while True:
    i = input("请输入内容：").strip()
    if i == 'b':
        sys.exit()
    socket.send(i.encode('utf-8'))

    message = socket.recv()
    print("Received reply:",message.decode("utf-8")) 