import serial

ser = serial.Serial('COM12', 115200)
ser.readline() #captures the junk readline

x0 = float(ser.readline())
print x0
y0 = float(ser.readline())
print y0
z0 = float(ser.readline())
print z0

while True:
	x1 = float(ser.readline())
	y1 = float(ser.readline())
	z1 = float(ser.readline())


	if (abs(x1-x0) <= 60 and abs(y1-y0) <= 60 and abs(y1-y0) <= 60):
		ser.write('1')
		print 'TRUE! TRUE! TRUE!'
		
	else: 
		ser.write('0')
		print 'FALSE! FALSE! FALSE!'

	print ("x1: "+str(x1))
	print ("y1: "+str(y1))
	print ("z1: "+str(z1))
