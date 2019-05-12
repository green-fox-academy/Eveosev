"""
    Exercises in Function
"""
#Doubling
base_num = 123
def doubling(num):
    num *= 2
    return num
db_num = doubling(base_num)
print(f"The double of {base_num} is {db_num}")

#Greeter function
al = "Greenfox"
def greet(x):
    print(f"Greetings, dear {x}")
greet(al)

#Append a func
typo = "Chinchill"
def append_a_func(x):
    new_x = x + "a"
    return new_x
typo_add = append_a_func(typo)
print(f"{typo_add}")

#Summing
parameter = int(input("Please input a number: "))
def sum(x, initial = 0):
    for i in range(x + 1):
        initial += i
    return initial
print(f"The sum from 0 to {parameter} is {sum(parameter)}")

#Factorio
num_factorio = int(input("Please input a integer: "))
def factorio(x):
    for i in range(x + 1):
        i *= i
    return i
anwser = factorio(num_factorio)
print(f"The {num_factorio}'s fatororial is {anwser}")

#Print arguments
def print_params(*args):
    print(f"{args}")
print_params(1,2,3,4,5,"hi")

#Subint
param = input("Please input a number: ")
def subint(x, listdata = [1, 11, 34, 52, 61], count = []):
    for i in range(len(listdata)):
        if x in str(listdata[i]): count.append(i)
    return count
indeces = subint(param)
print(f"{indeces}")

#Unique
def unique(x):
    uni = set(x)
    return(uni)
print(unique([1, 11, 34, 11, 52, 61, 1, 34]))

#Anagram
input1 = input("Please input a string word: ")
input2 = input("Please input a string word: ")
def anagram(x, y):
    consequence = input1 == input2[::-1]
    return consequence
answer1 = anagram(input1, input2)
print(f"{answer1}")

#Palindrome builder
input3 = input("Please input a  string word: ")
def palindrome(x):
    palindrome_x = x + x[::-1]
    return palindrome_x
answer3 = palindrome(input3)
print(f"{answer3}")

#Palindrome Search
def search_palindrome(x, count = []):
    for i in range(3, len(x) + 1):
            

#Sort the list
def bubble(x):
    y = sorted(x)
    return y
print(bubble([1, 2, 4, 3]))

def advanced_bubble(x, T = True):
    x = sorted(x, reverse = T)
    return x
print(advanced_bubble([1,2,3,4,5,3]))

"""
    Data structure
"""

#Simple replace
example = "In a dishwasher far far away"
e_list = example.split()
e_list[e_list.index("dishwasher")] = "galaxy"
example =" ".join(str(i) for i in e_list)
print(str(example))

#url fixer
url = "https//www.reddit.com/r/nevertellmethebots"
url.replace("bots","odds")
url = url[:5] + ":" + url[5:]
print(url)

#Takes longers
quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
quote = quote[:quote.index("It") + 2] + " always takes longer than" + quote[quote.index("It") + 2:]
print(quote)

#Todo print
todoText = "- Buy milk\n"
todoText = todoText + "- Download games\n" + "  - Diablo"
print(todoText)

#Reverse
def reverse(x):
    x = x[::-1]
    return x

reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
print(reverse(reversed))

#List introduction 1
list_intro = []
def check(x):
    if len(x) == 0: print("The list is empty")
    else: print(f"There are/is {len(x)} element(s) in the list") 
check(list_intro)
list_intro.append("William")
check(list_intro)
list_intro.append("John")
list_intro.append("Amanda")
check(list_intro)
list_intro[2]
for i in list_intro:
    print(i)

for i in range(len(list_intro)):
    print(str(i+1) + ". " + list_intro[i])

list_intro.remove("John")
list_intro = list_intro[::-1]
for i in list_intro:
    print(i)

list_intro = []

#Map introduction
map1 = {}
def map_check(x):
    if len(x) == 0: print("The map is empty")
    else: print("The map is not empty")
map_check(map1)

map1["97"] = "a"
map1["98"] = "b"
map1["99"] = "c"
map1["65"] = "A"
map1["66"] = "B"
map1["67"] = "C"

for key in map1:
    print(f"{key}")

print(map1["99"] + " is associated with key 99")
del map1["97"]

if "100" in key:
    print("There is an associated value with key '100'")
else: print("There is no associated value with key '199'")
map1 = {}

#List introduction 2
A = ['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']
B = ['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']
A.remove('Durian')
A.append('Kiwifruit')
if len(A) == len(B):
    print("List A has the same size as List B")
else: print("The sizes of List A and List B are different")
A.index("Avocado")
B.index("Durian")
B.append("Passion Fruit and Pummelo")
A[2]

#Map introduction 2
map2 = {}
map2["978-1-60309-452-8"] = "A Letter to Jo"
map2["978-1-60309-459-7"] = "Lupus"
map2["978-1-60309-444-3"] = "Red Panda and Moon Bear"
map2["978-1-60309-461-0"] = "The Lab"
for key in map2:
    print(f"{map2[key]} (ISBM: {key})")

del map2["978-1-60309-444-3"]

def deleteKeyFromValue(x):
  for key in map2:
    if map2[key] == x:
        del map2[key]
        break
deleteKeyFromValue("The Lab")

map2["978-1-60309-450-4"] = "They Called Us Enemy"
map2["978-1-60309-453-5"] = "Why Did We Trust Him?"

def value_check(x):
    if x not in key: print(f"The key {x} is not in the map")
    elif map2[x] != "": 
        print(f"The value {map2[x]} is associated to the key {x}")
    else:
        print(f"There is no associated value with key {x} ")

