import pyb
def imu():
	acc = pyb.Accel()
	x = acc.y()
	y = acc.x()
	z = acc.z()
	print("x:",x*90/25," y:",y*90/25," z:",z*90/25)