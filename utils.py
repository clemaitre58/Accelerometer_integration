import numpy as np

def quat2matrot(q):
    """fonction de convertion permettant de calculer la matrice de rotation qui permet de remettre les données dans repère inertielle et non celle du capteur

    :q: TODO
    :returns: TODO

    """

    print(type(q[0]))
    r = q[0]
    i = q[1]
    j = q[2]
    k = q[3]


    m_r = np.ones((3, 3))

    m_r[0, 0] = 2 * (-j * j - k * k) + 1
    m_r[0, 1] = 2 * (i * j - r * k)
    m_r[0, 2] = 2 * (i * k + r * j)

    m_r[1, 0] = 2 * (i * j + r * k)
    m_r[1, 1] = 2 * (-i * i - k * k ) + 1
    m_r[1, 2] = 2 * (j * k - r * i)

    m_r[2, 0] = 2 * (i * k - r * j)
    m_r[2, 1] = 2 * (j * k + r * i)
    m_r[2, 2] = 2 * (-i * i - j * j) + 1

    return m_r

def process_all_q2mr(q0, q1, q2, q3):
    """traitement du tous les quaternions vers toutes matrices de rotations

    :q0: TODO
    :q1: TODO
    :q2: TODO
    :q3: TODO
    :returns: TODO

    """
    m_r = []
    np.array(m_r)
    for i in range(len(q1)):
        q = [q0[i], q1[i], q2[i], q3[i]]
        m_rtn = quat2matrot(q)
        m_r.append(m_rtn)

    return m_r


def calc_deltat(timestamp):
    """calcul des deltat exacte durant l'acquisition des données 

    :timestam: TODO
    :returns: TODO

    """
    tab_delta =  np.diff(timestamp)

    
    return tab_delta

def rep_boitier_inertiel(Ax, Ay, Az, q0, q1, q2, q3):
    """TODO: Docstring for rep_boitier_inertiel.

    :Ax: Acc lin x
    :Ay: Acc lin y
    :Az: Acc lin z
    :q0: quat q0
    :q1: quat q1
    :q2: quat q2
    :q3: quat q3
    :returns: array Ax, Ay, Az corrigé dans l'espace

    """
    Axi = []
    Ayi = []
    Azi = []

    A= []


    m_r = process_all_q2mr(q0, q1, q2, q3)
    np.array(Axi)
    np.array(Ayi)
    np.array(Azi)
    for i in range(len(Ax)):
        A = np.array([Ax[i], Ay[i], Az[i]])
        Ares = np.dot(m_r[i], A.T)
        Axi.append(Ares[0])
        Ayi.append(Ares[1])
        Azi.append(Ares[2])

    np.array(Axi)
    print(type(Axi))

    return Axi, Ayi, Azi
