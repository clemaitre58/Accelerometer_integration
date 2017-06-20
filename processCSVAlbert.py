import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from pandas import DataFrame, read_csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#matplotlib inline
import sys
import pandas as pd
import numpy as np
#import ipdb
#--- fonctions perso

from convertCSV import *
from integration import *
freq_ech = 20

#str_path_data = "/home/cedric/Documents/Riganami/Data/TestMagneto/11_6_11.CSV"
str_path_data = "/home/cedric/Documents/Conseil/Drumistic/Documents/DocProtoExplo/D_Drummer_Proto_Explo/TestDrift/Data/data_lin_accelero.csv"
#str_path_data = "/home/cedric/Documents/Riganami/Data/Mesures_Terrain/11_22_50.CSV"

#str_path_data = "/home/cedric/Documents/Riganami/Data/Bruit_Stationnaire/15_12_17/13_28_15.CSV"
df = pd.read_csv(str_path_data)

#print type(df)


[Ax,Ay,Az] = CropData(df, 2000, 8532)

#ValidationData(df)

[Axc,Ayc,Azc] = ConvertData(Ax,Ay,Az,)

print ("Ax -> Valeur maxi : " + str(max(Axc)) + " Valeur mini : " + str(min(Axc)) + " Valeur moyenne : " + str(sum(Axc)/len(Axc)) + " Ecart type : " + str(np.std(Axc)))
print ("Ay -> Valeur maxi : " + str(max(Ayc)) + " Valeur mini : " + str(min(Ayc)) + " Valeur moyenne : " + str(sum(Ayc)/len(Ayc)) + " Ecart type : " + str(np.std(Ayc)))
print ("Az -> Valeur maxi : " + str(max(Azc)) + " Valeur mini : " + str(min(Azc)) + " Valeur moyenne : " + str(sum(Azc)/len(Azc)) + " Ecart type : " + str(np.std(Azc)))
#print "Gx -> Valeur maxi : " + str(max(Gxc)) + " Valeur mini : " + str(min(Gxc)) + " Valeur moyenne : " + str(sum(Gxc)/len(Gxc)) + " Ecart type : " + str(np.std(Gxc))
#print "Gy -> Valeur maxi : " + str(max(Gyc)) + " Valeur mini : " + str(min(Gyc)) + " Valeur moyenne : " + str(sum(Gyc)/len(Gyc)) + " Ecart type : " + str(np.std(Gyc))
#print "Gz -> Valeur maxi : " + str(max(Gzc)) + " Valeur mini : " + str(min(Gzc)) + " Valeur moyenne : " + str(sum(Gzc)/len(Gzc)) + " Ecart type : " + str(np.std(Gzc))
#print "Mx -> Valeur maxi : " + str(max(Mxc)) + " Valeur mini : " + str(min(Mxc)) + " Valeur moyenne : " + str(sum(Mxc)/len(Mxc)) + " Ecart type : " + str(np.std(Mxc))
#print "My -> Valeur maxi : " + str(max(Myc)) + " Valeur mini : " + str(min(Myc)) + " Valeur moyenne : " + str(sum(Myc)/len(Myc)) + " Ecart type : " + str(np.std(Myc))
#print "Mz -> Valeur maxi : " + str(max(Mzc)) + " Valeur mini : " + str(min(Mzc)) + " Valeur moyenne : " + str(sum(Mzc)/len(Mzc)) + " Ecart type : " + str(np.std(Mzc))
#print "ATemp -> Valeur maxi : " + str(max(ATempc)) + " Valeur mini : " + str(min(ATempc)) + " Valeur moyenne : " + str(sum(ATempc)/len(ATempc)) + " Ecart type : " + str(np.std(ATempc))

#print "Sonar -> Valeur maxi : " + str(max(Sonarc)) + " Valeur mini : " + str(min(Sonarc)) + " Valeur moyenne : " + str(sum(Sonarc)/len(Sonarc)) + " Ecart type : " + str(np.std(Sonarc))

#print "GPSL -> Valeur maxi : " + str(max(GPSLc)) + " Valeur mini : " + str(min(GPSLc)) + " Valeur moyenne : " + str(sum(GPSLc)/len(GPSLc)) + " Ecart type : " + str(np.std(GPSLc))
#print "GPSl -> Valeur maxi : " + str(max(GPSlc)) + " Valeur mini : " + str(min(GPSlc)) + " Valeur moyenne : " + str(sum(GPSlc)/len(GPSlc)) + " Ecart type : " + str(np.std(GPSlc))
#

print("\n\n\n")

print("Offset A : " + str(Compute_offset(sum(Axc)/len(Axc), sum(Ayc)/len(Ayc), sum(Azc)/len(Azc))))
#print "Offset G : " + str(Compute_offset(sum(Gxc)/len(Axc), sum(Gyc)/len(Gyc), sum(Gzc)/len(Gzc)))
#print "Offset M : " + str(Compute_offset(sum(Mxc)/len(Mxc), sum(Ayc)/len(Myc), sum(Azc)/len(Mzc)))

