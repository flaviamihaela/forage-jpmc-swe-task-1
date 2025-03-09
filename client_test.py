import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'top_bid': {'price': 120.48, 'size': 109}, 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'top_bid': {'price': 117.87, 'size': 81}, 'stock': 'DEF'}
        ]
        expected_prices = [(120.84, 119.775)]  # Midpoint prices
        for i, quote in enumerate(quotes):
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(price, expected_prices[i])
    
    def test_getRatio(self):
        self.assertEqual(getRatio(10, 5), 2)
        self.assertEqual(getRatio(5, 10), 0.5)
        self.assertEqual(getRatio(10, 0), None)  # Handle division by zero


if __name__ == '__main__':
    unittest.main()
