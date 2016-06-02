import unittest
from chuck import ChuckNorris


class ChuckNorrisTestCase(unittest.TestCase):

    def setUp(self):
        self.cn = ChuckNorris()

    def test_retrieve_jokes_random(self):
        data = self.cn.random()
        self.assertTrue('type' in data)
        self.assertEqual(data['type'], 'success')
        self.assertTrue('value' in data)
        self.assertTrue('id' in data['value'])
        self.assertTrue('joke' in data['value'])
        self.assertTrue('categories' in data['value'])

    def test_retrieve_jokes_by_id(self):
        data = self.cn.get_jokes_by_id(15)
        self.assertTrue('type' in data)
        self.assertEqual(data['type'], 'success')
        self.assertTrue('value' in data)
        self.assertTrue('id' in data['value'])
        self.assertTrue('joke' in data['value'])
        self.assertTrue('categories' in data['value'])
        self.assertEqual(data['value']['joke'], 'When Chuck Norris goes to donate blood, he declines the syringe, and instead requests a hand gun and a bucket.')

    def test_retrieve_jokes_categories(self):
        data = self.cn.get_jokes_categories()
        self.assertTrue('type' in data)
        self.assertTrue('value' in data)
        self.assertTrue(hasattr(data['value'], '__iter__'))

    def test_retrieve_jokes_count(self):
        data = self.cn.get_jokes_count()
        self.assertTrue('type' in data)
        self.assertEqual(data['type'], 'success')
        self.assertTrue('value' in data)
        self.assertTrue(isinstance(data['value'], int))

    def test_retrieve_jokes_random_3_records(self):
        data = self.cn.random(total=3)
        self.assertTrue('type' in data)
        self.assertEqual(data['type'], 'success')
        self.assertTrue('value' in data)
        self.assertTrue(hasattr(data['value'], '__iter__'))
        self.assertEqual(len(data['value']), 3)

    def test_retrieve_jokes_random_limit_category(self):
        data = self.cn.random(categories=['nerdy'])
        self.assertTrue('type' in data)
        self.assertEqual(data['type'], 'success')
        self.assertTrue('value' in data)
        self.assertEqual(data['value']['categories'][0], 'nerdy')

if __name__ == '__main__':
    unittest.main()
