import unittest , re ,numpy

def filterNumber(text):
    phones = re.findall(r'\+966\d{9}', text)
    if phones :
        return phones[0]
    else :
        return numpy.NaN
    
class TestArrayFunctions(unittest.TestCase):
    def test_filterNumber(self):
        self.assertEqual(filterNumber("+966503994473⁩"),"+966503994473")
        self.assertEqual(filterNumber("""+966506293960⁩
"""),"+966506293960")
        self.assertEqual(filterNumber("+966503610000"),"+966503610000")
        self.assertEqual(filterNumber("+966591238800⁩"),"+966591238800")
        self.assertEqual(filterNumber("+966537244555"),"+966537244555")
        # self.assertEqual(filterNumber("+96653724455"),numpy.NaN)
        self.assertEqual(filterNumber("+9665372445550"),"+966537244555")



if __name__ == "__main__":
    print(numpy.nan)
    try:
        unittest.main()
    except SystemExit:
        pass
