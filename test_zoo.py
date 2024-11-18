import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.

    def test_C1b1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)

    def test_C1b2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_C1b3(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_C1b4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_C1b5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 200)

if __name__ == '__main__':
    unittest.main()