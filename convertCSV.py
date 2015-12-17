def  ValidationData(Data) :
	print("Verification des donnees en cours")
	colNum = Data['Num'].values
	cpt = 0
	nbErreur = 0
	tailleTab = len(colNum)
	for element in colNum :
		if ((cpt + 1) < tailleTab-1) and (element != (colNum[cpt + 1] -1)) :
			print "erreur ligne : " + str(element)
			nbErreur += 1
		cpt += 1
	print "Total Nb erreurs : " + str(nbErreur)
	print("Verification des donnees termine")


def  ConvertData(Ax,Ay,Az,Gx,Gy,Gz,Mx,My,Mz,ATemp,Sonar,GPSL,GPSl) :
	print("Convertion des donnees en cours")

	# conversion des donees

	Axc = Ax * 8 / 32.768
	Ayc = Ay * 8 / 32.768
	Azc = (Az * 8 / 32.768) - 1000

	Gxc = Gx * 2000 / 32.768
	Gyc = Gy * 2000 / 32.768
	Gzc = Gz * 2000 / 32.768

	Mxc = Mx * 2 / 32.768
	Myc = My * 2 / 32.768
	Mzc = Mz * 2 / 32.768

	ATempc = ((ATemp * 0.125)/8)+21

	Sonarc = Sonar

	GPSLc = GPSL
	GPSlc = GPSl

	print("Convertion des donnees termine")

	return(Axc,Ayc,Azc,Gxc,Gyc,Gzc,Mxc,Myc,Mzc,ATempc,Sonarc,GPSLc,GPSlc)

def CropData(Data, Debut,Fin):

	# Accelerometre
	Ax = Data['Ax'].values
	Ay = Data['Ay'].values
	Az = Data['Az'].values

	# goniometre
	Gx = Data['Gx'].values
	Gy = Data['Gy'].values
	Gz = Data['Gz'].values

	#magnetometre
	Mx = Data['Mx'].values
	My = Data['My'].values
	Mz = Data['Mz'].values

	#capteur de temperature
	ATemp = Data['ATemp'].values

	#sonar
	Sonar = Data['SONAR'].values

	#gps
	GPSL = Data['GPSL'].values
	GPSl = Data['GPSl'].values

	# conversion des donees

	Axc = Ax[Debut:Fin]
	Ayc = Ay[Debut:Fin]
	Azc = Az[Debut:Fin]


	Gxc = Gx[Debut:Fin]
	Gyc = Gy[Debut:Fin]
	Gzc = Gz[Debut:Fin]

	Mxc = Mx[Debut:Fin]
	Myc = My[Debut:Fin]
	Mzc = Mz[Debut:Fin]

	ATempc = ATemp[Debut:Fin]

	Sonarc = Sonar[Debut:Fin]


	GPSLc = GPSL[Debut:Fin]

	GPSlc = GPSl[Debut:Fin]


	return(Axc,Ayc,Azc,Gxc,Gyc,Gzc,Mxc,Myc,Mzc,ATempc,Sonarc,GPSLc,GPSlc)
