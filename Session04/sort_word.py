# Get list of words from input, separated by comma
words = [x for x in input("Enter: ").split(',')]

print("List of words is: ", words)

# A list store word in ASCII type , each element is a list of ASCII numbers
list_of_words_ascii = []

for word in words:
    word = word.replace(' ','')          # Remove white space of word, ' ' has space, '' doesn't
    word_ascii = [ord(character) for character in word]           # Divide word into ASCII codes
    list_of_words_ascii.append(word_ascii)

print()
print("List of words in ASCII code type is: ", list_of_words_ascii)

# Function compare list a and b. In this case a, b is list of int.
# This function will return list have smaller ASCII code
def compare_list(a,b):

    index = 0
    max_index = len(a) if len(a)<len(b) else len(b)         # max index is length of smaller list

    # Finding the first index not equal
    while(a[index] == b[index]):
        index += 1
        # Handle index out of range if list a = list b or a, b contain each other.
        # Ex: [1,2,3] vs [1,2,3,4] ; "war" vs "wars" ; etc
        if (index == max_index):
            return (a if len(a)==max_index else b) #return smaller list

    # This line run is mean a not equal b. Now just return list have smaller value
    if a[index] < b[index]:
        return a
    else:
        return b

# SORTED, store sorted words to list_return
list_return = []
while (len(list_of_words_ascii) > 0):
    
    min_word = list_of_words_ascii[0]                 # Assign min_word to first element
    # Find min_word in list 
    for word in list_of_words_ascii:
        min_word = compare_list(word, min_word)       # if word < min_word -> assign min_word = word

    s = "".join([chr(c) for c in min_word])           # Convert min_word (ASCII code) to string
    list_return.append(s)
    list_of_words_ascii.remove(min_word)              

print()
print("Sorted list is: ", list_return)