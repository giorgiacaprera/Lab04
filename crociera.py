import csv
from cabine import *
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.cabine = []
        self.passeggeri = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def name(self):
        return self._nome

    @name.setter
    def name(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        self.cabine.clear()
        self.passeggeri.clear()
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for riga in reader:
                    codice = riga[0]
                    if codice.startswith('CAB'):
                    # Gestione cabine
                        if len(riga) == 4:  # Cabina Base
                            cabina = Cabina(*riga)
                        elif len(riga) == 5:  # Cabina Animali o Deluxe
                        # Se è numerico -> cabina animali, se no deluxe
                            if riga[4].isdigit():
                                cabina = CabinaAnimali(riga[0], riga[1], riga[2], riga[3], riga[4])
                            else:
                                cabina = CabinaDeluxe(riga[0], riga[1], riga[2], riga[3], riga[4])
                        self.cabine.append(cabina)
                    elif codice.startswith('P'):
                        nome, cognome = riga[1:]
                        passeggero = Passeggero(codice, nome, cognome)
                        self.passeggeri.append(passeggero)
        except FileNotFoundError:
            print(f'File {file_path} non esiste')

    def _trova_cabina(self, codice):
        return next((c for c in self.cabine if c.codice == codice), None)

    def _trova_passeggero(self, codice):
        return next((p for p in self.passeggeri if p.codice == codice), None)

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        cabina = self._trova_cabina(codice_cabina)
        passeggero = self._trova_passeggero(codice_passeggero)

        if not cabina:
            raise Exception("Cabina non trovata.")
        if not passeggero:
            raise Exception("Passeggero non trovato.")
        if not cabina.disponibile:
            raise Exception("Cabina non disponibile.")
        for c in self.cabine:
            if passeggero == c.passeggero:
                raise Exception("Passeggero già associato ad una cabina.")

        cabina.assegna(passeggero)

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        return sorted(self.cabine)

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for p in self.passeggeri:
            res = f"- {p}"
            for c in self.cabine:
                if p == c.passeggero:
                    res = f"{res} --> Assegnato alla cabina: {c.codice}"
                    break
            print(res)