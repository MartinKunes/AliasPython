def voltage( U, R):

    result_I = U / R
    return result_I


def wats(I, R):
    result_U = I * R
    return result_U


def resistance(U, I):
    result_R = U / I
    return result_R


def Coulomb(Q1,Q2, r, er):
    eo = 8.854187817e-12
    e = eo * er
    sila = (1 / (4 * 3.14159265359 * e)) * (Q1 * Q2) / (r**2)
    return sila
