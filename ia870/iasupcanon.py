# -*- encoding: utf-8 -*-
# Module iasupcanon

from numpy import *

def iasupcanon(f, Iab, theta=45, DIRECTION="CLOCKWISE"):
    from ia870.iaintersec import iaintersec
    from ia870.iainterot import iainterot
    from ia870.iaunion import iaunion
    from ia870.iasupgen import iasupgen

    DIRECTION = DIRECTION.upper()
    y = iaintersec(f,0)
    for t in range(0,360,theta):
        Irot = iainterot( Iab, t, DIRECTION )
        y = iaunion( y, iasupgen(f, Irot))

    return y