#X1 = Azc[23400:25000];
#X2 = Azc[28200:32000];
#X3 = Azc[36000:40300];
#X4 = Azc[41000:44600];
#X5 = Azc[53000:55700];
#X6 = Azc[59000:61000];
#X7 = Azc[63400:66120];
#X8 = Azc[68000:71000];
#X9 = Azc[75000:76800];
#X10 = Azc[81000:83000];
#X11 = Azc[92000:94400];
#X12 = Azc[96840:100000];
#X13 = Azc[103600:105700];
#
#
#print str(calcul_rms(X1)-1)
#print str(calcul_rms(X2)-1)
#print str(calcul_rms(X3)-1)
#print str(calcul_rms(X4)-1)
#print str(calcul_rms(X5)-1)
#print str(calcul_rms(X6)-1)
#print str(calcul_rms(X7)-1)
#print str(calcul_rms(X8)-1)
#print str(calcul_rms(X9)-1)
#print str(calcul_rms(X10)-1)
#print str(calcul_rms(X11)-1)
#print str(calcul_rms(X12)-1)
#print str(calcul_rms(X13)-1)
#
#print "Ecart type"
#
#print str(variance_rms(X1))
#print str(variance_rms(X2))
#print str(variance_rms(X3))
#print str(variance_rms(X4))
#print str(variance_rms(X5))
#print str(variance_rms(X6))
#print str(variance_rms(X7))
#print str(variance_rms(X8))
#print str(variance_rms(X9))
#print str(variance_rms(X10))
#print str(variance_rms(X11))
#print str(variance_rms(X12))
#print str(variance_rms(X13))
#
#
#print "Fidélité"
#print str(fidelite(X1))
#print str(fidelite(X2))
#print str(fidelite(X3))
#print str(fidelite(X4))
#print str(fidelite(X5))
#print str(fidelite(X6))
#print str(fidelite(X7))
#print str(fidelite(X8))
#print str(fidelite(X9))
#print str(fidelite(X10))
#print str(fidelite(X11))
#print str(fidelite(X12))
#print str(fidelite(X13))

#X = df['Num']
#Xc = X[1:107000]
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
#P2 = plt.figure(3)
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
#
val_calibrtion_zero = calcul_offset(Axc, Ayc, Azc, len(Axc))
velocity_init = []
velocity_init.extend([0, 0, 0])
position_init = []
position_init.extend([0, 0, 0])

Axc = Conv_g2ms2(Axc)
Ayc = Conv_g2ms2(Ayc)
Azc = Conv_g2ms2(Azc)
velocity, position = double_integration(Axc, Ayc, Azc, val_calibrtion_zero, velocity_init, position_init, freq_ech)

velocity_simpson, position_simpson = double_integration_simpson(
    Axc,
    Ayc,
    Azc,
    val_calibrtion_zero,
    velocity_init,
    position_init,
    freq_ech,
    20)

print (np.shape(position))
print (np.shape(Axc))
var_distance_plan_xy = position_dist_origine_planxy(position[0, :], position[1, :])
var_distance_plan_xy_simpson = position_dist_origine_planxy(
    position_simpson[0, :],
    position_simpson[1, :])

val_maxi_div = 0.2

print(var_distance_plan_xy)

ind_div_max = trouve_ind_divergence(var_distance_plan_xy, val_maxi_div)

print(ind_div_max)


temps_div_dist = trouve_dis_div_temps(var_distance_plan_xy, 60, freq_ech)
temps_div_dist_1 = trouve_dis_div_temps(var_distance_plan_xy, 1, freq_ech)
print("temps pour diverger de " + str(val_maxi_div)  + "mm : " + str(ind_div_max * 1./freq_ech) + "sec")
print("Distance de diverge apres 1min : " + str(temps_div_dist) + "m")
#fig = plt.figure()
ind_div_max_simpson = trouve_ind_divergence(var_distance_plan_xy_simpson, val_maxi_div)

temps_div_dist_simpson = trouve_dis_div_temps(var_distance_plan_xy_simpson, 60, freq_ech)

print ("Methode de Simpson -> temps pour diverger de " + str(val_maxi_div)  + "m : " + str(ind_div_max_simpson* 1./freq_ech) + "sec")
print ("Methode de Simpson -> Distance de diverge apres 1min : " + str(temps_div_dist_simpson) + "m")
print ("Methode de Simpson -> Distance de diverge apres 1sec : " + str(temps_div_dist_1) + "m")
#ipdb.set_trace()
#delta_pos = np.abs(
#    (
#
#        position[0, 0:78900]
#        -
#        position_simpson[0, 0:78900]
#    )
#    )/np.abs(position[0, 0:78900])
#
#delta_pos *= 1000.
##)
#
#if(position[0, 0]==0 and position_simpson[0, 0]==0) :
#    delta_pos[0] = 0
#
#val_un = np.ones((78900, ))
#
#plt.figure()
#plt.plot(delta_pos[100: 78900])
##plt.plot(val_un)
#plt.show()

#ax = fig.add_subplot(111, projection='3d')
##n = 100
##for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
##xs = randrange(n, 23, 32)
##ys = randrange(n, 0, 100)
##zs = randrange(n, zl, zh)
#print np.shape(position)
#ax.scatter(position[:,1], position[:,2], position[:,3])
#print position[1:]
#ax.set_xlabel('X Label')
