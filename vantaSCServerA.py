import time
import collections
from socket import *
from nanpy import ArduinoApi
from nanpy import Servo
from nanpy import SerialManager

sample_map = collections.OrderedDict((
    ('316', 1570 + 855),
    ('OREAS 74a', 1570 + 640),
    ('6063', 1570 + 420),
    ('NIST 2710a', 1570 + 222),
    ('PVC High', 1570),
    ('Gold Plating', 1570 - 230),
    ('PVC Low', 1570 - 450),
    ('304', 1570 - 670),
    ('Pure Gold', 1570 - 878)
))

connection = SerialManager(device='/dev/ttyUSB0')
a = ArduinoApi(connection=connection)
servo = Servo(3)
servo.writeMicroseconds(1570 + 855)

host = "0.0.0.0"
port = 7777

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print("Sample Changer ready")

while True:
    print("Waiting for client...")
    q, addr = s.accept()

    print("Connected client: %s" % (addr, ))
    while True:
        msg = q.recv(1024)
        msgd = msg.decode()

        if not msg:
            q.close()
            break

        if msgd not in sample_map:
            print 'Invalid Sample requested'
        else:
            servo.writeMicroseconds(sample_map[msgd])
            print("Moved to Sample \"" + msgd + "\" in bay #" +
                  str(sample_map.keys().index(msgd) + 1) + " at " +
                  time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
