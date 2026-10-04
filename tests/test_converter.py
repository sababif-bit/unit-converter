from src.converter import (
    kilometer_to_meter,
    kilogram_to_gram,
    meter_to_kilometer,
    gram_to_kilogram,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius
)

def test_kilometer_to_meter():
    assert kilometer_to_meter(1) == 1000
    assert kilometer_to_meter(0) == 0
    assert kilometer_to_meter(2.5) == 2500

def test_kilogram_to_gram():
    assert kilogram_to_gram(1) == 1000
    assert kilogram_to_gram(0) == 0
    assert kilogram_to_gram(2.5) == 2500

def test_meter_to_kilometer():
    assert meter_to_kilometer(1000) == 1
    assert meter_to_kilometer(0) == 0
    assert meter_to_kilometer(2500) == 2.5

def test_gram_to_kilogram():
    assert gram_to_kilogram(1000) == 1
    assert gram_to_kilogram(0) == 0
    assert gram_to_kilogram(2500) == 2.5

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40