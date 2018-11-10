'''
Import unittest and simple_one modules
'''
import unittest
import simple_one

class TestSimpleOne(unittest.TestCase):
    '''
    Unit test for simple_one.py
    '''
    def test_one_word(self):
        '''
        Test one word
        '''
        text = 'python'
        result = simple_one.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multi_words(self):
        '''
        Test multiple words
        '''
        text = 'monty python'
        result = simple_one.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
