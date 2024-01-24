from pathlib import Path 
import os

if __name__ == '__main__':

    """
    try:
        tekst = open('small.txt', 'r')
        print(tekst.readline())
    except Exception as e:
        print(e)
    finally:
        tekst.close()
    """
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """


    def tekst_lesing(file_name):
        nabo_mappe = Path(__file__).resolve().parent.parent / 'tests'
        il_bane = nabo_mappe / file_name
        bok = []
        fil = open(il_bane,'r')
        for i in fil:
            bok.append(i)
        return bok
    

    def read_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    
    nabo_mappe = os.path.join(os.path.dirname(__file__), '..', 'tests')
    fil_bane = os.path.join(nabo_mappe, 'voluspaa.txt')
    read_file(fil_bane)