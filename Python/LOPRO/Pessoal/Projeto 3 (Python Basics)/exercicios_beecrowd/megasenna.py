num = 1
ndois = 1
ntres = 1
nquatro = 1
ncinco = 1
nseis = 1
acumuladora = 0


while num <= 10:
    num += 1
    while ndois <= 10:
        ndois += 1
        if ndois == num:
            ndois += 1
        while ntres <= 10:
            ntres += 1
            if ntres == ndois or ntres == num:
                ntres += 1
            while nquatro <= 10:
                nquatro += 1
                if ntres == nquatro:
                    ntres += 1
                while ncinco <= 10:
                    ncinco += 1
                    if ncinco == nquatro:
                        nquatro += 1
                    while nseis <= 10:
                        nseis += 1
                        if nseis == ncinco:
                            nseis += 1
                            print(num, ndois, ntres, nquatro, ncinco, nseis)








