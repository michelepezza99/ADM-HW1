# Say "Hello, World!" With Python
if __name__ == '__main__':
    my_str = 'Hello, World!'
    print(my_str)

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif (n % 2 == 0) and (2 <= n <= 5):
        print('Not Weird')
    elif (n % 2 == 0) and (6 <= n <= 20):
        print('Weird')
    elif (n % 2 == 0) and (n >= 20):
        print('Not Weird')
 

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# Write a function
def is_leap(year):
    leap = False
    # Write your logic here
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 100 == 0) and (year % 400 == 0):
            leap = True
    else:
        leap = False
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    s = ''
    for i in range(1,n+1):
        s += str(i)
    print(s)

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lis = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(lis)
    

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    set1 = set(arr)
    lis = list(set1)
    lis.sort()
    print(lis[-2])

# Nested Lists
if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    studs = [[names[i],scores[j]] for i in range(len(names)) for j in range(len(scores)) if i == j]
    studs.sort(key=lambda x: x[1])
    snd_lwst_l = list(set([j for i,j in studs]))
    snd_lwst = snd_lwst_l[1]
    snd_students = [name for name,grade in studs if grade == snd_lwst]
    snd_students.sort()
    for i in snd_students:
        print(i)
            

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s = 0
    for i in student_marks[query_name]:
        s += i
    average = s/len(student_marks[query_name])
    print(f"{average:.2f}")
        

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = list(map(int,input().split()))
a_list = []
b_list = []
for a in range(n):
  a_list.append(input())
for b in range(m):
  b_list.append(input())
final_dict = defaultdict()
for b in b_list:
  if b in a_list:
    final_dict[b] = [i+1 for i,a in enumerate(a_list) if a == b]
    print(' '.join(map(str,final_dict[b])))
  else:
    print(-1)

# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
cols = input().split()
total = 0
for i in range(n):
  studs = namedtuple('student',cols)
  MARKS, CLASS, NAME, ID = input().split()
  student = studs(MARKS, CLASS, NAME, ID)
  total += int(student.MARKS)
print('{:.2f}'.format(total / n))

# Lists
if __name__ == '__main__':
    N = int(input())
    lis = []
    for i in range(N):
        com = input().split()
        if len(com) == 3:
            num = com[1:]
            num = [int(k) for k in num]
            cd = com[0]
        elif len(com) == 2:
            num = int(com[-1])
            cd = com[0]
        else:
            cd = com[0]
        if cd == 'insert':
            lis.insert(num[0],num[-1])
        elif cd == 'print':
            print(lis)
        elif cd == 'remove':
            lis.remove(num)
        elif cd == 'append':
            lis.append(num)
        elif cd == 'sort':
            lis.sort()
        elif cd == 'pop':
            lis.pop()
        elif cd == 'reverse':
            lis = lis[::-1]
        else:
            print('Non existing command!')

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup = tuple(integer_list)
    print(hash(tup))

# sWAP cASE
def swap_case(s):
    swap = []
    for i in list(s):
        if i == i.lower():
            swap.append(i.upper())
        else:
            swap.append(i.lower())
    swap = ''.join(swap)
    return swap

# String Split and Join

def split_and_join(line):
    # write your code here
    line = line.split()
    line = '-'.join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')

# Mutations
def mutate_string(string, position, character):
    lis = list(string)
    lis[position] = character
    return ''.join(lis)

# Find a string
def count_substring(string, sub_string):
    len1 = len(string)
    len2 = len(sub_string)
    tot = 0
    for i in range(len1-len2+2):
        if sub_string in string[i:i+len2]:
            tot += 1
    return tot

# String Validators
if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))  
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))  

# Text Alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Text Wrap

def wrap(string,max_width):
  for i in range(0,len(string)+1,max_width):
    c = string[i:i+max_width]
    if len(c) == max_width:
      print(c)
    else:
      return c

# Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Output the design pattern.
N,M = map(int,input().split())
for i in range(1,N,2):
  print(('.|.'*i).center(M,'-'))
print('WELCOME'.center(M,'-'))
for i in range(N-2,-1,-2):
  print(('.|.'*i).center(M,'-'))

# String Formatting
def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    for i in range(1,number+1):
        bina = bin(i)[2:]
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        print(deci.rjust(w),octa.rjust(w),hexa.rjust(w),bina.rjust(w))

