from cabina import Cabina

class CabinaAnimali(Cabina):
    def __init__(self, codice, letti, ponte, prezzoBase, maxAnimali):
        self.maxAnimali = int(maxAnimali)

        def prezzoFinale(self):
            return self.prezzoBase * (1 + 0.10 * self.maxAnimali)

        def __str__(self):
            stato = 'Disponibile' if self.disponibile else 'Occupata'
            return f'{self.codice}: Animali | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.prezzoFinale()}€ - Max animali: {self.maxAnimali}'
