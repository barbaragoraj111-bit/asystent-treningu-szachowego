# ABC = Abstract Base Class, czyli abstrakcyjna klasa bazowa.
# Dzieki temu SesjaTreningowa bedzie tylko "szablonem" - nie bedzie ogolnej sesji,
# tylko zawsze konkretny rodzaj treningu jak w klasach dzieciach.
from abc import ABC

# KLASA BAZOWA czyli rodzic - tu trafia cechy wspolne dla kazdego treningu
# np. data, czas trwania w minutach, notatka
# powinna miecto co inne klasy: czas treningu, date, mozliwosc notatki o treningu
class SesjaTreningowa(ABC):
    pass
# to bedzie KOMPOZYCJA, ani nie jest rodzicem ani nie dziedziczy po nim
class Ksiazka:
    def __init__(self, tytul: str, jednostka: str, cel: int): # jednostka to dla partii komentowanych strony, dla taktyki zadania, a cel ile stron lub zadan w ksiazce
        if cel <= 0:
            raise ValueError("Cel musi byc wiekszy od 0.")

        self.tytul = tytul
        self.jednostka = jednostka
        self.cel = cel
        self.przerobione = 0

    def dodaj_progres(self, ilosc: int): #ta do tej funkcji daje sie ilosc czyli ile danego dnia sie zrobilo zadan lub stron np. 13
        if ilosc <= 0:
            raise ValueError("Dodawany progres musi byc wiekszy od 0.")
        self.przerobione = min(self.cel, self.przerobione + ilosc)

    def ustaw_progres(self, aktualna_pozycja: int): #ta funkcja bierze na ktorym sie jest obecnie zadaniu lub ktorej sie jest stronie
        if aktualna_pozycja < 0 or aktualna_pozycja > self.cel:
            raise ValueError(f"Pozycja musi byc miedzy 0 a {self.cel}.")

        self.przerobione = aktualna_pozycja

    def pozostalo(self) -> int:
        return self.cel - self.przerobione

    def procent_ukonczenia(self) -> float:
        return round((self.przerobione / self.cel) * 100, 1)

    def __str__(self) -> str:
        return (
            f"{self.tytul}: {self.przerobione}/{self.cel} "
            f"{self.jednostka} ({self.procent_ukonczenia()}%)"
        )

# KLASY POCHODNE, czyli dzieci - dziedzicza po SesjaTreningowa, co oznacza, ze
# automatycznie przejmuja jej wspolne cechy, nie bede ich juz dodawala osobno w tych klasach
# w srodku kazdej klasy dziecko tylko to, co jest specyficzne dla danego treningu.

class Debiuty(SesjaTreningowa):
    pass

class ZadaniaTaktyka(SesjaTreningowa):
    pass

class ZadaniaGraPozycyjna(SesjaTreningowa):
    pass

class ZadaniaKoncowki(SesjaTreningowa):
    pass

class PartieSkomentowane(SesjaTreningowa):
    pass

class PartieTreningowe(SesjaTreningowa):
    pass

class Turniej(SesjaTreningowa):
    pass