# Alphabet Rangoli
def print_rangoli(size):
    import string
    
    # Get the lowercase alphabet
    alphabet = string.ascii_lowercase
    
    # List to store the rangoli rows
    lines = []
    
    # Create the rows from top to bottom
    for i in range(size):
        # Get the slice of the alphabet for this row
        left_part = alphabet[size-1:i:-1]  # Letters from size-1 down to i+1
        center_part = alphabet[i:size]     # Letters from i to size-1
        row = '-'.join(left_part + center_part)  # Combine both parts with '-'
        lines.append(row.center(4*size-3, '-'))  # Center the row with dashes
        
    # Print the top half and the mirror image for the bottom half
    print('\n'.join(lines[-1::-1] + lines[1:]))

# Capitalize!

# Complete the solve function below.
def solve(s):
  for name in s.split():
    s = s.replace(name,name.capitalize())
  return s

# The Minion Game
def minion_game(string):
  vowels = 'AEIOU'
  kevin = stuart = 0
  length = len(string)
  for i in range(length):
    if string[i] in vowels:
      kevin += length - i
    else:
      stuart += length - i
  if stuart > kevin:
    print(f'Stuart {stuart}')
  elif kevin > stuart:
    print(f'Kevin {kevin}')
  else:
    print('Draw')

# Merge the Tools!
def merge_the_tools(string, k):
  n = len(string) / k
  for i in range(0,int(n*k),k):
    substr = string[i:i+k]
    u = []
    for j in range(len(substr)):
      if substr[j] not in u:
        u.append(substr[j])
    print(''.join(u))

# Introduction to Sets
def average(array):
    # your code goes here
    set1 = set(array)
    return sum(set1) / len(set1)

# No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
# No Idea!
n, m = map(int,input().split())
array = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happiness = 0
for i in array:
  if i in A:
    happiness += 1
  elif i in B:
    happiness -= 1
print(happiness)

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Symmetric Difference
# Symmetric Difference
M = int(input())
A = set(map(int,input().split()))
N = int(input())
B = set(map(int,input().split()))
sdiff = A ^ B
lis = list(sdiff)
lis.sort()
for i in lis:
  print(i)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Set.add()
N = int(input())
stamps = set()
for i in range(N):
  stamps.add(input())
print(len(stamps))

# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
  com = input().split()
  word = com[0]
  if word == 'pop' and len(s) > 0:
    s.pop()
  elif word == 'discard':
    s.discard(int(com[-1]))
  elif word == 'remove' and int(com[-1]) in s:
        s.remove(int(com[-1]))
print(sum(s))

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(map(int,input().split()))
b = int(input())
fr = set(map(int,input().split()))
print(len(eng | fr))

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(map(int,input().split()))
b = int(input())
fr = set(map(int,input().split()))
print(len(eng & fr))

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(map(int,input().split()))
b = int(input())
fr = set(map(int,input().split()))
print(len(eng - fr))

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(map(int,input().split()))
b = int(input())
fr = set(map(int,input().split()))
print(len(eng ^ fr))

# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Set Mutations
n = int(input())
s = set(map(int,input().split()))
N = int(input())
for _ in range(N):
  com = input().split()
  temp = set(map(int,input().split()))
  if com[0] == 'intersection_update':
    s.intersection_update(temp)
  elif com[0] == 'update':
    s.update(temp)
  elif com[0] == 'symmetric_difference_update':
    s.symmetric_difference_update(temp)
  elif com[0] == 'difference_update':
    s.difference_update(temp)
print(sum(s))

# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
# The Captain's Room
k = int(input())
rooms = list(map(int,input().split()))
a = set()
b = set()
for room in rooms:
  if room not in a:
    a.add(room)
    b.add(room)
  else:
    b.discard(room)
b = list(b)
print(b[0])

# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Check Subset
T = int(input())
for _ in range(T):
  n = int(input())
  A = set(map(int,input().split()))
  m = int(input())
  B = set(map(int,input().split()))
  lis = [a in B for a in list(A)]
  print(all(lis))

# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Check Strict Superset
A = set(map(int,input().split()))
n = int(input())
l1 = []
for i in range(n):
  B = set(map(int,input().split()))
  l2 = [b in A for b in B]
  issubset = all(l2)
  l3 = [a not in B for a in A]
  isstrict = any(l3)
  l1.append(issubset and isstrict)
print(all(l1))

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# collections.Counter()
from collections import Counter
X = int(input())
shoes = list(map(int,input().split()))
cust = int(input())
store = Counter(shoes)
rev = 0
for i in range(cust):
  size_price = list(map(int,input().split()))
  size = size_price[0]
  price = size_price[1]
  if store[size] > 0:
    store[size] -= 1
    rev += price
