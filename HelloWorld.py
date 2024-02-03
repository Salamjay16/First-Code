#print("hello world")  
#print("salam-jay")

#red_bucket = "salam-jay"
#print(red_bucket)

#red_bucket = input("what do you want to put in the bucket")
#print(red_bucket)

#print(2!=8)
#print(4<5)
#print(7>9)
#print(2>3)
#print(3<=5)

#salam_age = 28  
#Age_for_NYSC = 30


# if salam_age < Age_for_NYSC:
#    print("salam should still be an undergraduates")
# elif salam_age == Age_for_NYSC:
#    print("salam should be a graduate")
# else:
#    print("salam is too old for NYSC")    

#print("salam should still be an undergraduates")
#print("salam should still be an undergraduates")
#print("salam should still be an undergraduates")

#def print_salam():
    #text = "salam should still be an undergraduates"
    #print(text)
    #print(text)
    
    
#print_salam()    
#print_salam()  
#print_salam()  

#def school_age_calculator(age,name):
   # if age < 10:
    #    print("you should still be in primary school", name, "is only", age)
    #elif  age == 10:
     #   print("Graduated from primary school.", name, "is already", age)
    #else:
    #    print("what are you still doing in primary school\nYou should be in secondary school!") 
         
#school_age_calculator (8,"Abdulsalam")      
#school_age_calculator (10,"Jackson") 
#school_age_calculator (12,"salam-jay") 

#def add_ten_to_age(age):
 #   new_age = age + 10
 #   return new_age

#How_old_will_i_be = add_ten_to_age(9)
#print(How_old_will_i_be)

#let's create a loop; while-loop amd for_loop
#while-loop
#import math
#from multiprocessing.connection import wait
#from os import remove
#from tracemalloc import stop
#from xml.etree.ElementTree import Comment


#s = 0
#while (s <= 5):
#    print (s)
#    s=s+1
    
#for-loop
#for s in range(5,10):
#    print(s)  
    
#days =["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]   

#for d in days:
#    if (d == "Thur"):break
#    print(d)
    
#    days =["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]   

#for d in days:
#    if (d == "Thur"):continue
#    print(d)
    
#import math
#print("pi is", 3*math.pi)

#Commentary = 'Finished Python for Beginners Tutorial'
#print(Commentary)


#Intermediate_python_Programming_Course:
#1 ---- #List

# mylist = ["banana", "cherry", "apple"]   
# print(mylist)

# mylist2 = list()
# print(mylist2) 

# mylist2 = ["5", "true", "Apple", "apple"]
# print(mylist2) 

# item = mylist2[2]
# print(item)
    
# for x in mylist:
    # print(x)
    
# if "apple" in mylist2:
    # print("yes") 
# elif "apple" != mylist2:
    # print("crystal clear")
# else:
    # print("no")

# print(len(mylist2))

# mylist2.append("lemon")
# print(mylist2) 

# mylist2.insert(2, "holder")
# print(mylist2)

# item = mylist2.pop(2)
# print(item)
# print(mylist2)

# item = mylist2.remove("apple")
# print(mylist2)

# item = mylist2.reverse()
# print(mylist2)

# item = mylist2.clear()
# print(mylist2)

# mylist = [2, -4, -10, 5, 3, 7, 11]
# print(mylist)

# item = mylist
# print(mylist)

# new_list = sorted(mylist)
# print(mylist)
# print(new_list)             

# mylist = [0] * 5
# print(mylist)

# mylist3 = [1, 2, 3, 4, 5]

# new_list2 = mylist + mylist3
# print(new_list2)

# mylist4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = mylist4[::-2]
# print(a)

# list_org = ["baanana", "cherry", "apple",]
# list_cpy = list_org
# print(list_cpy)

# list_cpy.append("lemon")
# print(list_cpy)
# print(list_org) 

# b = [i * i for i in mylist4]
# print(b)

#2 --------- TUPLES: ordered, immutable, allows duplicate elements
# its similar to list but only difference is dat cannot be change after its creation
# often used for objects that belong together

#mytuple = tuple(["salam-jay", 38, "font"])
#print(mytuple)

