# effective python chapter 1

# Item 7
# quadriere die Zahlen in einem array
a = [1,2,3,4,5,6,7,8,9,10]
squares = [x ** 2 for x in a]
print (squares)

# das ganze als Lambda Funktion
squares_lambda = map(lambda x: x**2,a)
for i in squares_lambda:
    print(i)

# berechne Quadratwert, nur wenn grade Zahl in der Liste
squares_even = [x ** 2 for x in a if x %2 == 0]
print (squares_even)

# use zip to process iterators in parallel
print ("Use zip to process iterators in parallel")
names = ["Cecilia","Lise","Marie"]
letters = [len(n) for n in names]

# get largest name
max_letters = 0

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

print ("Longest Name", longest_name)
print ("Max letters ", max_letters)

