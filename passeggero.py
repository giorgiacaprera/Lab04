class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina = None

    def __str__(self):
        stringa = self.cabina.codice if self.cabina else 'Nessuna cabina assenata'
        return f'{self.codice}: {self.nome} {self.cognome} - Cabina: {stringa}'

    def assegnaCabina(self, cabina):
        self.cabina = cabina