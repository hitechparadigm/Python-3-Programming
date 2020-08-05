def strip_punctuation(word):
    """Strips punctuation from list of words"""
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word


def get_pos(my_input):
    """Count positive words from file"""
    newlist = my_input.split()
    count_pos = 0
    for word in newlist:
        word = strip_punctuation(word)
        word = word.lower()
        if word in positive_words:
            count_pos += 1
    return count_pos


def get_neg(my_input):
    """Count negative words from file"""
    newlist = my_input.split()
    count_pos = 0
    for word in newlist:
        word = strip_punctuation(word)
        word = word.lower()
        if word in negative_words:
            count_pos += 1
    return count_pos

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#reading Twitter file
fileconnection = open("project_twitter_data.csv", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)

#writing resuts to resulting_data.csv
outfile = open("resulting_data.csv", "w")
# output the header row
outfile.write(
    'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

for row in lines[1:]:
    if len(row) < 4:
        continue

    else:
    #row = strip_punctuation(row)
        vals = row.strip().split(',')
        vals[0] = (strip_punctuation(vals[0])).lower()
        print(vals)
        retweet = vals[1]
        reply = vals[2]
        pos_score = get_pos(vals[0])
        neg_score = get_neg(vals[0])
        net_score = pos_score - neg_score


#    for tweet in vals:
        row_string = '{},{},{},{},{}'.format(
            retweet, reply, pos_score, neg_score, net_score)
        #print(row_string)
    
        outfile.write(row_string)
        outfile.write('\n')
            
outfile.close()

