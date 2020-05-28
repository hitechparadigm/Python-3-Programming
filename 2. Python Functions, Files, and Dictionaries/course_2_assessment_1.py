# 1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the file and save to the variable num
f = open("travel_plans.txt")
num = len(f.read())
print(num)

# 2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words
num_words = 0
fileref = "emotion_words.txt"

with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())

print("number of words : ", num_words)

# 3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.
fileref = "school_prompt.txt"
with open(fileref, 'r') as file:
    num_lines = len(file.readlines())

# 4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
fileref = "school_prompt.txt"
with open(fileref, 'r') as file:
    beginning_chars = file.read()[:30]

# 5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
fileref = "school_prompt.txt"
three = []
with open(fileref, 'r') as file:
#    three = [line.split()[2] for line in f]

    for line in file:
        word = line.split()[2]
        three.append(word)

        print(line)
        print(three)

# 6. Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
fileref = "emotion_words.txt"
emotions = []
with open(fileref, 'r') as file:
    for line in file:
        word = line.split()[0]
        emotions.append(word)

# 7. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
f = open("travel_plans.txt")
first_chars = f.read()[:33]

# 8. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
fileref = open("school_prompt.txt")
words = fileref.read().split()
p_words = [word for word in words if 'p' in word]