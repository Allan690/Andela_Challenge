import unittest
from triplecheck import Validator 

class TripleCheckTest(unittest.TestCase):
    def test_no_element_occurs_more_than_thrice(self):
        message ='Elements should not have a count greater than 3'
        result = Validator([5,5,5,5,4,4,4,3])
        self.assertNotEqual(message, result, msg ='No element should occur more than thrice')

    def test_empty_list(self):
        message ='List cannot be empty'
        result = Validator([])
        self.assertNotEqual(result, message, msg=message)

    def test_no_element_occurs_twice(self):
        message ='Elements must have a count of either 3 or 1'
        result = Validator([5,5,4,4,4,1])
        self.assertNotEqual(message,result,msg=message)

    def test_single_element_in_list(self):
        self.assertEqual(4, Validator([5, 3, 4, 3, 5, 5, 3]))

if __name__=='__main__':
    unittest.main()