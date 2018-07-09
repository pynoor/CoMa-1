def steigungsverhalten(a, b, c, d, x_0):

    """
    # Diese Funktion berechnet die erste und zweite Ableitung einer Funktion
    # f = ax^3 + bx^2 + cx + d im Punkt x_0 
    # Weiterhin prüft sie ob die Funktion an x_0 steigt, fällt oder einen 
    # kritischen Punkt in x_0 hat.
    # Gilt dazu f'(x_0) > 0 (f'(x_0) < 0) so gibt die Funktion aus dass f 
    # an x_0 steigt (fällt).
    # Gilt aber f'(x_0) = o, so hat f in x_0 einen kritischen Punkt.
    # Gilt ferner dass f''(x_0) < 0 (f''(x_0) > 0) ist, so gibt die Funktion aus, dass f in 
    #x_0 in lokales Maximum (Minimum) hat.
    # Gilt zuletzt jedoch weder f''(x_0) < 0 noch f''(x_0) > 0, so gibt die
    #Funktion aus dass f in x_0 einen kritischen Punkt unbekannten Typs hat.
    
    """

    f = a * (x_0 ** 3) + b * (x_0 ** 2) + c * x_0 + d
    df = 3 * a * (x_0 ** 2) + 2 * b * x_0 + c
    d2f = 6 * a * x_0 + 2 * b

    if df < 0 :
        print ("An der Stelle " + str(x_0) + " fällt die Funktion.")
    elif df > 0 :
        print ("An der Stelle " + str(x_0) + " steigt die Funktion.")
    elif df == 0 :
        if d2f < 0 :
            print("An der Stelle " + str(x_0) + " hat die Funktion ein lokales Maximum.")
        elif d2f > 0 :
            print ("An der Stelle " + str(x_0) + " hat die Funktion ein lokales Minimum.")
        else :
            print ("An der Stelle " + str(x_0) + " hat die Funktion einen kritischen Punkt unbekannten Typs.")

