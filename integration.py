import numpy as np
#import ipdb

def fidelite(x):
    J = []
    taille = 10
    for i in range(taille):
        J.append(calcul_rms(x[i*100:i*100+100]))
    Vmin = np.min(J)
    Vmax = np.max(J)

    return Vmax-Vmin

def variance_rms(x):
    J = []
    taille = 10
    for i in range(taille):
        J.append(calcul_rms(x[i*100:i*100+100]))
    return np.sqrt(np.var(J))

def calcul_rms(x, axis=None):
        return np.sqrt(np.mean(x**2, axis=axis))

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
            velocity_x.append(velocity_init[0])
            velocity_y.append(velocity_init[1])
            velocity_z.append(velocity_init[2])

            position_x.append(position_init[0])
            position_y.append(position_init[1])
            position_z.append(position_init[2])
        if (i == 1):
            velocity_x.append(velocity_init[0]+integration_trapeze_init(velocity_init[0], i, vect_x, delta_t))
            velocity_y.append(velocity_init[1]+integration_trapeze_init(velocity_init[1], i, vect_y, delta_t))
            velocity_z.append(velocity_init[2]+integration_trapeze_init(velocity_init[2], i, vect_z, delta_t))

            position_x.append(position_init[0]+integration_trapeze_init(position_init[0], i, velocity_x, delta_t))
            position_y.append(position_init[1]+integration_trapeze_init(position_init[1], i, velocity_y, delta_t))
            position_z.append(position_init[2]+integration_trapeze_init(position_init[2], i, velocity_z, delta_t))
        if (i > 1):
            #ipdb.set_trace()
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

def integration_trapeze_init(val_init, b, f, delta_t):
    f_a = val_init
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

def trouve_dis_div_temps(vect, temps, freq_ech):
    taille_vect = len(vect)
    nb_ech_stop = temps / (1/freq_ech)
    return vect[nb_ech_stop]


def double_integration_simpson(vect_x, vect_y, vect_z, calibration, velocity_init, position_init, freq_ech, nb_ech):
    delta_t = 1./freq_ech
    taille_vect = len(vect_x)
    velocity_x = []
    velocity_y = []
    velocity_z = []

    position_x = []
    position_y = []
    position_z = []
    for i in range(taille_vect-nb_ech):
        if (i == 0):
            velocity_x.append(velocity_init[0])
            velocity_y.append(velocity_init[1])
            velocity_z.append(velocity_init[2])

            position_x.append(position_init[0])
            position_y.append(position_init[1])
            position_z.append(position_init[2])
        if (i == 1):
            velocity_x.append(velocity_init[0]+integration_simpson_init(velocity_init[0], i, vect_x, delta_t, nb_ech))
            velocity_y.append(velocity_init[1]+integration_simpson_init(velocity_init[1], i, vect_y, delta_t, nb_ech))
            velocity_z.append(velocity_init[2]+integration_simpson_init(velocity_init[2], i, vect_z, delta_t, nb_ech))

            position_x.append(position_init[0]+integration_simpson_init(position_init[0], i, velocity_x, delta_t, nb_ech))
            position_y.append(position_init[1]+integration_simpson_init(position_init[1], i, velocity_y, delta_t, nb_ech))
            position_z.append(position_init[2]+integration_simpson_init(position_init[2], i, velocity_z, delta_t, nb_ech))
        if (i > 1):
            #ipdb.set_trace()
            velocity_x.append(velocity_x[i-1]+integration_simpson(i-1, i, vect_x, delta_t, nb_ech))
            velocity_y.append(velocity_y[i-1]+integration_simpson(i-1, i, vect_y, delta_t, nb_ech))
            velocity_z.append(velocity_z[i-1]+integration_simpson(i-1, i, vect_z, delta_t, nb_ech))

            position_x.append(position_x[i-1]+integration_simpson(i-1, i, velocity_x, delta_t, nb_ech))
            position_y.append(position_y[i-1]+integration_simpson(i-1, i, velocity_y, delta_t, nb_ech))
            position_z.append(position_z[i-1]+integration_simpson(i-1, i, velocity_z, delta_t, nb_ech))
    #ipdb.set_trace()
    #    print np.shape(position_x)
    #    print np.shape(position_y)
    velocity = np.array([velocity_x, velocity_y, velocity_z])
    position = np.array([position_x, position_y, position_z])
    return velocity, position

def integration_simpson(a, b, f, delta_t, nb_ech):
    h = (b-a)/np.double(nb_ech)
    z = np.double(f[a]+f[b])/6.
    for i in range(1,nb_ech) :
        z = z+f[np.int(a+i*h)]/3.
    for i in range(nb_ech) :
        z=z+f[np.int(a+(2.*i+1)*h/2.)]*2./3.

    val_int =  z*h
    val_int *= delta_t

    return val_int

def integration_simpson_init(val_init, b, f, delta_t, nb_ech):
    a = 0
    f_a = val_init
    h = (b-a)/np.double(nb_ech)
    z = np.double(f_a+f[b])/6.
    for i in range(1,nb_ech) :
        z = z+f[np.int(a+i*h)]/3.
    for i in range(nb_ech) :
        z=z+f[np.int(a+(2.*i+1)*h/2)]*2./3.

    val_int =z*h
    val_int *= delta_t

    return val_int
