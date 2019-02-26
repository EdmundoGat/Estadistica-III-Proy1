import os
os.getcwd()

a = [".bad",".LOG",".info","Ambient.pgm"]
for i in range(2,40):
	if(i != 14):
		if(i<10):
			collection = "/Users/mundogn/Documents/EstadisticaAplicadaIII/CroppedYale_3/yaleB0"+str(i)
		else:
			collection = "/Users/mundogn/Documents/EstadisticaAplicadaIII/CroppedYale_3/yaleB"+str(i)
		j=1
		for k, filename in enumerate(os.listdir(collection)):
			a_match = [True for match in a if match in filename]
			if not(True in a_match):
				os.rename(collection +"/"+ filename, collection +"/"+ str(j) + ".pgm")
				j=j+1
		print("Imagenes yaleB"+str(i)+": "+str(j))