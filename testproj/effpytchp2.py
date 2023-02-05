# effective python - chapter 2 functions

# item 14: prefer exceptions to returning None
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid Inputs") from e


x = 5
y = 0

try:
    result = divide(x, y)
except ValueError:
    print("Invalid Inputs")
else:
    print("Result = ", result)

# item 16 consider	Generators	Instead	of	Returning	Lists

# nicht so performant
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index,letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

# performanter / besser
def index_words_iter(text):
    if text:
        yield 0
    for index,letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = "Four score and seven years ago..."
result = index_words(address)
result2 = list(index_words_iter(address))
print (result[:3])
print (result2[:3])
