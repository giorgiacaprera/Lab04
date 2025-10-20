from cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzoBase, stile):
        self.stile = stile

    def prezzoFinale(self):
        return self.prezzoBase * 1.20

    def __str__(self):
        stato = 'Disponibile' if self.disponibile else 'Occupata'
        return f'{self.codice}: Deluxe {self.stile} | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.prezzoFinale()} - {stato}'
