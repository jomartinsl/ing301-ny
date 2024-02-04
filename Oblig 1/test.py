
filnavn = 'tekst.txt'


def lese_fil(filnavn_):
    bok = []
    fil = open(filnavn_,'r')

    for i in fil:
        if i == '\n':
            bok.append(i)
    return bok



for i in lese_fil(filnavn):
    print(i)





