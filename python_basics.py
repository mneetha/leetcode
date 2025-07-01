# Control flow
import traceback

name = 'shiv'
if name == 'shiv':
    print('Hi Shiv')
elif name == 'arjun':
    print('Hi Arjun')
else:
    print('Who are you?')


# ternary pattern
age = 15
print('kid' if age < 18 else 'adult')

#switch - case
response_code = 201
# match response_code:
#     case 200 | 2001:
#         print('ok')
#     case 300 | 303:
#         print("Redirect")
#     case int():
#         if response_code > 99 and response_code < 500:
#             print('code is a valid number')
#     case _:
#         print("invalid code")

#while

spam = 0
while spam < 5:
    print('Hello world')
    spam = spam + 1

while True:
    name = input('please type your name')
    if name == ' joe':
        continue
    if name == 'shiv':
        break
    break

#for
pets = ['Bella', 'milo', 'loki']
for pet in pets:
    print(pet)

for i in range(5):
    print(f'willl stop at 5! or 4? ({i})')

for i in range(0,10,2):
    print(i)

for i in range(5, -1, -1):
    print(i)

for i in [1,2,3,4,5]:
    if i == 3:
        break
    else:
        print('num is not equal to 3')

#functions
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

def add(x, y):
    return x+y

add = lambda x,y:x+y

def make_adder(n):
    return lambda x:x+n

plus_3 = make_adder(3)
plus_4 = make_adder(4)
plus_3(4)

#list
furniture = ['table', 'chair', 'rack', 'shelf']
furniture[0:4]
furniture[:]

furniture2 = furniture[:]
furniture.append('desk')
len(furniture2)
price = [100, 30, 190, 60, 44]
# furniture + ['see', 'i']

for index, item in enumerate(furniture):
    print(f'index: {index} - item: {item}')

for item, amount in zip(furniture, price):
    print(f'the {item}  costs ${amount}')

table, chair, rack, shelf, desk = furniture

furniture.index('chair')
furniture.insert(1, 'bed')
del furniture[2]
furniture.remove('chair') #first instance

furniture.pop()

numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
numbers.sort(reverse=True)

sorted(furniture)


#tuples - immutable objects
furniture1 = ('table', 'chair', 'rack', 'shelf')
furniture1[0]

tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
list('hello')

#dict

my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

my_cat['age_years'] = 2
print(my_cat)
print(my_cat['size'])

for value in my_cat.values():
    print(value)
pet = {'color': 'red', 'age': 42}
for key in pet.keys():
    print(key)

for key in pet:
    print(key)

for items in pet.items():
    print(item)

for key, value in pet.items():
    print(f'Key: {key}, Value:{value}')

wife = {'name': 'Rose', 'age': 33}
f'my wife name is {wife.get("name", "some_other_value")}'

wife.setdefault('has_hair', True)
wife.pop('age')
wife.popitem()
del wife['name']

my_cat.clear()

person = {'name': 'Rose', 'age': 33}
'name' in person.keys()
'Rose' in person.values()

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
dict_c = {**dict_a, **dict_b}

#set
s = {1,3,4,6}
s = set([1,2,3])
s = {1, 2, 3, 2, 3, 4}
# s[0] will fail
s.add(5)
s.update([8,9])

s.remove(3)
s.discard(3)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2,s3) # s1 & s2 & s3

s1.difference(s2) #s1 - s2

s1.symmetric_difference(s2) #s1^s2

#list comprehension

names = ['Charles', 'Susan', 'Patrick', 'George']
new_list = []
for n  in names:
    new_list.append(n)
new_list_1 = [n for n in names]

n = [{a,b} for a in range(1,3) for b in range(1,3)]

new_list = []
for n in names:
    if n.startswith('C'):
        new_list.append(n)
new_list_1 = [n for n in names if n.startswith('C')]

nums = [1, 2, 3, 4, 5, 6]
new_list = [num*2 if num%2 == 0 else num for num in nums]

#set comprehension
b = {"abc", "def"}
{s.upper() for s in b}

