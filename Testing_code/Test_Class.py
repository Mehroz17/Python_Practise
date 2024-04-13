import unittest
from GetName import name
class testing(unittest.TestCase):

    def test_function(self):
        for_name = name("muhammad","mehroz")
        self.assertEqual(for_name,"Muhammad Mehroz")

        for_name2 = name("Arif","Ahmed")
        self.assertEqual(for_name2,"Arif Ali")


if __name__ == "__main__":
    unittest.main()