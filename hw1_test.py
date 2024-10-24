import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def testUnitCaseOne_1(self):
        input = "Hello"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def testUnitCaseOne_2(self):
        input = "COnstitUtiOnAl"
        result = hw1.vowel_count(input)
        expected = 6
        self.assertEqual(expected, result)

    # Part 2
    def testUnitCaseTwo_1(self):
        input = [[1,2], [2,3,4], [3,4], [1]]
        result = hw1.short_lists(input)
        expected = [[1,2], [3,4]]
        self.assertEqual(expected, result)

    def testUnitCaseTwo_2(self):
        input = [[3,2,1], [2,3], [78,9], [1], [9,6], [2,34,567,8]]
        result = hw1.short_lists(input)
        expected = [[2,3], [78,9], [9,6]]
        self.assertEqual(expected, result)

    # Part 3
    def testUnitCaseThree_1(self):
        input = [[1,2], [3,2], [6,9]]
        result = hw1.ascending_pairs(input)
        expected = [[1,2], [6,9]]
        self.assertEqual(expected, result)

    def testUnitCaseThree_2(self):
        input = [[2,4], [78,2], [6,900],[-1,2], [32,4,9,7]]
        result = hw1.ascending_pairs(input)
        expected = [[2,4], [6,900], [-1,2]]
        self.assertEqual(expected, result)
    # Part 4
    from data import Price
    def testUnitCaseFour_1(self):
        input1 = self.Price(22,1234)
        input2 = self.Price(45, 2145)
        result = hw1.add_prices(input1, input2)
        expected = self.Price(67, 33)
        self.assertEqual(expected, result)

    def testUnitCaseFour_2(self):
        input1 = self.Price(90,1223454)
        input2 = self.Price(15,12145)
        result = hw1.add_prices(input1, input2)
        expected = self.Price(105, 24)
        self.assertEqual(expected, result)

    # Part 5
    from data import Rectangle
    from data import Point
    def testUnitCaseFive_1(self):
        input = self.Rectangle(self.Point(2,3),(self.Point(3,4)))
        result = hw1.rectangle_area(input)
        expected = 1
        self.assertEqual(expected, result)

    def testUnitCaseFive_2(self):
        input = self.Rectangle(self.Point(0,5),(self.Point(5,15)))
        result = hw1.rectangle_area(input)
        expected = 50
        self.assertEqual(expected, result)

    # Part 6
    from data import Book
    def testUnitCaseSix_1(self):
        authors = ["damien", "daniels"]
        listOfBooks = [self.Book(authors, "Ray Luis"), self.Book(authors, "Jon Wayne")]
        name = "damien"
        result = hw1.books_by_author(name, listOfBooks)
        expected = ["Ray Luis", "Jon Wayne"]
        self.assertEqual(expected, result)

    def testUnitCaseSix_2(self):
        authors1 = ["george", "daniels"]
        authors2 = ["john pork", "grace johnson"]
        authors3 = ["london", "george"]
        listOfBooks = [self.Book(authors1, "Gray Hound"), self.Book(authors2, "Jon Wayne"), self.Book(authors3, "Grimace Shake")]
        name = "george"
        result = hw1.books_by_author(name, listOfBooks)
        expected = ["Gray Hound", "Grimace Shake"]
        self.assertEqual(expected, result)

    # Part 7
    from data import Circle
    def testUnitCaseSeven_1(self):
        input = self.Rectangle(self.Point(0,0), self.Point(2,4))
        result = hw1.circle_bound(input)
        expected = self.Circle(self.Point(1.0,2.0), (20 ** 0.5) / 2)
        self.assertEqual(expected, result)

    def testUnitCaseSeven_2(self):
        input = self.Rectangle(self.Point(2,4), self.Point(8,10))
        result = hw1.circle_bound(input)
        expected = self.Circle(self.Point(3.0,3.0), (72 ** 0.5) / 2)
        self.assertEqual(expected, result)

    # Part 8
    from data import Employee
    def testUnitCasEight_1(self):
        input = [self.Employee("John Doe", 24), self.Employee("Jason Williams", 5), self.Employee("Dray", 4)]
        result = hw1.below_pay_average(input)
        expected = ["Jason Williams", "Dray"]
        self.assertEqual(expected, result)

    def testUnitCasEight_2(self):
        input = [self.Employee("Damian", 12), self.Employee("Fein Dragon", 21), self.Employee("Gamer", 23)]
        result = hw1.below_pay_average(input)
        expected = ["Damian"]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
