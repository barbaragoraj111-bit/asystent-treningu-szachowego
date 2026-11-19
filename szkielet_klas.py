# ABC = Abstract Base Class, czyli abstrakcyjna klasa bazowa.
# Dzieki temu SesjaTreningowa bedzie tylko "szablonem" - nie bedzie ogolnej sesji,
# tylko zawsze konkretny rodzaj treningu jak w klasach dzieciach.
from abc import ABC

# KLASA BAZOWA czyli rodzic - tu trafia cechy wspolne dla kazdego treningu
# np. data, czas trwania w minutach, notatka
class SesjaTreningowa(ABC):
    pass


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