#item = mytuple[1]
#print(item)

#for i in mytuple:
#    print(i)
    
#if "desktop" in mytuple:
#    print("yes")
#else:
#    print("no")
    
#mytuple1 = ("h", "e", "n", "n", "e", "s", "s", "y")
#print(len(mytuple1))
#print(mytuple1.index("y"))

#mylist = list(mytuple)
#print(mylist)
#mytuple1 = tuple(mylist)

#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#b = a[::-2]
#print(b)

#my_tuple = "Salam-jay", 20, "Abeokuta"
#name, age, city = my_tuple
#print(name,age,city)

#my_tuple1 = (0,1,2,3,4,5)
#i1, * i2, i3 = my_tuple1
#print(i1, i2, i3)

#from ast import stmt
#import sys
#my_list1 = [0,1,2, "hello", "True"]
#my_tuple2 = (0,1,2, "hello", "True")
#print(sys.getsizeof(my_list1),"bytes")
#print(sys.getsizeof(my_tuple2),"bytes")

#import timeit
#print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
#print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))

#DICTIONARIES:key-value pairs, Unordered, Mutable
# a dictionary is created with {} and inside it ecah key value is seperated by a colon:

#mydict = {"name": "Salam-jay", "Age": 20, "city": "Abeokuta"} 
#print(mydict)

#mydict2 = dict(name="jackson", Age=21, city="ifo")
#print(mydict2)

#value = mydict2["name"]
#print(value)

#mydict["email"] = "salamjay16@gmail.com"
#print(mydict)

#mydict["email"] = "salamjayboss19@gmail.com"
#print(mydict)

#mydict.popitem()
#print(mydict)

#if "city" in mydict:
#    print(mydict["city"])
    
#try:
#    print(mydict["lastname"])
#except:
#    print("Error")    
    
#for key,value in mydict.items():
#    print(key,value)  
    
#mydict_cpy = mydict.copy()
#mydict_cpy["new_mail"] = "Jaypeslovers20@gmail.com"
#print(mydict_cpy)
#print(mydict)

#mydict.update(mydict2)
#print(mydict)

#mydict3 = "{2:4,6:8,10:12}"
#print(mydict3)
#value = mydict3[3]
#print(value)
    
#mytuple = (8,7)  
#mydict4 = {mytuple: 15}
#print(mydict4)

#4 -------- SETS; unordereed, mutable, no-duplicate
#                created with {} just like dictionary; simple element seperated by a comma

#myset = {1, 2, 3, 4, 5,}
#myset1 =set("Salam-Jay")
#print(myset)
#print(type(myset1)) 
#myset.add(9)
#myset.add(7)
#myset.add(11)
#print(myset)

#myset.remove(7)
#myset.discard(9)

#print(myset.pop())
#print(myset)

#for j in myset:
#    print(j)

#if 14 in myset:
#    print(YES)
#else:
#    print("no")
    
#odds = {1, 3, 5, 7, 9}
#evens = {0, 2, 4, 6, 8, 10}
#primes ={2, 3, 5, 7,}
#u = odds.union(evens)
#print(u)

#y = evens.intersection(primes)
#print(y)
   
#setA = {1,2,3,4,5,6,7,8,9}
#setB = {1,2,4,10,11,12}
#setC = {6,7}
#diff = setA.symmetric_difference(setB)
#print(diff)

#setA.intersection_update(setB)
#print(setA)

#setA.difference_update(setB)
#print(setA)

#setA.symmetric_difference_update(setB)
#print(setA)

#print(setB.issubset(setA))
#print(setA.issuperset(setB))
#print(setB.isdisjoint(setC))

#setC.add(12)
#print(setC)
#print(setB)

#a = frozenset([1,2,3,4,5])
#print(a)

#5 --- STRINGS: Unordered, immutable, text representation
       # one of the most used data type in Python created with ""
       
