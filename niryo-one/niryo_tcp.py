from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import socket
import serial

rospy.init_node('niryo_one_example_python_api')

# print "--- Start"
n = NiryoOne()

try:
        # n.calibrate_auto()
        # n.calibrate_manual()
        time.sleep(1)

except NiryoOneException as e:
        print e
        n.activate_learning_mode(True)

n.set_arm_max_velocity(100)

HOST = '169.254.200.200'
PORT = 5021

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(5)

with serial.Serial('/dev/ttyACM0', 9600) as ser:
        x = ser.readline()
        print(x)
        while True:
                clientsocket, addr = s.accept()
                # print(f"Connection from {addr} has been established.")
        try:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        except ValueError:
            n.activate_learning_mode(True)

        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglen:
            try:
                print(full_msg[HEADERSIZE:])
                new_msg = True

                if full_msg[HEADERSIZE:] == "R":
                    print("We received a rock!")
                    n.move_joints([0.082, 0.365, -0.591, -0.26, -0.223, 1.593])
                    arduino_msg = "R\n"
                    ser.write(str(arduino_msg).encode("utf-8"))  # ser1
                    n.move_joints([0.056, -0.553, - 0.34, 0.032, 0.0925, 1.599])
                    time.sleep(1)
                elif full_msg[HEADERSIZE:] == "S":
                    print("We received a scissor!")
                    n.move_joints([0.082, 0.365, -0.591, -0.26, -0.223, 1.593])
                    arduino_msg = "S\n"
                    ser.write(str(arduino_msg).encode("utf-8"))  # ser2
                    time.sleep(1)
                    n.move_joints([0.056, -0.553, -0.34, 0.032, 0.0925, 1.599])
                elif full_msg[HEADERSIZE:] == "P":
                    print("We received a paper!")
                    n.move_joints([0.082, 0.365, -0.591, -0.26, -0.223, 1.594])
                    arduino_msg = "P\n"
                    ser.write(str(arduino_msg).encode("utf-8"))  # ser3
                    time.sleep(1)
                    n.move_joints([0.056, -0.553, -0.34, 0.032, 0.0925, 1.599])

                full_msg = ''
                y = ser.readline()
                print(y)


            except NiryoOneException as e:
                n.activate_learning_mode(True)

