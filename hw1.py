import data

# Write your functions for each part in the space below.

# Part 1
# Counts the amount of vowels
def vowel_count(word:str) -> int:
    count = 0
    #a list containing all the vowels to check
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    character = [y for y in word]

    #for loop checks for the while list
    for x in vowels:
        y = 0
        #runs through each character in the word checking its vowels then counting it
        while y < len(character):
            if x == character[y]:
                count += 1
            y += 1
    return count

# Part 2
#Checks the length of the list and only returns with a list of 2
def short_lists(list:list[list[int]]) -> list:
    len2 = []
    #Checks the length of the list
    for x in list:
        if len(x) == 2:
            len2.append(x)
    return len2

# Part 3
#Checks if the next pair is greater than the previous one then appends (Only length of 2)
def ascending_pairs(list:list[list[int]]) -> list:
    len2 = []
    for x in list:
        #Checks the length of the list and if the second value is an ascending value
        if len(x) == 2 and x[0] < x[1]:
            len2.append(x)
    return len2

# Part 4
from data import Price
#Adds the prices together and ensures that the cents stays within two places
def add_prices(price1, price2) -> Price:
    #Adds both prices together the dollars and cents
    totalDollars = price1.dollars + price2.dollars
    totalCents = price1.cents + price2.cents
    #Keeps only the first largest 2 values of the decimal, keeping it between two values
    while totalCents > 100:
        totalCents = totalCents // 10
    return Price(totalDollars, totalCents)


# Part 5
from data import Rectangle
#Obtains the area of the rectangle
def rectangle_area(rectangle:Rectangle) -> int:
    #Grabs both the length and width of the rectangle subtracting the two points from one another
    length = abs(rectangle.bottom_right.x - rectangle.top_left.x)
    width = abs(rectangle.bottom_right.y - rectangle.top_left.y)
    area = length * width
    return area

# Part 6
from data import Book
#Grabs the authors books
def books_by_author(name:str, books:list[Book]) -> list[Book]:
    authorsBooks = []
    #Begins by grabbing each book
    for x in books:
        #Then grabs the books authors
        for names in x.authors:
           #checks if the named asked for is equal then appends the books with authors name
           if name == names:
                authorsBooks.append(x.title)
    return authorsBooks

# Part 7
from data import Circle
from data import Point
#Grabs the circles center and radius size that encloses the rectangle
def circle_bound(rectangle:Rectangle) -> Circle:
    #Begins obtaining the radius using pythagoreom theorem
    hypotenuse = (((rectangle.bottom_right.x - rectangle.top_left.x) ** 2) + ((rectangle.bottom_right.y - rectangle.top_left.y) ** 2)) ** 0.5
    radius = hypotenuse / 2

    #Obtains the center point of the circle obtaining the size of top and side then dividing to get half
    centerx = (rectangle.bottom_right.x - rectangle.top_left.x) / 2
    centery = (rectangle.bottom_right.y - rectangle.top_left.y) / 2
    centerPoint = Point(centerx, centery)

    return Circle(centerPoint, radius)

# Part 8
from data import Employee
#Grabs the employees workers then releases the lowest paid workers
def below_pay_average(companyWorkers:list[Employee]) -> list[str]:
    #Begins by obtaining avg pay by adding all workers pay then dividing them
    avgPay = 0
    for worker in companyWorkers:
        avgPay += worker.pay_rate
    avgPay = avgPay // (len(companyWorkers))

    #Checks the workers that are under the avg pay amount by comparing their pay and releases them
    underpaidWorkers = []
    for worker in companyWorkers:
        if worker.pay_rate < avgPay:
            underpaidWorkers.append(worker.name)

    return underpaidWorkers



