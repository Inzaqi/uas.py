# python expressions
print("Python Ecpressions:")
# a. 15 mod 5
print(f"a. 15 % 5 = {15 % 5}")
# b. 12 + 3 * 5 == 75
print(f"b. 12 + 3 * 5 == 75 -> {12 + 3 * 5 == 75}")
# c. "PML"+"15523"
print(f'c. "PML"+"15523" = {"PML"+"15523"}')
# d. “100”+234
print(f'd. “100” + 234 -> {"100" + str(234)}')
# e. ((11%3)+2) != 8/2
print(f'e. ((11%3)+2) != 8/2 -> { ((11%3)+2) != 8/2}')

#ekspresi Boolean
print("\nboolean:")
p = 11
q = 5
r = 4
a = ((p-r) == (r+q) )
b = (((p%3)+q)!=(r%2))
c = ((q-3)==(p%2+q))
d = ((r+q)!=((p*2)%2))
e = ((((q%3)+p)>(r%2)))
f = (((r+p))<=(q*5))
print(f'a. {a}')
print(f'b. {b}')
print(f'c. {c}')
print(f'd. {d}')
print(f'e. {e}')
print(f'f. {f}')


#Isian Singkat
print("\nIsian Singkat:")
# 1
print(f'1. “Honey” + “Boo” * 3 = {"Honey" + "Boo" * 3}')
# 2
capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'
print(f'2. capitals["Germany"] = {capitals["Germany"]}')
#3
a = "23"
b=9
print(f'3. a+b -> {a + str(b)}')
#4
letters = ["a", "b", "o", "c", "p"]
print(f'4a. letters[1] = {letters[1]}')
print(f'4b. letters[len(letters)-2] = {letters[len(letters)-2]}')
print(f'4c. letters + [“x”] = {letters + ["x"]}')
print(f'4d. letters = {letters}')
#5
print(f"5. ‘ ‘.join(‘h a n d s’.split()) = {' '.join('h a n d s'.split())}")
#6
import json

json_string = """
[
  {"1": "one", "2": "two", "3": "three"},
  {"1": "un", "2": "deux", "3": "trois"},
  {"1": "eins", "2": "zwei", "3": "drei"}
]
"""
data = json.loads(json_string)
print(f'6. json.loads(json_string)[1]["2"] = {data[1]["2"]}')
#7
def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1

vals = [100, 66, 55, 64, 41, 35, 18, 64]
print(f'7. pembagi_indeks1([100, 66, 55, 64, 41, 35, 18, 64], 5) = {pembagi_indeks1(vals, 5)}')
#8
def mystery(n,m):
    p=0
    e=0
    while p < n :
        p= + 1
        e= 0
    return p
print(mystery(4,3))