'''my_string = """Hello \
salam-jay"""   
print(my_string)
char = my_string[-8]
print(char)

substring = my_string[::-1]
print(substring)

nick = "jackson"
name = "AbdulSalam"
sentence = nick + " " + name
print(sentence)
print(sentence.upper())


for i in sentence:
    print(i)

if "Abdul" in sentence:
    print("yes")
else:
    print("no")
print(sentence.find("o"))

my_string = "Jackson,Abdulsalam"
print(my_string.replace('Abdulsalam', 'Abiodun'))
mylist = my_string.split(",")
print(mylist)
new_string = " ".join(mylist)
print(new_string)

from timeit import default_timer as timer
my_list = [' ab '] * 1000000 


#bad
start = timer()
my_string1 = ''
for i in my_list:
    my_string1 += i
stop = timer()
print(stop-start)


#good
start = timer()
my_string1 = ''.join(my_list)
stop = timer()
print(stop-start)

#formatting strings
# %, .format{}, f-Strings
var = 3.1428577  
my_string2 = "the variable is %.3f" % var
print(my_string2)

#format{}
var1 = 9.4285731 
var2 = 6.2857154
my_string3 = "the variable is {} and {}".format(var1,var2)
print(my_string3)

#f-Strings
var1 = 3.333333 
var2 = 6.666666
my_string3 = f"the variable is {var1} and {var2}"
print(my_string3)'''

'''#COLLECTIONS: counter, namedtuple, orderedDict, defaultDict, deque
 #1 ---- Counter:is a container that stores elements as dictionary keys and that counts as dictionary values
from collections import Counter
jay = "bsucht7cjhfjoiwtgbmnic"
my_counter = Counter(jay)
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))  

#2 --- namedtuple:is an easy to-create light-weight object-type similar to EXTRACT  
from collections import namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1, -5)
print(pt)
print(pt.x, pt.y)

#3 -- orderedDict -- is just like a regular dictionary but they remember the order the items where inserted
from collections import OrderedDict
ordered_dict = {}
ordered_dict['a'] = 1 
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['b'] = 2
print(ordered_dict)

#4 -- defaultdict:is also similar to the usual dictionary container but have a default value if the key hasn't been set yet    
from collections import defaultdict
c = defaultdict(list)
c['a']= 2
c['b']= 4
print(c['b'])

#5 -- deque;double-ended q;use to add/remove elements from both ends
from collections import deque
d = deque()
d.append(3)
d.append(5)
d.appendleft(8)
d.popleft()
d.extendleft([6,4,9])
print(d)
d.rotate(-2)
print(d)'''

'''#ITERTOOLS: are data types that can be used in a For-loop;list 
   # product, permutations, combinations, accumulate, groupby & infinite-iterators 
#1 --- Product 
from itertools import product
from typing import Sequence
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=1)
print(list(prod))

#2 -- Permutations
from itertools import permutations
a = [1,2,5]
b = [3,4]
perm = permutations(a, 3)
print(list(perm))

#3 -- Combinations
from itertools import combinations, combinations_with_replacement
c = [1,4,7,9]
d = [3,4]
comb = combinations(c, 2)
print(list(comb)) 
comb_wr = combinations_with_replacement(c,2)
print(list(comb_wr))

#4 -- accumulate; to sum in ascending order
from itertools import accumulate
import operator
e = [6,8,12,10,14]
acc = accumulate(e)
acc = accumulate(e, func=operator.mul)
acc = accumulate(e, func=max)
print(list(acc))

#5--- groupby; return keys and group 
from itertools import groupby
def smaller_than_3(x):
    return x < 3
a = [1,2,3,4]
group_obj =groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
    
#6 -- infinite iterators; count, cycle, repeat
    from itertools import count
    for i in count(100):
        print(i)
    if i == 500:
        break
    
 itertools import cycle
    a = [1,3,2,4 ]
    for i in cycle(a,10):
        print(i)
    
from itertools import repeat
a = [1,3,5,7]
for j in repeat(a, 50):
        print(j)'''


