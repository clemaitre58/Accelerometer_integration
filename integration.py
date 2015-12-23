import numpy as np
import ipdb;
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

def double_integration(vect_x, vect_y, vect_z, calibration, velocity_init, position_init, freq_ech):
    delta_t = 1./freq_ech
    taille_vect = len(vect_x)
    velocity_x = []
    velocity_y = []
    velocity_z = []

    position_x = []
    position_y = []
    position_z = []
    for i in range(taille_vect):
        if (i == 0):
            #Attention a le faire plus proprement pour initialisation different de
            # A(0, 0,0) V(0, 0, 0)
            velocity_x.append(0)
            velocity_y.append(0)
            velocity_z.append(0)

            position_x.append(0)
            position_y.append(0)
            position_z.append(0)
        if (i == 1):
            velocity_x.append(vect_x[1]/2. * delta_t)
            velocity_y.append(vect_y[1]/2. * delta_t)
            velocity_z.append(vect_z[1]/2. * delta_t)

            position_x.append(velocity_x[1]/2. *delta_t)
            position_y.append(velocity_y[1]/2. *delta_t)
            position_z.append(velocity_z[1]/2.  *delta_t)
        if (i > 1):
            #            ipdb.set_trace()
            velocity_x.append(velocity_x[i-1]+integration_trapeze(i-1, i, vect_x, delta_t))
            velocity_y.append(velocity_y[i-1]+integration_trapeze(i-1, i, vect_y, delta_t))
            velocity_z.append(velocity_z[i-1]+integration_trapeze(i-1, i, vect_z, delta_t))

            position_x.append(position_x[i-1]+integration_trapeze(i-1, i, velocity_x, delta_t))
            position_y.append(position_y[i-1]+integration_trapeze(i-1, i, velocity_y, delta_t))
            position_z.append(position_z[i-1]+integration_trapeze(i-1, i, velocity_z, delta_t))
    #ipdb.set_trace()
    #    print np.shape(position_x)
    #    print np.shape(position_y)
    velocity = np.array([velocity_x, velocity_y, velocity_z])
    position = np.array([position_x, position_y, position_z])
    return velocity, position

def integration_trapeze(a, b, f, delta_t):
    f_a = f[a]
    f_b = f[b]
    val_int = (f_a+f_b)/2.
    val_int *= delta_t

    return val_int
def position_dist_origine_planxy(x, y, x0=0, y0=0):
    x -= x0
    y -= y0
    res = np.sqrt(
        np.power(x, 2)
        +
        np.power(y, 2)
    )

    return res

def trouve_ind_divergence(vect, val_divergence):
    taille_vect = len(vect)
    for i  in range(taille_vect):
        if (vect[i] >= val_divergence):
            return i

