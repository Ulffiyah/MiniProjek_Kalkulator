
import unittest
from kalkulator import tambah, kurang, kali, bagi


class TestKalkulator(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(tambah(10, 5), 15)

    def test_kurang(self):
        self.assertEqual(kurang(10, 5), 5)

    def test_kali(self):
        self.assertEqual(kali(10, 5), 50)

    def test_bagi(self):
        self.assertEqual(bagi(10, 5), 2)

    def test_bagi_dengan_nol(self):
        with self.assertRaises(ValueError):
            bagi(10, 0)


if __name__ == "__main__":
    unittest.main()