'''# Lambda arguments: expression
from functools import reduce
from tkinter import Y


add10 = lambda x: x ** 10
print(add10(5))

def add10_func(x):
    return x + 10
print(add10_func(5))

mult = lambda x,y: x ** y
print(mult(2,7))

div = lambda x,y: x / y 
print(div(160,12))
 
points2D = [(3,4), (5,-2), (7,2), (1,6)] 
points2D_sorted = sorted(points2D)
points2D_sorted1 = sorted(points2D, key=lambda x: x[1])
points2D_sorted2 = sorted(points2D, key=lambda x:x[0] + x[1])
print(points2D)
print(points2D_sorted)
print(points2D_sorted1)
print(points2D_sorted2)

#LAMBDA functions
from itertools import groupby
persons = [{'name': 'Jackson', 'age': 9}, {'name':'Jay', 'age': 15},
           {'name': 'Salam-jay', 'age': 16}, {'name':'Abiodun', 'age': 17}]
            
a = [1, 2, 3, 4]
group_obj = groupby(persons, key=lambda x: x['name'])
for key, value in group_obj:
    print(key, list(value))

# map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))

#map-list comprehension
c = [x**2 for x in a]
print(c)

# filter(func, seq)
f = [6,7,8,9,10,11,12,13,14]
g = filter(lambda x: x%2==0,f)
print(list(g))

#filter-list comprehension
h = [x for x in f if x%2==1]
print(h)

# reduce(func, seq)
a = [1,2,3,4,5]
prod_a = reduce(lambda x,y: x*y, a)
print(prod_a)'''


'''# ERRORS --- Syntax error, EXCEPTIONS;diff. between these these 2
#how can we erase and handle exceptions, most common built in exceptions, how to define my own exceptions

#Syntax error -- occurs when the parse detect a synthetically incorrect statement 
#a = 5*5 
#print(a)

#Exception Error --- Type Error
#a = 5 + "salam-jay"

#module Error
#import somemodule

#Name Error
#a = 5
#b = c

#File Error
#f = open('somefile.txt')
 
#Value Error
#v = [6,7,8,9,10,11,12,13,14]
#v.remove(9)
#print(v) 

#Index Error
#f = [6,7,8,9,10,11,12,13,14]
#f[9]
#print(f)

#Key Error
#my_dict = {'name': 'salam-jay'}
#my_dict['age']

#Exception
#x = 21
#if x > 20:
#    raise Exception('x should be reduced')

#Assertion Error 
#f = -10
#assert (f>=0), "x isn't positive"

#Handle Exceptions
        #1 -- Zero Division Error
        #a = 5 / 0

#2 -- Try & Except Error
#try:
#    f = 5 / 1
#    b = f + 4
#except ZeroDivisionError as e:
#    print(e)
#except TypeError as e:
#    print(e)
#else:
#    print('everything is fine')
#finally:
#    print('cleaning the Trash..')

#Define own Exceptions; from error Class
from multiprocessing.sharedctypes import Value


BaseException 
class ValueTooHighError(Exception): 
    pass 

class ValueTooSmallError(Exception):
   def __init__(self, message, value):
        self.message = message
        self.value = value
      

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is High')
    if x < 5:
        raise ValueTooSmallError('value is Small', x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)'''


'''#LOGGING: diff. Log levels, diff. config. options, how to log in different modules
    #how to use diff. log-endless, how to catch a stech traces in log, how to use rotating file handler

import logging
import logging.config

logging.config.fileConfig("logging.conf")

logger =logging.getLogger('simpleExample')
logger.debug('this is a debug message')'''


#JSON  --- JvaScript Object Notation
#import json

'''person = {"name": "Salam-jay", "age": 20, "city": "Abeokuta", "Single": "True", "titles": ("pre-Engineer", "programmer")}

personJSON = json.dumps(person, indent=4, separators=(": ", "="))
print(personJSON)

person = {"name": "Jackson", "age": 21, "city": "Abeokuta", "Single": "True", "titles": ("MNSE", "Coder")}

personJSON1 = json.dumps(person, indent=4, sort_keys=True)
print(personJSON1) 

with open ("person.json", "w") as file: 
    json.dump(person, file, indent=4)

with open ("person.json", "r") as file: 
    person = json.load(file)
    print(person)
    
    

class User:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
user = User("Salam-jay", 21)

def encode_user(o):
    if isinstance(o, user):
        return {"name": o.name, "age": o.age, o.__class__.name__: True}
    else:
        raise TypeError("Object of type user is not JSON serializable")
    
from json import JSONEncoder
Class UserEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, user):
            return {"name": o.name, "age": o.age, o.__class__.name__: True}


userJSON = json.dumps(user, default=encode_user)
print(userJSON)'''


