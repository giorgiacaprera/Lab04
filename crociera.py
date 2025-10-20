from cabina import Cabina
from cabinaAnimali import CabinaAnimali
from cabinaDeluxe import CabinaDeluxe
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.cabine = {}
        self.passeggeri = {}

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
        try:
            with open(file_path, 'r') as file:
                for riga in file:
                    campi = riga.strip().split(',')
                    if campi[0].startswith('CAB'):
                        codice, letti, ponte, prezzo = campi[:4]
                        if len(campi) == 4:
                            cabina = Cabina(codice, letti, ponte, prezzo)
                        elif len(campi) == 5:
                            extra = campi[4]
                            if extra.isdigit():
                                cabina = CabinaAnimali(codice, letti, ponte, prezzo, extra)
                            else:
                                cabina = CabinaDeluxe(codice, letti, ponte, prezzo, extra)
                        else:
                            raise ValueError('Formato cabina non valido')
                        self.cabine[codice] = cabina
                    elif campi[0].startswith('P'):
                        codice, nome, cognome = campi
                        passeggero = Passeggero(codice, nome, cognome)
                        self.passeggeri[codice] = passeggero
        except FileNotFoundError:
            print(f'File {file_path} non esiste')

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        if codice_cabina not in self.cabine:
            raise ValueError(f'Cabina {codice_cabina} non trovata')
        if codice_passeggero not in self.passeggeri:
            raise ValueError(f'Passeggero non trovato')
        cabina = self.cabine[codice_cabina]
        passeggero = self.passeggeri[codice_passeggero]
        if not cabina.disponibile:
            raise Exception('Cabina non disponibile')
        if passeggero.cabina is not None:
            raise Exception('Il passeggero ha già una cabina')
        cabina.assegna_passeggero(passeggero)
        passeggero.assegna_cabina(cabina)

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        return sorted(self.cabine.values())

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for passeggero in self.passeggeri.values():
            print(passeggero)
