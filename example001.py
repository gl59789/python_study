
def print_monthly_expense(month, hours):
    monthly_expense = hours * 0.65
    print("In " + month + " we spent: " + str(monthly_expense))

print_monthly_expense("June", 243)
print_monthly_expense("July", 325)
print_monthly_expense("August", 298)



def rectangle_area(base, height):
    area = base * height  # the area is base*height
    print("The area is " + str(area))

rectangle_area(5, 6)


def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km

distance_in_km = convert_distance( 55 )
round_trip_in_km = distance_in_km * 2
print("The distance in kilometer is " + str(distance_in_km))
print("The round-trip in kilometer is " + str(round_trip_in_km))



def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


def number_group(number):
    if (number > 0 ):
        return "Positive"
    elif (number < 0):
        return "Negative"
    else:
        return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative


def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

print("A dog" + "A mouse")
print(9999+8888 + 100*100)



def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = int(filesize / block_size)
    # Use the modulo operator to check whether there's any remainder
    partial_block = filesize % block_size
    # Depending on whether there's a remainder or not, return the right number.
    if partial_block > 0:
        return full_blocks + 1
    return full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192


def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

print("big" > "small")


def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail



def format_name(first_name, last_name):
    if first_name !="" and last_name != "":# code goes here
        return "Name: " + last_name + ", " + last_name
    elif first_name !="" and last_name =="":
        return "Name: " + first_name
    elif first_name =="" and last_name !="":
        return "Name: " + last_name
    return '""'

print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""


def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) > len(word1) and len(word2) > len(word3):
        word = word2
    else:
        word = word3
    return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


def fractional_part(numerator, denominator):
    if denominator != 0:
        remainder = numerator % denominator
        fraction = remainder / denominator
        return fraction
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient
    return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

def count_down(start_number):
    current = start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)


def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        n += 1
print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3


def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            factor += 1# If it's not, increment the factor by one
    return "Done"

print_prime_factors(100) # Should print 2,2,5,5









def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False

def sum_divisors(n):
    divisor = 1
    sum = 0
    while n > divisor:
        if n % divisor == 0:
            sum += divisor
        divisor += 1

    # Return the sum of all divisors of n, not including n
    return sum

print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16

def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0 and n != 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    else:
        return False

print(is_power_of_two(0))



def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120



def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result

for n in range(10):
    print(n, factorial(n))


#Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
for x in range(1, 11):
    print (x**3)


for x in range(101):
    if (x % 7) == 0:
        print(x)


def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15



number = 1
while number <= 7:
    print(number, end=" ")
    number += 1


def show_letters(word):
    for x in word:
        print(x)

show_letters("Hello")
# Should print one line per letter



def digits(n):
    count = 0
    if n == 0:
        return 1
    while (int(n) > 0):
        count += 1
        n /= 10
    return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1



def multiplication_table(start, stop):
    for x in range(start, stop+1):
        for y in (range(start, stop+1)):
            print(str(x*y), end=" ")
        print()

multiplication_table(1, 3)
# Should print the multiplication table shown above



def counter(start, stop):
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x-= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x+= 1
    return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

for x in range(1, 10, 3):
    print(x)


for x in range(10):
    for y in range(x):
        print(y)


def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))




def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for x in input_string:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if x != " ":
            new_string += x.lower()
            reverse_string = "".join(reversed(new_string))
    # Compare the strings
    print(new_string, reverse_string)
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km



def group_list(group, users):
    members = ", ".join(users)
    return '"' + group + ": " + str(members) + '"'

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"



def skip_elements(elements):
    # code goes here
    index = 0
    return elements[::2]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print("{} is {} years old and works as {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])


def skip_elements(elements):
    # code goes here
    new_elements =[]
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_elements.append(element)
    return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

def skip_elements(elements):
    return [ element for element in elements if elements.index(element) % 2 == 0]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for filename in filenames:
    old_name = filename
    if filename.endswith(".hpp"):
        new_name = filename.replace(".hpp", ".h")
    else:
        new_name = old_name
    newfilename = (old_name, new_name)
    newfilenames.append(newfilename)
print (newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += "-"
    return result

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split(" ")
    for word in words:
        # Create the pig latin word and add it to the list
        new_word = word[1:] + word[0] + "ay"
        say = say + new_word + " "
        # Turn the list back into a phrase
    return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents?
print("Chapter 5" in toc) # Is there a Chapter 5?


cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, thing in cool_beasts.items():
    print("{} have {}".format(beast, thing))


wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for k, v in wardrobe.items():
    for color in v:
        print("{} {}".format(color, k))


def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user, domain))
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))




def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user in user_groups:
                user_groups[user].append(group)
            else:
                user_groups[user] = [group]

    # Now add the group to the the list of
    # groups for this user, creating the entry
    # in the dictionary if necessary

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"] }))



def format_address(address_string):
    # Declare variables
    addresses = []
    house_number = 0
    street_name = ""
    # Separate the address string into parts
    addresses = address_string.split(" ")
    # Traverse through the address parts
    for address in addresses:
    # Determine if the address part is the
    # house number or part of the street name
        if address.isnumeric():
            house_number = int(address)
        else:
            street_name = street_name + address + " "
    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"



def highlight_word(sentence, word):
    return sentence.replace(word, word.upper())

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))



def combine_lists(list1, list2):
# Generate a new list containing the elements of list2
# Followed by the elements of list1 in reverse order
    new_list1 = list1[::-1]
    for item in new_list1:
        list2.append(item)
    return list2

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


def squares(start, end):
    return [ x**2 for x in range(start, end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def car_listing(car_prices):
    result = ""
    for k, v in car_prices.items():
        result += "{} costs {} dollars".format(k, v) + "\n"
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))



def combine_guests(guests1, guests2):
# Combine both dictionaries into one, with each key listed
# only once, and the value from guests1 taking precedence
    for k, v in guests2.items():
        if k not in guests1.keys():
            guests1[k] = v
    return guests1
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))



def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text:
        # Check if the letter needs to be counted or not
        if letter.isalpha():
            if not letter.lower() in result:
                result[letter.lower()] = 1
            else:
                result[letter.lower()] += 1

            # Add or increment the value in the dictionary
    return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

print(colors)


host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())


class Flower:
    color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "violet"

this_pun_is_for_you = Flower()

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)


# “If you have an apple and I have an apple and we exchange these apples, then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    #"you" and "me" will exchange ALL our apples with one another
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples

def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another
    you.ideas += me.ideas
    me.ideas += you.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7

fido=Dog()
fido.years=3
print(fido.dog_years())

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name set.
        return "hi, my name is {}".format(self.name)

    # Create a new instance with a name of your choice
some_person = Person("Kevin")
# Call the greeting method
print(some_person.greeting())



class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        """Outputs a message with the name of the person"""
        print("Hello! My name is {name}.".format(name=self.name))




class Clothing:
    material = ""
    def __init__(self,name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))

class Shirt(Clothing):
    material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()



class Clothing:
    stock={ 'name': [],'material' :[], 'amount':[]}
    def __init__(self,name):
        material = ""
        self.name = name
    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)
    def Stock_by_Material(self, material):
        count=0
        n=0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n+=1
        return count

class shirt(Clothing):
    material="Cotton"
class pants(Clothing):
    material="Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