#RANDOM NUMBERS; for pseudo-RN, secret module for crypto-graphically strong-RN
'''import random

r = random.random()
print(r)

f = random.uniform(2,9)
print(f)

d = random.randint(1,10)
print(d)

u = random.randrange(3,8)
print(u)

n = random.normalvariate(0,1)
print(n)

mylist = list("SALAM-JACKSON")
c = random.sample(mylist,2)
print(c)

mylist1 = list("boss-jay")
a = random.choices(mylist1,k=3)
print(a)

mylist2 = list("ADEYANJU")
random.shuffle(mylist2)
print(mylist2)

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10)) 

random.seed(1)
print(random.random())
print(random.randint(1,10)) 

random.seed(2)
print(random.random())
print(random.randint(1,10)) 

import secrets #: used for passwords, security-Tokens, account-Authentication

b = secrets.randbelow(10)
print(b)

i = secrets.randbits(10)
print(i)

mylist3 = list("CHEMISTRY")
e = secrets.choice(mylist3)
print(e)

#import numpy'''

#DECORATORS; diff. btw function and class decorators, 2 diff decorators 
#function decorator;
 
'''@mydecorator
def dosomething():
    pass'''
    
    
#import functools
def start_end_decorator(func):
    '''def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

@start_end_decorator
def print_name():
    print("Salam-jay")

#print_name = start_end_decorator(print_name)
print_name()

result = (add5(10))
print(result)'''
    
    '''@functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper
@start_end_decorator

def add5(x):  
   return x + 5

#print(help(add5))
#print_name = start_end_decorator(print_name)
print(add5.__name__)'''


'''#TEMPLATE FOR A DECORATOR
def my_decorator(func): 
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # do something...
            result = func(*args, **kwargs)
            # do something...
            return result
            return wrapper
@my_decorator
def fname(arg):
    return arg '''

'''def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=4)  
def greet(name):
    print(f'Hello {name}')
    
(greet('Abdulsalam'))'''

#stack decorator
'''def start_end_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}=(v!r)" for k in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}{signature}")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result 
    return wrapper
        
@debug
@start_end_decorator
def say_hello(name):
    greetings = f"Hello {name}"
    print(greetings)
    return greetings
say_hello('JACKSON ')'''


#CLASS DECORATOR
                #Example 1
'''class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self,*args, **kwargs):
        print('Hi there')

cc = CountCalls(None)
cc()

@CountCalls
def say_hello(arg):
    print("Hello")
    
                #Example 2
class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self,*args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(arg):
    print("Hello")
say_hello(arg)
say_hello(arg)
say_hello(arg)
say_hello(arg)
say_hello(arg)'''
#TIMER DECORATOR, #CHECK DECORATOR, #DEBUG DECORATOR


#GENERATORS are functuions that return an object that can be iterated over; much-more memory efficient
                #Example-1
'''def mygenerator():
    yield 3
    yield 2
    yield 1
    
g = mygenerator()
print(list(g))
 
for i in g:
    print(i)
    
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)

print(sum(g))
print(sorted(g))'''

                    #Example-2
'''def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
        
cd = countdown(4)
value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))'''

                    #example 3
#import sys
'''def first(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
print(sum(first(10)))
print(sys.getsizeof(first(1000000)))


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
        

print(sum(firstn_generator(10)))
print(sys.getsizeof(firstn_generator(1000000)))'''

                    #example 4
'''def fibonacci(limit):
    # the fibonacci sequence works like this; the first two numbers are 0 & 1
    #then all the following numbers are sum of the previous two number
    # 0+1=1  1+1=2  1+2=3 and so on like 5 8 13 
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b 
        
fib = fibonacci(30)
for i in fib:
    print(i)'''
    
                    #Generator expression
'''import sys
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)

    
mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)
print(sys.getsizeof(mylist))
print(sys.getsizeof(mygenerator))'''


                    #mini-project:
                    # LOVELY HEART CODE
