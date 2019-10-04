import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default weight of a product being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        '''tests the products stealability given some values for
        price and weight'''
        prod = Product('Test Product', weight=11, price=7)
        self.assertEqual(prod.stealability(), 'Kinda stealable')
        prod2 = Product('Test Product', weight=11, price=5)
        self.assertEqual(prod2.stealability(), 'Not so stealable...')
        prod3 = Product('Test Product', weight=1, price=11)
        self.assertEqual(prod3.stealability(), 'Very stealable')

    def test_errors(self):
        '''tests that bad data passed to product returns an error'''
        self.assertRaises(TypeError, Product, 5)
        self.assertRaises(TypeError, Product, 'test', price='four')
        self.assertRaises(TypeError, Product, 'test', weight='four')
        self.assertRaises(TypeError, Product, 'test', flammability='four')
        self.assertRaises(TypeError, Product, 'test', identifier='four')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme Reporting is up to standard"""

    def test_default_num_products(self):
        """ tests the default number of products is 30"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """tests that product names are legal"""
        products = generate_products()
        for i in range(len(products)):
            nameSplit = products[i].name.split()
            self.assertIn(nameSplit[0], ADJECTIVES)
            self.assertIn(nameSplit[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
