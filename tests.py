import unittest
from chuck import ChuckNorris


class ChuckNorrisTestCase(unittest.TestCase):

    def setUp(self):
        self.cn = ChuckNorris()

    def test_retrieve_jokes_random(self):
        data = self.cn.random()
        self.assertIsNotNone(data)
        self.assertIsNotNone(data.id)
        self.assertIsNotNone(data.joke)
        self.assertIsNotNone(data.categories)
        self.assertTrue(isinstance(data.categories, list))

    def test_retrieve_jokes_by_id(self):
        data = self.cn.get_jokes_by_id(15)
        self.assertIsNotNone(data)
        self.assertIsNotNone(data.id)
        self.assertIsNotNone(data.joke)
        self.assertIsNotNone(data.categories)
        self.assertTrue(isinstance(data.categories, list))
        self.assertEqual(data.id, 15)
        self.assertEqual(data.joke, 'When Chuck Norris goes to donate blood, he declines the syringe, and instead requests a hand gun and a bucket.')

    def test_retrieve_jokes_categories(self):
        data = self.cn.get_jokes_categories()
        self.assertTrue(isinstance(data, list))

    def test_retrieve_jokes_count(self):
        data = self.cn.get_jokes_count()
        self.assertTrue(isinstance(data, int))

    def test_retrieve_jokes_random_3_records(self):
        data = self.cn.random(total=3)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 3)
        for i in data:
            self.assertIsNotNone(i)
            self.assertIsNotNone(i.id)
            self.assertIsNotNone(i.joke)
            self.assertIsNotNone(i.categories)

    def test_retrieve_jokes_random_limit_category(self):
        data = self.cn.random(categories=['nerdy'])
        self.assertIsNotNone(data)
        self.assertIsNotNone(data.id)
        self.assertIsNotNone(data.joke)
        self.assertIsNotNone(data.categories)
        self.assertEqual(data.categories[0], 'nerdy')


if __name__ == '__main__':
    unittest.main()