print(rev)

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Collections.OrderedDict()
from collections import OrderedDict
N = int(input())
store = OrderedDict()
for _ in range(N):
  *item, price = input().split()
  item = ' '.join(item)
  price = int(price)
  if item in store.keys():
    store[item] += price
  else:
    store[item] = price
for i in store:
  print(i, store[i])

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Collections.deque()
from collections import deque
N = int(input())
d = deque()
for _ in range(N):
  com = input().split()
  word = com[0]
  if len(com) > 1:
    num = com[-1]
  if word == 'append':
    d.append(num)
  elif word == 'appendleft':
    d.appendleft(num)
  elif word == 'pop':
    d.pop()
  elif word == 'popleft':
    d.popleft()
print(' '.join(d))

# Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Piling Up!
from collections import deque
T = int(input())
for _ in range(T):
  n = int(input())
  blocks = deque(map(int,input().split()))
  pile = deque()
  pile.append(float('inf'))
  for i in range(n):
    if blocks[0] >= blocks[-1] and blocks[0] <= pile[-1]:
      pile.append(blocks[0])
      blocks.popleft()
    elif blocks[-1] > blocks[0] and blocks[-1] <= pile[-1]:
      pile.append(blocks[-1])
      blocks.pop()
    else:
      break
  pile.popleft()
  if len(pile) == n:
    print('Yes')
  else:
    print('No')

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Word Order
from collections import Counter
n = int(input())
words = []
for i in range(n):
  words.append(input())
occ = Counter(words)
print(len(occ.keys()))
print(*occ.values())

# Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys
# Company Logo
from collections import Counter

if __name__ == '__main__':
    s = input()
    word = Counter(list(s))
    l = list(zip(list(word.keys()),list(word.values())))
    l.sort(key=lambda x:(-x[1],x[0]))
    for i in range(3):
        print(*l[i])

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Calendar Module
import calendar
date = list(map(int,input().split()))
Year = date[-1]
Month = date[0]
Day = date[1]
cal = calendar.weekday(year=Year,month=Month,day=Day)
if cal == 0:
  print('MONDAY')
elif cal == 1:
  print('TUESDAY')
elif cal == 2:
  print('WEDNESDAY')
elif cal == 3:
  print('THURSDAY')
elif cal == 4:
  print('FRIDAY')
elif cal == 5:
  print('SATURDAY')
else:
  print('SUNDAY')