'''import _tkinter
import time
import tkinter.font
import turtle
pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
        
def heart():
    pen.fillcolor('BLUE')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    
def txt():
    pen.up()
    pen.setpos(-75, 90)
    pen.down()
    pen.color('white')
    pen.write("I MISS YOU", font = ("veranda", 20, "bold", "italic",))
    time.sleep(3)
heart()
txt()
pen.ht()
         
                #Area of a trapezoid
                example_1
import functools
from unittest import result
def Area_of_a_Trapezoid(base_1,base_2,height):
    #Calculate it's Area
    Area_of_a_Trapezoid = 0.5 * (base_1 + base_2) * height
    print("Area of a Trapezoid:",Area_of_a_Trapezoid)
    return result
Area_of_a_Trapezoid(9,6,4)

                #example_2 ---- Area of Trapezium
import math
base_1 = 5
basse_2 = 6
height = float(input("Height in cm: "))
base_1 = float(input('Base 1 value in cm: '))
base_2 = float(input('Base 2 value in cm: '))
area = ((base_1 + base_2) /2 * height)
print("Area is in cm**:", area)'''

user = input("What is your favourite thing?")
print(f"i like {user} too")

import base64
                #Grading system
my_score = int(input("What's your score? "))
if my_score in range(0, 11):
    print("Your grade is 'F9', you be olodo")
if my_score in range(11, 39):
    print("F9, you no sabi shit!")
if my_score in range(39, 45):
    print("Your grade is E8")
if my_score in range(45, 50):
    print("Your grade is D7")
if my_score in range(50, 55):
    print("Your grade is C6")
if my_score in range(55, 60):
    print("Your grade is C5")
if my_score in range(60, 65):
    print("Your grade is C4")
if my_score in range(65, 70):
    print("Your grade is B3")
if my_score in range(70, 75):
    print("Your grade is B2")
if my_score in range(75, 90):
    print("Your grade is A1")
if my_score in range(90, 101):
    print("Your grade is A1, You are too brilliant!")



# THREADING VS MULTIPROCESSING: diff. btw a process & a thread, Adv. & Diasdv of both, 
#how and why Thread are limited by the Gil, how to easily use the builtin Threading & Multiprocessing Module to create processes 
                    #MULTIPROCESSING
'''from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range (100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()


# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)
    
# start
for p in processes:
    p.start()
    
# Join
for p in processes():
    p.join()
    
print('end main')'''

                #More details on Multiprocessing
from calendar import c
from inspect import Arguments
from multiprocessing import Pool, Process, process, Value, Array, Lock, Queue
import os, time, numbers
from symtable import Function
import traceback
from turtle import clone
from unittest import result

'''def square_numbers():
    for i in range (100):
        i * i     
        
if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()   
    # number of CPUs on the machine, Usually a good choice for the number of processes 
    
    # create processes and assign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)
        
    # start all processes
    for process in processes:
        process.start()
        
    # wait for all processes to finish
    # block the math program until these processes are finished
    for process in processes:
        process.join()'''

                    #number Type
'''def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        #with lock:
            #number.value += 1
        number.value += 1
        lock.release()
       
if __name__ == "__main__":
    
    lock = Lock()
    shared_number = Value('i',0)
    print('Number at the beginning is', shared_number.value)  
    
    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('number at end is', shared_number.value)'''
      
                    #Array type
'''def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
           with lock:
            numbers[i] += 1 
        
       
if __name__ == "__main__":
    
    lock = Lock()
    shared_array = Array('d',[0.0, 100.0, 200.0])
    print('array at the beginning is', shared_array[:])  
    
    p1 = Process(target=add_100, args=(shared_array,lock))
    p2 = Process(target=add_100, args=(shared_array,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('array at end is', shared_array[:])'''

               # example on QUEUE using MULTIPROCESSING
'''from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import time

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)
        
def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == "__main__":
    
    numbers = range(1,6)
    q = Queue()
    
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())'''
        
            #Process pool:can be used to manage multiple processes;
