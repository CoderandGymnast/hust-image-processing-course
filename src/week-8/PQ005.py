'''
[NOTE]: 
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
'''

from scipy.spatial import distance

import unittest

class TestDistanceMethods(unittest.TestCase):

    def test_Manhattan_001(self):
        a,b=[[0,0]],[[24, 7]]
        self.assertEqual(distance.cdist(a,b,"cityblock"), 31.)

    def test_Manhattan_002(self):
        a,b=[[24,7]],[[3,3]]
        self.assertEqual(distance.cdist(a,b,"cityblock"), 25.)
        
    def test_Chessboard_001(self):
        a,b=[[0,0]],[[24, 7]]
        self.assertEqual(distance.cdist(a,b, 'chebyshev'),24.)
        
    def test_Chessboard_002(self):
        a,b=[[24,7]],[[3,3]]
        self.assertEqual(distance.cdist(a,b,"chebyshev"), 21.)
if __name__ == '__main__':
    unittest.main()

