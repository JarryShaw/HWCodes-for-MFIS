# -*- coding: utf-8 -*-

#求解不定方程
#求二元一次不定方程的特解

def binaryEquation(a=1, b=1, c=1):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise __import__('NTLExceptions').IntError

    if a < 0:   apn = -1;   a *= -1
    else:       apn = 1
    if b < 0:   bpn = -1;   b *= -1
    else:       bpn = 1
    if c < 0:   cpn = -1;   c *= -1
    else:       cpn = 1

    gcd = __import__('NTLGreatestCommonDivisor').greatestCommonDivisor(a, b)
    if (c % gcd != 0):   
        raise __import__('NTLExceptions').SolutionError
    else:
        mtp = c / gcd

    (s,t) = __import__('NTLBezoutEquation').bezoutEquation(a, b)
    x0 = s * mtp * apn * cpn;   y0 = t * mtp * bpn * cpn

    return x0, y0

if __name__ == '__main__':
    (x0,y0) = binaryEquation(7,24,-3)

    print 'The general solutions for \'7*x + 24*y = -3\' is (t∈Z)'
    print 'x = %d + 24*t' %x0
    print 'y = %d - 7*t' %y0
