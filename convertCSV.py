import numpy as np

def  ValidationData(Data) :
	print("Verification des donnees en cours")
	colNum = Data['Num'].values
	cpt = 0
	nbErreur = 0
	tailleTab = len(colNum)
	for element in colNum :
		if ((cpt + 1) < tailleTab-1) and (element != (colNum[cpt + 1] -1)) :
			print ("erreur ligne : " + str(element))
			nbErreur += 1
		cpt += 1
	print ("Total Nb erreurs : " + str(nbErreur))
	print("Verification des donnees termine")


def  ConvertData(Ax,Ay,Az) :
	print("Convertion des donnees en cours")

	# conversion des donees

	Axc =np. double(Ax) * 4 / 32768
	Ayc = np.double(Ay) * 4/ 32768
	Azc = (np.double(Az) * 4/ 32768)

	#Gxc = np.double(Gx) * 2000 / 32768
	#Gyc = np.double(Gy) * 2000 / 32768
	#Gzc = np.double(Gz) * 2000 / 32768

	#Mxc = np.double(Mx) * 2 / 32768
	#Myc = np.double(My) * 2 / 32768
	#Mzc = np.double(Mz) * 2 / 32768

	#ATempc = ((np.double(ATemp) * 0.125)/8)+21

	#Sonarc = Sonar

	#GPSLc = GPSL
	#GPSlc = GPSl

	print("Convertion des donnees termine")

	return(Axc,Ayc,Azc)

def CropData(Data, Debut,Fin):

    Data = Data.astype(float)

    # Accelerometre
    Ax = Data['Ax'].values
    Ay = Data['Ay'].values
    Az = Data['Az'].values
    
    # Quaternion
    q0 = Data['q0'].values
    q1 = Data['q1'].values
    q2 = Data['q2'].values
    q3 = Data['q3'].values
    
    # Timestamp
    timestamp = Data['timestamp'].values
    
    ## goniometre
    #Gx = Data['Gx'].values
    #Gy = Data['Gy'].values
    #Gz = Data['Gz'].values
    
    ##magnetometre
    #Mx = Data['Mx'].values
    #My = Data['My'].values
    #Mz = Data['Mz'].values
    
    ##capteur de temperature
    #ATemp = Data['ATemp'].values
    
    ##sonar
    #Sonar = Data['SONAR'].values
    
    ##gps
    #GPSL = Data['GPSL'].values
    #GPSl = Data['GPSl'].values
    
    ## conversion des donees
    
    Axc = Ax[Debut:Fin]
    Ayc = Ay[Debut:Fin]
    Azc = Az[Debut:Fin]
    
    # Quaternion
    q0c = q0[Debut:Fin]
    q1c = q1[Debut:Fin]
    q2c = q2[Debut:Fin]
    q3c = q3[Debut:Fin]
    
    # Timestamp
    timestampc = timestamp[Debut:Fin]
    
    #Gxc = Gx[Debut:Fin]
    #Gyc = Gy[Debut:Fin]
    #Gzc = Gz[Debut:Fin]
    
    #Mxc = Mx[Debut:Fin]
    #Myc = My[Debut:Fin]
    #Mzc = Mz[Debut:Fin]
    
    #ATempc = ATemp[Debut:Fin]
    
    #Sonarc = Sonar[Debut:Fin]
    
    
    #GPSLc = GPSL[Debut:Fin]
    
    #GPSlc = GPSl[Debut:Fin]
    
    
    return(Axc, Ayc, Azc, q0c, q1c, q2c, q3c, timestamp)

def Compute_offset(a, b, c):
    a_2 = np.power(a, 2)
    b_2 = np.power(b, 2)
    c_2 = np.power(c, 2)

    return np.sqrt(a_2+b_2+c_2)

def Conv_g2ms2(val):
    nb_val = len(val)
    res = []
    for i in range(nb_val):
        val_lu = val[i];
        val_lu *= 9.80665
        res.append(val_lu)

    return res
