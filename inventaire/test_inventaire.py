import pytest
from inventaire import val, alerte, mouv, cout, classer, rot, par_cat, rapport, maj_prix, export_json

TEST_DICT = [{"q": 5, "pu": 1.00, "seuil": 10, "ref": "A", "cat": "cat1", "autre": 0}, {"q": 0, "pu": 0.00, "seuil": 5, "ref": "B", "cat": "cat2", "autre": 0}]


def test_val():
    assert val(TEST_DICT) == 5.00

def test_alerte():
    assert alerte(TEST_DICT)

def test_mouv():
    assert mouv(TEST_DICT[0], 3, "out", [], False, False)

def test_cout():
    assert cout(TEST_DICT[0]) == 28.00

def test_classer():
    assert classer(TEST_DICT) == sorted(TEST_DICT, key=lambda x: x["ref"])

def test_rot():
    assert rot(TEST_DICT, 2) == 0

def test_par_cat():
    assert par_cat(TEST_DICT)

def test_rapport():
    assert rapport(TEST_DICT, cat="cat1", seuil_min=1, export=False, verbose=False)

def test_maj_prix():
    assert maj_prix(TEST_DICT, "A") == None

def test_export_json():
    assert export_json(TEST_DICT, "test.json")






