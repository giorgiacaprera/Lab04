class Cabina:
    def __init__(self, codice, letti, ponte, prezzoBase):
        self.codice = codice
        self.letti = int(letti)
        self.ponte = int(ponte)
        self.prezzoBase = float(prezzoBase)
        self.disponibile = True
        self.passeggero = None

    def prezzoFinale(self):
        return self.prezzoFinale

    def assegnaPasseggero(self, passeggero):
        if not self.disponibile:
            raise Exception('Cabina già occupata')
        self.passeggero = passeggero
        self.disponibile = False

    def __str__(self):
        stato = 'Disponibile' if self.disponibile else 'Occupata'
        return f'{self.codice}: Standard | {self.letti} - Ponte {self.ponte} - Prezzo {self.prezzoFinale()}€ - {stato}'

    def __lt__(self, other):
        return self.prezzoFinale() < other.prezzoFinale()