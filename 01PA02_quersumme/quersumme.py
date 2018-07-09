def quersummen(n) :
    output =[]
    for b in range (2,n+1) :
        x = n
        coef = []
        while x // b >= 1:
            coef.append(x % b)
            x = x // b
        if x // b == 0 :
            coef.append(x % b)
        output.append(sum(coef))
    print(' '.join(str(e) for e in output))
        