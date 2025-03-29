# This file is part of Calculator_app.
#
# Calculator_app is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Calculator_app is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (c) 2025 Jan Kai Marek, xmarekj00

# mathlib.py - knihovna pro základní matematické operace

def add(a, b):
    """
    Funkce pro sečítání dvou čísel.

    Parametry:
    a (int, float): První číslo.
    b (int, float): Druhé číslo.

    Návratová hodnota:
    int, float: Součet dvou čísel.
    """
    pass  # Implementace sčítání zde


def subtract(a, b):
    """
    Funkce pro odčítání druhého čísla od prvního.

    Parametry:
    a (int, float): První číslo.
    b (int, float): Druhé číslo.

    Návratová hodnota:
    int, float: Rozdíl mezi dvěma čísly.
    """
    pass  # Implementace odčítání zde


def multiply(a, b):
    """
    Funkce pro násobení dvou čísel.

    Parametry:
    a (int, float): První číslo.
    b (int, float): Druhé číslo.

    Návratová hodnota:
    int, float: Součin dvou čísel.
    """
    pass  # Implementace násobení zde


def divide(a, b):
    """
    Funkce pro dělení prvního čísla druhým.

    Parametry:
    a (int, float): Dělenec.
    b (int, float): Dělitel.

    Návratová hodnota:
    int, float: Výsledek dělení.

    Výjimka:
    ZeroDivisionError: Pokud je dělitel roven nule.
    """
    pass  # Implementace dělení zde


def divide_with_remainder(a, b):
    """
    Funkce pro dělení prvního čísla druhým se zbytkem.

    Parametry:
    a (int): Dělenec (musí být celé číslo).
    b (int): Dělitel (musí být celé číslo).

    Návratová hodnota:
    tuple: Dvojice (quotient, remainder), kde quotient je celočíselný podíl a remainder je zbytek.

    Výjimka:
    ZeroDivisionError: Pokud je dělitel roven nule.
    """
    pass  # Implementace dělení se zbytkem zde


def factorial(n):
    """
    Funkce pro výpočet faktoriálu zadaného čísla.

    Parametry:
    n (int): Číslo, jehož faktoriál chceme spočítat. Číslo musí být nezáporné.

    Návratová hodnota:
    int: Faktoriál čísla.

    Výjimka:
    ValueError: Pokud je n záporné číslo.
    """
    pass  # Implementace faktoriálu zde


def power(base, exponent):
    """
    Funkce pro umocnění základu na zadaný exponent.

    Parametry:
    base (int, float): Základ umocnění.
    exponent (int): Exponent, musí být celé číslo (přirozené číslo).

    Návratová hodnota:
    int, float: Výsledek umocnění.
    """
    pass  # Implementace umocnění zde


def sqrt(x, degree=1):
    """
    Funkce pro výpočet odmocniny zadaného čísla s podporou odmocnitele.

    Parametry:
    x (int, float): Číslo, ze kterého chceme spočítat odmocninu.
    degree (int): Odmocnitel, který určuje, zda se jedná o druhou odmocninu (degree=1) nebo jiný typ odmocniny (degree != 1).

    Návratová hodnota:
    float: Výsledek výpočtu odmocniny s uvedeným odmocnitelem.

    Výjimka:
    ValueError: Pokud je x záporné číslo a není žádána komplexní odmocnina, nebo pokud odmocnitel není platný.
    """

    pass  # Implementace odmocniny zde


