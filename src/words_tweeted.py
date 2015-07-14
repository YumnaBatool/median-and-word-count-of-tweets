f = open("tweet_input/tweets.txt", "r")
tweet = f.read()
words = tweet.split()
WordFrequency = {}

for word in words:
    word = word.lower()
    if word in WordFrequency.keys():
        WordFrequency[word] += 1
    else:
        WordFrequency[word] = 1

keylist = WordFrequency.keys()
keylist.sort()

fname = "tweet_output/ft1.txt"
f = open(fname, 'w')
for key in keylist:
    f.write(key + ": " + str(WordFrequency[key]) + "\n")
f.close()