'''from multiprocessing import Pool

def cube(number):
    return number * number * number 
        

if __name__ == "__main__":
    
    numbers = range(15)
    pool = Pool()
    
    #pool has 4 important methods; MAP, APPLY, JOIN, CLOSE
    result = pool.map(cube, numbers)
    #pool.apply(cube, numbers[0])
    
    pool.close()
    pool.join()
    
    print(list(result))'''
    

                         #THREADING
'''from threading import Thread
import os
import time

def square_numbers():
    for i in range (100):
        i * i
        time.sleep(0.1)

threads = []
num_threads = 10


# create processes
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)
    
# start
for t in threads:
    t.start()
    
# Join
for t in threads():
    t.join()
    
print('end main')'''

                    #More details on THREADING
'''from threading import Thread

def square_numbers():
    for i in range(100):
        i * i
    
if __name__ == "__main__":
    threads = []
    num_threads = 10


    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)
    
    # start
    for thread in threads:
        thread.start()
    
    # Join
    for thread in threads():
        thread.join()
    
    print(threads)'''
    

                        #Example-2
'''from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
    global database_value
    
    with lock:
        local_copy = database_value
    #processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
    
    
if __name__  == "__main__":
    
    lock = Lock()
    print("start value", database_value)
    
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print('end value', database_value)
    
    print('end main')'''


                #QUEUEs; is a linear data structure that's follows the free-flow or first-in,first-out principle
                # example on QUEUE using THREAD
'''from queue import Queue
from threading import Thread, Lock, current_thread
import time
    #example-1: A queue of customers waiting in line with the customer that came first being served first

def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":
    q =  Queue()
    lock = Lock()
    #q.put(1)
    #q.put(2)
    #q.put(3)
    #first = q.get()
    #print(first)

    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon=True
        #a daemon thread is a backgroung thread that die when the main thread dies
        thread.start()
        
    for i in range(1,21):
        q.put(i)
        
    q.join()
 
    print('end main')'''
       

                #Function Arguments in Detail: we learn
"""
- The difference between arguments and Parameters
- Positional and Keyword Arguments
- Default arguments
- Variable-lenght arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs global Arguments
- Parameter passing (by value or by reference?)"""

#arguments
'''def fool(a, b, c):
    print(a, b, c)'''
 
#Positional Arguments   
'''fool(1,2,3)''' 

#Keyword Arguments:make its more clear what they present & we can rearrange the arguments to make it more READABLE
'''fool(a=2, b=3, c=1)'''   
   
#diff: another Positional Arguments can't be used after a Keyword Arguments
'''pool(1 , b=2, 3)'''
#SyntaxError: positional argument follows keyword argument

#Default argument
'''def fool(a, b, c, d=4):
    print(a, b, c, d)
fool(1,2,3,4,5)'''

#Variable-lenght arguments
'''def foo(a, b, c, *args, **kwargs):
    print(a,b,c)
    for arg in args:
        print(args)
    for key in kwargs:
        print(key, kwargs[key])
        
foo(1, 2, 3, 4, 5, six=6, seven=7)'''
    
#false keyword argument; keyword only argument
'''def poo(a, b, *, c, d):
    print(a,b,c,d)

poo(1, 2, c=3, d=4,)

def poo(*args,last):
    for arg in args:
        print(arg)
    print(last)

poo(1, 2, 3,last=100)'''

# UNpacking Arguments
'''def coo(a, b, c):
    print(a,b,c)
    
my_list = [0,1,2]
coo(*my_list)

my_dict = {'a':1, 'b':2, 'c':3}
coo(**my_dict)'''

#Local vs global Arguments
#Local Arguments
'''def joo():
    number = 3

number = 0
joo()
print(number)'''

#global Arguments
'''def joo():
    global number
    number = 3

number = 0
joo()
print(number)'''

#Local & global arguments joined 
'''def joo():
    global number
    x = number
    number = 3
    print('number inside function', x)

number = 0
joo()
print(number)'''

#Parameter passing
#mutable object
'''def moo(a_list):
    a_list.append(5)

mylist = [1,2,3,4]
moo(mylist)
print(mylist)'''

#immutable object
'''def boo(a_list):
    a_list.append(5)
    a_list[0] = -100
    
bylist = [1,2,3,4]
boo(bylist)
print(bylist)'''