#dict comprehension
c = {'name': 'pooka', 'age': 5}
h = {v:k for k,v in c.items()}

["{}: {}".format(k.upper(), v) for k,v in c.items()]

#manipulating strings

print("Hello there! \n how are you?\n I \'m doing fine.")

print(r"Hello there!\n How are you?\n I\'m doing fine.")

print(
    """Dear XYZ,
    ....
    Warm Regards,
    ABC"""
)

spam = "Hello World!"
spam[0]

spam[0:5]
spam[6:]
spam[6:-1]
spam[::-1]

'hello' in 'hello world'

'Hello' in 'hello world'
'' in 'spam'

greet = 'Hello world!'
greet.upper()
greet.lower()
greet.title()

spam.islower()
spam.isupper()

#isalpha, isalnum, isdecimal, isspace, istitle,

spam.startswith('Hello')
spam.endswith('world')

''.join(['My', 'name', 'is', 'simon'])
', '.join(['My', 'name', 'is', 'simon'])
' '.join(['My', 'name', 'is', 'simon'])
'ABC'.join(['My', 'name', 'is', 'simon'])

'My name is Simon'.split()

'MyABCnameABCisABCSimon'.split('ABC')

' My    name is Simon'.split()

' My name is Simon '.split(' ')

'Hello'.rjust(10)
'Hello'.rjust(20)
'Hello world'.rjust(20)
'Hello'.ljust(10)
'Hello'.center(10)

'Hello'.rjust(10,'*')
'Hello'.ljust(10, '-')
'Hello'.center(10, '=')

spam = ' Hello world'
spam.strip()

spam.lstrip()
spam.rstrip()
spam.strip()
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')

sentence = 'one sheep two sheep three sheep four'
sentence.count('sheep')
sentence.count('e')
sentence.count('e', 6)
sentence.count('e', 7)

text = "Hello, world"
text.replace("world", "planet")

fruits = "apple, banana, cherry, apple"
fruits.replace('apple', 'orange', 1)

#String formating

name = 'pete'
print('hello %s' % name)

print('i have %d apples' % 5)
print('hello i\'m {}, my age is {}'.format('john', 90))
print(f'Hello {name}')
a,b = 5,10
print(f'five plus ten is {a+b} and not {a*b}')

name = 'robert'
messages = 12
(
    f'hi, {name}'
    f'you have {messages} unread messages'
)

from datetime import datetime
now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
f'date and time: {now=}'

f"{name.upper() = :-^20}"
a= 10000
f"{a:,}"

a=3.1415926
f"{a:.2f}"

from string import Template
name = 'Elizabeth'
t = Template('Hey $name!')
t.substitute(name=name)

import re
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 444-555-2323')
mo.group(1)
mo.group(2)
mo.group(0)
mo.group()

area_code, main_num = mo.groups()

hero_regex = re.compile(r'Batman|Tina Fey.')
mo1 = hero_regex.search('Batman and Tina Fey')
mo1.group()

mo2 = hero_regex.search('Tina Fey and Batman.')
mo2.group()

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)

bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('the adventures of Batman')
mo1.group()
mo2 = bat_regex.search('The adventures of Batwoman')
mo2.group()

bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
mo1.group()

mo2 = bat_regex.search('The Adventures of Batwoman')
mo2.group()

mo3 = bat_regex.search('The Adventures of Batwowowowoman')
mo3.group()

bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The Adventures of Batwoman')
mo1.group()

mo2 = bat_regex.search('The Adventures of Batwowowowoman')
mo2.group()

mo3 = bat_regex.search('The Adventures of Batman')
mo3 is None

ha_regex = re.compile(r'(Ha){3}')
mo1 = ha_regex.search('HaHaHa')
mo1.group()

mo2 = ha_regex.search('Ha')
mo2 is None

ha_regex = re.compile(r'(Ha){2,3}')
mo1 = ha_regex.search('HaHaHaHa')
mo1.group()

greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_ha_regex.search('HaHaHaHaHa')
mo1.group()

non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
mo2.group()

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')

vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_regex.findall('Robocop eats baby food. BABY FOOD.')

consonant_regex = re.compile(r'[^aeiouAEIOU]')
consonant_regex.findall('Robocop eats baby food. BABY FOOD')

begins_with_hello = re.compile(r'^Hello')
begins_with_hello.search('Hello world!')
begins_with_hello.search('He said hello.') is None

whole_string_is_num = re.compile(r'^\d+$')
whole_string_is_num.search('1234567890')
whole_string_is_num.search('12345xyz67890') is None
whole_string_is_num.search('12 34567890') is None

at_regex = re.compile(r'.at')
at_regex.findall('The cat in the hat sat on the flat mat.')
greedy_regex = re.compile(r'<.*>')
mo1 = greedy_regex.search('<To serve man> for dinner.>')
non_greedy_regex = re.compile(r'<.*?>')
mo2 = non_greedy_regex.search('<To serve man> for dinner.>')

no_newline_regex = re.compile('.*')
no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

newline_regex = re.compile('.*', re.DOTALL)
newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')

robocop = re.compile(r'robocop', re.I)
robocop.search('Robocop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.').group()
robocop.search('Al, why does your programming book talk about robocop so much?').group()

names_regex = re.compile(r'Agent \w+')
names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

import os
#windows
os.path.join('usr', 'bin', 'spam')

from pathlib import Path
#unix
print(Path('usr').joinpath('bin').joinpath('spam'))

print(Path('usr') / 'bin' / 'spam')

my_files = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in my_files:
    print(os.path.join('C:\\Users\\asweigart', filename))

home = Path.home()
for filename in my_files:
    print(home / filename)

os.getcwd()
os.chdir('C:\\Windows\\System32')
os.getcwd()

print(Path.cwd())
os.chdir('usr/lib/python3.9')
print(Path.cwd())

os.makedirs('C:\\delicious\\walnut\\waffles')
cwd = Path.cwd()
(cwd / 'delicious' / 'walnut' / 'waffles').makedir(parents=True)

os.path.isabs('/')
os.path.isabs('..')

Path('/').is_absolute()
Path('..').is_absolute()

os.getcwd()
os.path.abspath('..')

print(Path.cwd())
print(Path('..').resolve())

os.path.exists('.')
os.path.exists('setup.py')
os.path.exists('/etc')
os.path.exists('nonexistentfile')

os.path.isfile('setup.py')
os.path.isfile('/home')
os.path.isfile('nonexistentfile')

Path('setup.py').is_file()
Path('/home').is_file()
Path('nonexistentfile').is_file()


with open('') as hello_file:
    hello_content = hello_file.read()
    lines_content = hello_file.readlines()
    for line in hello_file:
        print(line, end='')

with open('bacon.txt', 'w') as hello_file:
    hello_file.write('hello again\n')

with open('bacon.txt', 'a') as hello_file:
    hello_file.write('not you again\n')

import json
with open('some_json.json', "r") as f:
    content = json.load(f)

content = {"name": "Joe", "age": 20}

with open("some_json.json") as f:
    json.dump(content, f, indent=2)

from ruamel.yaml import YAML
with open("filename.yaml") as f:
    yaml = YAML()
    yaml.load(f)

import anyconfig

conf1 = anyconfig.load('path to someconf.yml')

def divide(dividend, divisor):
    try:
        if (dividend == 10):
            var = 'str' + 1
        else:
            print(dividend / divisor)
    except ZeroDivisionError:
        print('You can not divide by 0')
    except:
        with open('errorInfo.txt', 'w') as err_file:
            err_file.write(traceback.format_exc())
    finally:
        print('Execution finished')

class MyCustomException(Exception):
    pass

raise MyCustomException('A custom message for my custom exception')


def some_func(*args, **kwargs):
    pass

some_func(arg1, arg2, arg3)

some_func(key1=arg1, key2=arg2)

some_func(arg1, key1=arg1)

