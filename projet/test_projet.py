import unittest
from main import surface_pizza, prix_par_cm2, analyser_pizzas

class TestPizza(unittest.TestCase):
    def test_surface_pizza_20_cm(self):
        self.assertAlmostEqual(surface_pizza(20), math_pi_100, places=10)

    def test_diametre_double_surface_x4(self):
        self.assertAlmostEqual(surface_pizza(40) / surface_pizza(20), 4.0)

    def test_prix_par_cm2(self):
        self.assertAlmostEqual(prix_par_cm2(10, 100), 0.1)

    def test_diametre_invalide(self):
        with self.assertRaises(ValueError):
            surface_pizza(0)

    def test_classement(self):
        pizzas = [
            {"nom": "A", "diametre": 20, "prix": 10},
            {"nom": "B", "diametre": 30, "prix": 12},
        ]
        resultat = analyser_pizzas(pizzas)
        self.assertEqual(resultat[0]["nom"], "B")

math_pi_100 = 3.141592653589793 * 100

if __name__ == "__main__":
    unittest.main()