#difference
'''def goo(a_list):
    a_list += [200, -300 ,400]

gylist = [1,2,3,4]
goo(gylist)
print(gylist)'''

#ASTERISK OPERATOR
#simple multiplication operation
'''result_of = 5 * 8
print(result_of)'''

#Raise to power_of
'''power_of = 2 ** 4
print(power_of)'''

#number of times
'''zeros = [0] * 10
print(zeros)
zeros_ones = (0,1)* 10
print(zeros_ones)
Alphabet = ("SJ") * 5
print(Alphabet)'''

#keywords (*args, **kwargs)
'''def doo(a, b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
doo(1,2,3,4,5, six=6, seven = 7)'''

'''def doo(a, b, c):
    print(a,b,c)
    
my_list = [0,1,2]
doo(*my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
doo(**my_dict)'''

#Unpacking CONTAINERS
'''numbers = [1,2,3,4,5,6]
beginning,middle,*secondlast,last= numbers
print(beginning)
print(middle)
print(secondlast)
print(last)'''

#Unpack Multiple data
'''my_tuple = (1, 2, 3)
my_list = (4,5,6)
new_list = [*my_tuple, *my_list]
print(new_list)

my_tuple1 = (7, 8, 9)
my_set = {10,11,12}
new_list1 = [*my_tuple1, *my_set]
print(new_list1)

new_list2 =[*my_tuple,*my_list,*my_tuple1,*my_set]
print(new_list2)

dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
my_dict = {**dict_a, **dict_b}
print(my_dict)'''


#SHALLOW vs Deep COPYING; how to copy mutable elements with the built-in copying Module, diff btw these two
                            #how to make actual copies of custom objects 
#Preamble --- Assignment Operator
'''org = [0,1,2,3,4,5]
cpy = org
cpy[0] = -10
print(cpy)
print(org)'''

#SHALLOW COPY for one LEVEL DEEP, for 2 or more (NEXT)-LEVEL DEEP; SHALLOW COPY is impossible
'''import copy
org = [0,1,2,3,4,5]
#cpy = copy.copy(org)
#cpy = org.copy()
#cpy = list(org)
cpy = org[:]   # -- list slicing
cpy[0] = -10
print(cpy)
print(org)'''

#DEEP COPY
'''import copy
org = [[0,1,2,3,4,5], [6,7,8,9,10]]
cpy = copy.deepcopy(org)
cpy[0][2] = -10
print(cpy)
print(org)'''

#CUSTOM Object
'''import copy
class Person:
   def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Salam-jay', 28)
p2 = copy.copy(p1)

p2.age = 29
print(p2.age)
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
            
p1 = Person('Salam-jay', 16)
p2 = Person('Jackson', 21)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 20
print(company_clone.boss.age)
print(company.boss.age)'''


#CONTEXT MANAGERS:are great-tools for resource Management, allow you to allocate amnd release resources when needed
#using WITH-OPEN Statement
'''with open('note.txx', 'w') as file:
    file.write('some todoo...')

file = open('note.txt', 'w')
try:
    file.write('some todoo...') 
finally:
    file.close()'''
    
#for our OWN Class
'''class ManagedFile:
    def __init__(self, filename):
        print('__init__')
        self.filename = filename
     
    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        #print('exc:', exc_type, exc_value)
        print('exit')
        return True
        
with ManagedFile('note.txt') as file:
    print('do some stuffs...')
    file.write('some todoo...') 
    file.somemethod()
print('continuing')''' 
         
         
#As a FUNCTION
'''from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close
        
with open.managed_file('note.txt') as f:
    f.write('some method...')'''
    
# mylist = []
# for number in range(0,1000):
#     if number % 2 == 1:
#         mylist.append(number)
# print(mylist)
    
# mylist2 = [number for number in range(0, 1000) if number % 3 == 0]
# mylist2

# def add_ten_to_age(age):
#    new_age = age + 10
#    return new_age
# print(add_ten_to_age(10))

# def sum_numbers(a, b):
#     return a + b
# print(sum_numbers(8, 5))