


#def read_file(file_name):
#        tekstfil = open(file_name, 'r')
#        print(tekstfil)






def read_file(file_name):
    tekstfil = []
    fil = open(file_name, 'r', encoding='utf-8')
    for i in fil:
        tekstfil.append(i.strip())
    return tekstfil



print(read_file('voluspaa.txt'))
#fil = read_file('voluspaa.txt')
#print(fil.read())
   
    




"""
def read_file(file_name):
    """
"""
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
"""
    tekststrenger = []
    
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                tekststrenger.append(line.strip('?!,."+-/\ ., \n 1 2 3 4 5 6 7 8 9 0'))
    except FileNotFoundError:
        print(f'Filen {file_name} ble ikke funnet.')
    for tommeOrd in tekststrenger:
        if tommeOrd == '':
            tekststrenger[len(tommeOrd)]
    return tekststrenger

# print(read_file('voluspaa.txt'))
"""