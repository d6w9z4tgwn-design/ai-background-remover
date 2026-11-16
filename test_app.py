import unittest
from app import output_path
class Test(unittest.TestCase):
 def test_name(self): self.assertEqual(output_path('a.jpg','out').name,'a_transparent.png')
