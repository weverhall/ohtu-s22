import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "mehu", 6)
            if tuote_id == 3:
                return Tuote(3, "kahvi", 10)
            
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_tilimaksu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("ellak", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_tilisiirto(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("ellak", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("ellak", 42, "12345", "33333-44455", 5)

    def test_tilisiirto_usealla_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("ellak", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("ellak", 42, "12345", "33333-44455", 22)

    def test_tilisiirto_varastossa_olevalla_ja_puuttuvalla_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("ellak", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("ellak", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_metodin_kutsuminen_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("ellak", "12345")
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("ellak", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("ellak", 42, "12345", "33333-44455", 6)

    def test_tuotteen_poistaminen_ostoskorista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("ellak", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("ellak", 42, "12345", "33333-44455", 6)
