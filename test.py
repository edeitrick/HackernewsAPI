import unittest
from hackernews import getRecentNewsID, getRecentNewsStory, convertToDataframe


class Test(unittest.TestCase):
    def test_getRecentNewsID(self):
        self.assertAlmostEqual(getRecentNewsID(), 27694114, delta = 70000)
    
    
    def test_getRecentNewsStory(self):
        story = getRecentNewsStory(getRecentNewsID())
        self.assertEqual(len(story), 8)
        
    def test_convertToDataframe(self):
        story = getRecentNewsStory(getRecentNewsID())
        datfr = convertToDataframe(story)
        desc = datfr[0]['descendants']
        self.assertEqual(desc, 0)


if __name__ == '__main__':
    unittest.main()
