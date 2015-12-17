import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
#matplotlib inline
import sys
import pandas as pd
import numpy as np

#--- fonctions perso

from convertCSV import *
from integration import *
#str_path_data = "/Users/lemaitrecedric/Documents/Riganami/Data/Bruit_Stationnaire/15_12_17/13_28_15.CSV"
str_path_data = "/Users/lemaitrecedric/Documents/Riganami/Data/Mesures_Terrain/11_22_50.CSV"
df = pd.read_csv(str_path_data)

#print type(df)


[Ax,Ay,Az,Gx,Gy,Gz,Mx,My,Mz,ATemp,Sonar,GPSL,GPSl] = CropData(df, 1, 78950)

ValidationData(df)

[Axc,Ayc,Azc,Gxc,Gyc,Gzc,Mxc,Myc,Mzc,ATempc,Sonarc,GPSLc,GPSlc] = ConvertData(Ax,Ay,Az,Gx,Gy,Gz,Mx,My,Mz,ATemp,Sonar,GPSL,GPSl)

print "Ax -> Valeur maxi : " + str(max(Axc)) + " Valeur mini : " + str(min(Axc)) + " Valeur moyenne : " + str(sum(Axc)/len(Axc)) + " Ecart type : " + str(np.std(Axc))
print "Ay -> Valeur maxi : " + str(max(Ayc)) + " Valeur mini : " + str(min(Ayc)) + " Valeur moyenne : " + str(sum(Ayc)/len(Ayc)) + " Ecart type : " + str(np.std(Ayc))
print "Az -> Valeur maxi : " + str(max(Azc)) + " Valeur mini : " + str(min(Azc)) + " Valeur moyenne : " + str(sum(Azc)/len(Azc)) + " Ecart type : " + str(np.std(Azc))
print "Gx -> Valeur maxi : " + str(max(Gxc)) + " Valeur mini : " + str(min(Gxc)) + " Valeur moyenne : " + str(sum(Gxc)/len(Gxc)) + " Ecart type : " + str(np.std(Gxc))
print "Gy -> Valeur maxi : " + str(max(Gyc)) + " Valeur mini : " + str(min(Gyc)) + " Valeur moyenne : " + str(sum(Gyc)/len(Gyc)) + " Ecart type : " + str(np.std(Gyc))
print "Gz -> Valeur maxi : " + str(max(Gzc)) + " Valeur mini : " + str(min(Gzc)) + " Valeur moyenne : " + str(sum(Gzc)/len(Gzc)) + " Ecart type : " + str(np.std(Gzc))
print "Mx -> Valeur maxi : " + str(max(Mxc)) + " Valeur mini : " + str(min(Mxc)) + " Valeur moyenne : " + str(sum(Mxc)/len(Mxc)) + " Ecart type : " + str(np.std(Mxc))
print "My -> Valeur maxi : " + str(max(Myc)) + " Valeur mini : " + str(min(Myc)) + " Valeur moyenne : " + str(sum(Myc)/len(Myc)) + " Ecart type : " + str(np.std(Myc))
print "Mz -> Valeur maxi : " + str(max(Mzc)) + " Valeur mini : " + str(min(Mzc)) + " Valeur moyenne : " + str(sum(Mzc)/len(Mzc)) + " Ecart type : " + str(np.std(Mzc))
print "ATemp -> Valeur maxi : " + str(max(ATempc)) + " Valeur mini : " + str(min(ATempc)) + " Valeur moyenne : " + str(sum(ATempc)/len(ATempc)) + " Ecart type : " + str(np.std(ATempc))

#print "Sonar -> Valeur maxi : " + str(max(Sonarc)) + " Valeur mini : " + str(min(Sonarc)) + " Valeur moyenne : " + str(sum(Sonarc)/len(Sonarc)) + " Ecart type : " + str(np.std(Sonarc))

print "GPSL -> Valeur maxi : " + str(max(GPSLc)) + " Valeur mini : " + str(min(GPSLc)) + " Valeur moyenne : " + str(sum(GPSLc)/len(GPSLc)) + " Ecart type : " + str(np.std(GPSLc))
print "GPSl -> Valeur maxi : " + str(max(GPSlc)) + " Valeur mini : " + str(min(GPSlc)) + " Valeur moyenne : " + str(sum(GPSlc)/len(GPSlc)) + " Ecart type : " + str(np.std(GPSlc))



#plt.annotate(texteAnnotation, xy=(1,MaxAx), xytext(8,0), xycoords=('axes fraction', 'data'), textcoords='offset points')
#plt.annotate(texteAnnotation, xy=(1, MaxAx), xytext=(8, 0),xycoords=('axes fraction', 'data'), textcoords='offset points')

#plt.plot(Axc)

#plt.plot(Ayc)
#plt.show()


#X = df['Num']
#Xc = X[1:78950]
#
##P0 = plt.figure(0)
#
## Three subplots sharing both x/y axes
#f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
#ax1.plot(Xc,Axc)
#ax1.set_title('Valeurs accelerometre')
#ax2.plot(Xc, Ayc, color='g')
#ax3.plot(Xc, Azc, color='r')
## Fine-tune figure; make subplots close to each other and hide x ticks for
## all but bottom plot.
#f.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
#
#
#P0 = plt.figure(1)
#
## Three subplots sharing both x/y axes
#f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
#ax1.plot(Xc,Gxc)
#ax1.set_title('Valeurs goniometre')
#ax2.plot(Xc, Gyc, color='g')
#ax3.plot(Xc, Gzc, color='r')
## Fine-tune figure; make subplots close to each other and hide x ticks for
## all but bottom plot.
#f.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
#
#
#
#P1 = plt.figure(2)
#
#
## Three subplots sharing both x/y axes
#f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
#ax1.plot(Xc,Mxc)
#ax1.set_title('Valeurs magnetometre')
#ax2.plot(Xc, Myc, color='g')
#ax3.plot(Xc, Mzc, color='r')
## Fine-tune figure; make subplots close to each other and hide x ticks for
## all but bottom plot.
#f.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
#
#
#P2 = plt.figure(2)
#
#
##save as pdf
#
#pp = PdfPages('FigAlbert.pdf')
#
#pp.savefig(P0)
#pp.savefig(P1)
#pp.savefig(P2)
#pp.close()
#
#plt.show()

val_calibrtion_zero = calcul_offset(Axc, Ayc, Azc, 1024)
velocity_init = []
velocity_init.extend([0,0,0])
position_init = []
position_init.extend([0,0,0])
velocity, position = double_integration(Axc, Axc, Azc, val_calibrtion_zero, velocity_init, position_init)