value_check("478-0-61159-424-8")
print(f"The value associated with key '978-1-60309-453-5' is {map2['978-1-60309-453-5']}")

#Personal Finance
list_PF = [500, 1000, 1250, 175, 800, 120]

def sum_PF(x, initial = 0):
  for i in range(len(x)):
     initial += x[i]
  return initial
spend = sum_PF(list_PF)
print(f"We spend {spend}")

max_PF = max(list_PF) 
print(f"Our greatest expense is {max_PF}")

min_PF = min(list_PF)
print(f"Our cheapest spending is {min_PF}")

ave_PF = spend / len(list_PF)
print(f"The average amount of our spendings is {ave_PF}")

#Telephone book
phone_book = {}
phone_book["William A. Lathan"] = "405-709-1865"
phone_book["John K. Miller"] = "402-247-8568"
phone_book["Hortensia E. Foster"] = "606-481-6467"
phone_book["Amanda D. Newland"] = "319-243-5613"
phone_book["Brooke P. Askew"] = "307-687-2982"

print(f"John K. Miller's phone number is {phone_book['John K. Miller']}")

def findKeyFromValue(x):
  for key in phone_book:
    if phone_book[key] == x:
        print(f"{key}'s phone number is {x}")
        break
findKeyFromValue("307-687-2982")

def checknumber(x):
    if x not in phone_book:
        print(f"{x} is not in our phone book")
    else:
        print(f"{x}'s phone number is {phone_book[x]}")
checknumber("Chris E. Myers")

#Shopping list
list_shopping = ['eggs', 'milk', 'fish', 'apples', 'bread', 'chicken']
if "milk" in list_shopping:
    print("milk is on the list")
else:
    print("milk in not on the list")
    
if "banana" in list_shopping:
    print("banana is on the list")
else:
    print("banana in not on the list")
  
#Product database
product = {}
product["eggs"] = 200
product["milk"] = 200
product["fish"] = 400
product["apples"] = 150
product["bread"] = 50
product["chicken"] = 550

print(f"The fish costs {product['fish']}")

expensiveproduct = max(product, key = product.get)
print(f"The most expensive product is {expensiveproduct}")

def averagecost(x, initial = 0):
    for key in x:
        initial = x[key] + initial
    ave_product = initial / len(x)
    return ave_product
print(averagecost(product))

def count(x, y, c = 0):
    for key in x:
        if x[key] < y: c += 1
    return c
n = count(product, 300)
print(f"There are(is) {n} product's price below 300")

v = product.values()
if 125 in v:
    print("We can not buy anything for exactly 125")
else:
    print("We can buy something for exactly 125")
    
def findKeyFromValue_p(x):
  for key in product:
    if product[key] == x:
        print(f"The cheapest product is {key}")
        break
findKeyFromValue_p(min(v))

#Product database 2
product = {}
product["eggs"] = 200
product["milk"] = 200
product["fish"] = 400
product["apples"] = 150
product["bread"] = 50
product["chicken"] = 550

def findlower(x, y):
    print(f"The following products cost less than {y}")
    for key in x:
        if x[key] < y:
            print(f"{key}")
            
n = findlower(product, 201)

def findhigher(x, y):
    print(f"The following products cost more than {y}")
    for key in x:
        if x[key] > y:
            print(f"{key}")
            
n = findhigher(product, 150)

#Shopping list 2
product2 = {}
product2['milk'] = 1.07
product2['rice'] = 1.59
product2['eggs'] = 3.14
product2['cheese'] = 12.60
product2['chicken breasts'] = 9.40
product2['apples'] = 2.31
product2['tomato'] = 2.58
product2['potato'] = 1.75
product2['onion'] = 1.10 

Bob = {}
Bob['milk'] = 3
Bob['rice'] = 2
Bob['eggs'] = 2
Bob['cheese'] = 1
Bob['chicken breasts'] = 4
Bob['apples'] = 1
Bob['tomato'] = 2
Bob['potato'] = 1

Alice = {}
Alice['rice'] = 1
Alice['eggs'] = 5
Alice['chicken breasts'] = 2
Alice['apples'] = 1
Alice['tomato'] = 10

def sumpay(x, y):
    initial = 0
    for key in x:
        initial = x[key] * y[key] + initial
    return initial
print(f"Bob pay {sumpay(Bob, product2)}")
print(f"Alice pay {sumpay(Alice, product2)}")

if 'rice' in Bob and 'rice' in Alice:
    print("Both Bob and Alice bought rice")
elif 'rice' in Bob and 'rice' not in Alice:
    print("Bob bought rice")
elif 'rice' not in Bob and 'rice' in Alice:
    print('Alice bought rice')
else:
    print("Both of Bob and Alice did not bought rice")   

if Bob['potato'] > Alice['potato']:
    print("Bob bought more potato")
elif Bob['potato'] < Alice['potato']:
    print("Alice bought more potato")
else:
    print("Bob and Alice bought the same number of potato")

if len(Bob) > len(Alice):
    print("Bob bought more different products")
elif len(Bob) < len(Alice):
    print("Alice bought more different products")
else:
    print("Alice and Bob bought the same")

if sum(list(Bob.values())) > sum(list(Alice.values())):
    print("Bob bought more products")
elif sum(list(Bob.values())) < sum(list(Alice.values())):
    print("Alice bought more products")
else:
    print("Alice and Bob bought the same number of products")

#To extract values in a dictionary, we can use list(map.values())











