import unittest
from recommender import load_movies, recommend, tokenize

class RecommenderTests(unittest.TestCase):
    def test_tokenization(self):
        self.assertEqual(tokenize('Space, SPACE!'), ['space', 'space'])

    def test_dataset_loads(self):
        self.assertEqual(len(load_movies()), 30)

    def test_space_recommendation(self):
        titles = [movie['title'] for _, movie in recommend('space astronaut mission')]
        self.assertIn('Orbit Rescue', titles)

    def test_exclusion(self):
        titles = [movie['title'] for _, movie in recommend('space astronaut mission', exclude_title='Orbit Rescue')]
        self.assertNotIn('Orbit Rescue', titles)

    def test_empty_query(self):
        with self.assertRaises(ValueError):
            recommend('  ')

    def test_zero_matches(self):
        self.assertEqual(recommend('zzzzunknownword'), [])

if __name__ == '__main__':
    unittest.main()
