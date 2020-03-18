import unittest
import configparser
config = configparser.ConfigParser()
config.read("https://github.com/kolla233/DisneyDev/tree/master/prmFiles/abc.txt")
a = config.get("addition", "a")
b = config.get("addition", "b")
result= config.get("addition", "result")
num1 = int(a)
num2 = int(b)
result = int(result)
def add(num1,num2):
    return num1 + num2

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(add(num1,num2), result)

if __name__ == '__main__':
    unittest.main()