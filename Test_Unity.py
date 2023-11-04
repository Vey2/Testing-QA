import unittest
from main import hitung_jumlah_ganjil

class TestHitungJumlahGanjil(unittest.TestCase):

    def test_hitung_jumlah_ganjil_1(self):
        self.assertEqual(hitung_jumlah_ganjil(5), 9)

    def test_hitung_jumlah_ganjil_2(self):
        self.assertEqual(hitung_jumlah_ganjil(10), 25)

    def test_hitung_jumlah_ganjil_3(self):
        self.assertEqual(hitung_jumlah_ganjil(0), 0)

if __name__ == '__main__':
    unittest.main()