# Time Delta
#!/bin/python3
from datetime import datetime, timedelta
import math
import os
import random
import re
import sys
# Complete the time_delta function below.
def time_delta(t1, t2):
  # complete here
  date_format = '%a %d %b %Y %H:%M:%S %z'
  time1 = datetime.strptime(t1,date_format)
  time2 = datetime.strptime(t2,date_format)
  time_diff = (time1 - time2).total_seconds()
  time_diff = abs(int(time_diff))
  return str(time_diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Exceptions
T = int(input())
for _ in range(T):
  a,b = input().split()
  try:
    print(int(int(a)//int(b)))
  except (ZeroDivisionError, ValueError) as e:
    print("Error Code:",e)

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Zipped!
N, X = map(int,input().split())
voti_tot = []
for i in range(X):
  voti_sub = list(map(float,input().split()))
  voti_tot.append(voti_sub)
grades = list(zip(*voti_tot))
for i in range(len(grades)):
  print(sum(grades[i])/len(grades[i]))

# Athlete Sort
# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr.sort(key = lambda x: x[:][k])
    for i in range(len(arr)):
      print(*arr[i])

# ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
# ginortS
def my_order(ch):
  if ch.islower():
    return (0,ch)
  elif ch.isupper():
    return (1,ch)
  elif ch.isdigit() and int(ch) % 2 == 1:
    return(2,ch)
  elif ch.isdigit() and int(ch) % 2 == 0:
    return(3,ch)
def ginorts(S):
  S_list = list(S)
  S_list.sort(key=my_order)
  return ''.join(S_list)
S = input()
print(ginorts(S))

# Map and Lambda Function
cube = lambda x: x**3 # complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
      return []
    elif n == 1:
      return [0]
    else:
      fib = [0,1]
      for i in range(1,n-1):
        fib.append(fib[i] + fib[i-1])
      return fib

# Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Detect Floating Point Number
import re
T = int(input())
for i in range(T):
  s = input()
  print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',s)))

# Re.split()
regex_pattern = r"[.,]+"    # Do not delete 'r'.

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Group(), Groups() & Groupdict()
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Re.findall() & Re.finditer()
import re
vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'
match = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', input(), flags=re.I)
print('\n'.join(match or ['-1']))

# Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Re.start() & Re.end()
import re
string = input()
substring = input()
pattern = re.compile(substring)
match = pattern.search(string)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)

# Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for i in range(N):
    line = input()
    # No need to even use regex for this, string's replace() method will do
    while (' && ' in line) or (' || ' in line):
        line = line.replace(' && ', ' and ')
        line = line.replace(' || ', ' or ')
        
    print(line)   

# Validating Roman Numerals


regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

# Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for i in range(0, N):
    print('YES') if re.match(r'[789]\d{9}$', input()) else print('NO')

# Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils 
N = int(input())
pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'
for i in range(0, N):
    addr = email.utils.parseaddr(input())
    if re.search(pattern, addr[1]):
        print(email.utils.formataddr(addr)) 
    

# Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())): 
    m = re.findall(r"(\#[a-f0-9]{3,6})[\;\,\)]{1}", input(), re.I) 
    if m:
        for j in list(m):
            print(j)

# HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
# HTML Parser - Part 1
from html.parser import HTMLParser
N = int(input())
class MyHTMLParser(HTMLParser): 
    
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for i in attrs:
            print('->', i[0], '>', i[1])
            
    def handle_endtag(self, tag):
        print('End   :', tag)
        
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for i in attrs:
            print('->', i[0], '>', i[1])
            
Parser = MyHTMLParser()
Parser.feed(''.join([input().strip() for i in range(0, N)]))

# HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, c):
        print('>>> Multi-line Comment') if (c.find('\n') != -1) else print('>>> Single-line Comment')
        print(c)
        
    def handle_data(self, data):
        if data is '\n':
            return
        print('>>> Data')
        print(data)
  
  
  
  
  
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
N = int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
    
html = '\n'.join([input() for i in range(0, N)])  
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Validating UID
# Validating UID
import re
T = int(input())
for i in range(T):
    UID = input()
    cond1 = len(re.findall(r"[A-Z]", UID)) >= 2
    cond2 = len(re.findall(r"[0-9]", UID)) >= 3
    cond3 = len(re.findall(r"[a-zA-Z0-9]", UID)) == len(UID)
    cond4 = len(set(UID)) == len(UID)
    cond5 = len(UID) == 10
    if all([cond1,cond2,cond3,cond4,cond5]):
      print('Valid')
    else:
      print('Invalid')

# Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Validating Credit Card Numbers
import re
N = int(input())
for _ in range(N):
    Num = input()
    cond1 = bool(re.match(r"^[456]\d{15}$", Num))
    cond2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", Num))
    Num = Num.replace("-", "")
    cond3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", Num))
    if (cond1 or cond2) and cond3:
        print("Valid")
    else:
        print("Invalid")

# Validating Postal Codes
regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

# Matrix Script
#!/bin/python3
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
matrix = list(zip(*matrix))

s = str()
for sub in matrix:
    for l in sub:
        s += l
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', s))

# XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    return len(node.items()) + sum([get_attr_number(i) for i in node])

# XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
        
    for c in elem:
        depth(c, level + 1)

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 " + i[-10:-5] + " " + i[-5:] for i in l])
    return fun

# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        return [ f(i) for i in sorted(people, key = lambda x: (int(x[2])))]
    return inner

# Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = arr[::-1]
    nump = numpy.array(arr)
    nump = nump.astype(float)  
    return nump

# Shape and Reshape
import numpy as np
arr = input().strip().split()
def shape_reshape(arr):
  narr = np.array(arr)
  narr = narr.astype(int)
  narr = np.reshape(narr,(3,3))
  return narr
print(shape_reshape(arr))


# Transpose and Flatten
import numpy as np
N, M = map(int,input().split())
arr = []
for i in range(N):
  row = list(map(int,input().split()))
  arr.append(row)
def trans_flat(a):
  a = np.array(a)
  print(np.transpose(a))
  print(a.flatten())
trans_flat(arr)


# Concatenate
import numpy as np
N, M, P = map(int,input().split())
arr1 = []
for i in range(N):
  row = list(map(int,input().split()))
  arr1.append(row)
arr2 = []
for i in range(M):
  row = list(map(int,input().split()))
  arr2.append(row)
def concatenate(a1,a2):
  n1 = np.array(a1)
  n2 = np.array(a2)
  print(np.concatenate((a1,a2),axis=0))
concatenate(arr1,arr2)


# Zeros and Ones
import numpy as np
def zeros_ones():
  dim = tuple(map(int,input().split()))
  print(np.zeros(dim,dtype = int))
  print(np.ones(dim,dtype= int))
zeros_ones()


# Eye and Identity
import numpy as np
np.set_printoptions(legacy = '1.13')
def eye_identity():
  n,m = map(int,input().split())
  print(np.eye(n,m))
eye_identity()


# Array Mathematics
import numpy as np
def array_mathematics():
  n,m = map(int,input().split())
  arr1 = []
  for i in range(n):
    row = list(map(int,input().split()))
    arr1.append(row)
  arr2 = []
  for i in range(n):
    row = list(map(int,input().split()))
    arr2.append(row)
  n1 = np.array(arr1)
  n2 = np.array(arr2)
  print(n1 + n2)
  print(n1 - n2)
  print(n1 * n2)
  print(n1 // n2)
  print(n1 % n2)
  print(n1**n2)
array_mathematics()



# Floor, Ceil and Rint
# Floor, Ceil and Rint
import numpy as np
np.set_printoptions(legacy = '1.13')
def floor_ceil_rint():
  n = np.array(list(map(float,input().split())))
  print(np.floor(n))
  print(np.ceil(n))
  print(np.rint(n))
floor_ceil_rint()



# Sum and Prod
# Sum and Prod
import numpy as np
def sum_prod():
  n,m = map(int,input().split())
  arr = [list(map(int,input().split())) for i in range(n)]
  num = np.array(arr)
  print(np.prod(np.sum(num,axis = 0)))
sum_prod()


# Min and Max
# Min and Max
import numpy as np
def min_max():
  n,m = map(int,input().split())
  arr = [list(map(int,input().split())) for i in range(n)]
  num = np.array(arr)
  print(np.max(np.min(num,axis = 1)))
min_max()


# Mean, Var, and Std
# Mean, Var, and Std
import numpy as np
def mean_var_std():
  n,m = map(int,input().split())
  arr = [list(map(int,input().split())) for i in range(n)]
  num = np.array(arr)
  print(np.mean(num,axis=1))
  print(np.var(num,axis=0))
  print(round(np.std(num,axis = None),11))
mean_var_std()

# Dot and Cross
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Dot and Cross - print matrix product
import numpy as np
def matrix_prod():
  n = int(input())
  n1 = np.array([list(map(int,input().split())) for i in range(n)])
  n2 = np.array([list(map(int,input().split())) for i in range(n)])
  m = np.zeros((n,n),dtype=int)
  for i in range(n):
    for j in range(n):
      m[i][j] = np.dot(n1[i,:],n2[:,j])
  print(m)
matrix_prod()

# Inner and Outer
# Inner and Outer
import numpy as np
def inner_outer():
  n1 = np.array(list(map(int,input().split())))
  n2 = np.array(list(map(int,input().split())))
  print(np.inner(n1,n2))
  print(np.outer(n1,n2))
inner_outer()

# Polynomials
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Polynomials
import numpy as np
def poly():
  coef = list(map(float,input().split()))
  print(np.polyval(coef,float(input())))
poly()

# Linear Algebra
# Linear Algebra
import numpy as np
def det():
  n = int(input())
  matr = [list(map(float,input().split())) for i in range(n)]
  print(round(np.linalg.det(matr),2))
det()

# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    # Write your code here
    count = Counter(candles)
    return(sorted(list(count.values()),reverse = True)[0])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    d = x2 - x1
    if (v1 > v2) and ( d % (v1 - v2) == 0):
      return 'YES'
    else:
      return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    # Write your code here
    r = 5
    likes = r // 2
    for i in range(n-1):
      r = r // 2 * 3
      likes += r // 2
    return likes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    # Write your code here
    def supersum(n):
      tot = 0
      for number in n:
        tot += int(number)
      tot = str(tot)
      if len(tot) == 1:
        return tot
      else: 
        return supersum(tot)
    p = supersum(n) * k
    return supersum(p)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
  # Write your code here
  d = arr[-1]
  i = n - 1
  while i > 0 and arr[i-1] > d:
    arr[i] = arr[i-1]
    print(*arr)
    i -= 1
  arr[i] = d
  print(*arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
  # Write your code here
  for j in range(1,n):
    d = arr[j]
    i = j
    while i > 0 and arr[i-1] > d:
      arr[i] = arr[i-1]
      i -= 1
    arr[i] = d
    print(*arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

