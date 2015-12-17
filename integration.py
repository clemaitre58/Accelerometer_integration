import numpy as np

def calcul_offset(vect_x, vect_y, vect_z, taille_cal_offset):
    taille_tab = len(vect_x)
    acc_x = acc_y = acc_z  = 0
    for i in  range(taille_cal_offset):
        acc_x += vect_x[i]
        acc_y += vect_y[i]
        acc_z += vect_z[i]
    offset_x = acc_x / taille_cal_offset
    offset_y = acc_y / taille_cal_offset
    offset_z = acc_z / taille_cal_offset

    offset = np.vstack((offset_x, offset_y, offset_z))
    return offset

def double_integration(vect_x, vect_y, vect_z, calibration, velocity_init, position_init):
    taille_vect = len(vect_x)
    velocity_x = []
    velocity_y = []
    velocity_z = []

    position_x = []
    position_y = []
    position_z = []

    for i in range(taille_vect):
        if (i == 0):
            velocity_x.append((vect_x[i]-calibration[0])+velocity_init[0])
            velocity_y.append((vect_y[i]-calibration[1])+velocity_init[1])
            velocity_z.append((vect_z[i]-calibration[2])+velocity_init[2])

            position_x.append((vect_x[i]-calibration[0])+velocity_init[0]+position_init[0])
            position_y.append((vect_y[i]-calibration[1])+velocity_init[1]+position_init[1])
            position_z.append((vect_z[i]-calibration[2])+velocity_init[2]+position_init[2])
        else:

            velocity_x.append((vect_x[i]-calibration[0])+velocity_x[i-1])
            velocity_y.append((vect_y[i]-calibration[1])+velocity_y[i-1])
            velocity_z.append((vect_x[i]-calibration[2])+velocity_z[i-1])

            position_x.append((vect_x[i]-calibration[0])+velocity_x[i-1]+position_x[i-1])
            position_y.append((vect_y[i]-calibration[1])+velocity_y[i-1]+position_y[i-1])
            position_z.append((vect_z[i]-calibration[2])+velocity_z[i-1]+position_z[i-1])

    velocity = np.vstack((velocity_x, velocity_y, velocity_z))
    position = np.vstack((position_x, position_y, position_z))
    return velocity, position
