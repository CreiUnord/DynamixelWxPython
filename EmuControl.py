#http://pyax-12.readthedocs.io/en/latest/index.html
from pyax12.connection import Connection
import time

class Emu():
      
    def start(self):
        #self.sc = Connection(port="/dev/ttyUSB0", baudrate=57600)
        self.sc = Connection(port="/dev/ttyUSB0", baudrate=1000000)
        #self.sc = Connection(port="COM12", baudrate=1000000)
        self.sc.flush()

    def scanUnits(self):
        ids = self.sc.scan()
        return ids

    def readDxl(self,ID):
        self.sc.flush()
        self.sc.pretty_print_control_table(ID)

    def jointMode(self,ID):
        self.sc.set_cw_angle_limit(ID,0,False)
        self.sc.set_ccw_angle_limit(ID,1023,False)

    def wheelMode(self,ID):
        self.sc.set_ccw_angle_limit(ID,0,False)
        self.sc.set_cw_angle_limit(ID,0,False)

    def moveJoint(self, ID, position):
        self.sc.goto(ID, position, speed=512, degrees=True)
        time.sleep(1)

    def moveWheel(self,ID, speed):
        if speed < 0:
            if speed < -1024:
                speed = 2047
            else:
                speed = 1023 + -speed
        else:
            if speed > 1023:
                speed = 1023
        self.sc.flush()
        self.sc.goto(ID, 0, int(speed), degrees=False)

    def stop(self):
        self.sc.close()

    def getPos(self, ID):
        position = self.sc.get_present_position(ID, True)
        return position
