from pathlib import Path


def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    bok = []
    fil = open(file_name,'r')
    for i in fil:
         bok.append(i)
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open
    return bok  # TODO: Du må erstatte denne linjen


def main():
    pass

    

    

if __name__ == '__main__':
    main()
