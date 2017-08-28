# a = [1, 11, 21, 1211, 111221,

# "WYSIWYG sequence": 1, "One 1" -> 11, "Two ones" -> 21, "One 2, one 1" -> 1211, so on so forth..

def next_term(current_term):
    current_char = current_term[0]
    count = 0
    next_term = ""
    for char in current_term:
        if char == current_char:
            count += 1
        else:
            next_term += str(count) + current_char
            current_char = char
            count = 1

    next_term += str(count) + current_char
    return next_term

current_term = "1"
for i in range(30):
    current_term = next_term(current_term)

print(len(current_term))

# len(a[30]) = 5808