f = open("tweet_input/tweets.txt", "r")
text = f.read()
tweets = text.split("\n")
Unique = []
Medians = []

for tweet in tweets:
    words = tweet.split()
    number = len(set(words))
    ##print number
    Unique.append(number)
    
    sortedUnique = sorted(Unique)
    UniqueLen = len(Unique)
    index = (UniqueLen - 1) // 2

    if (UniqueLen % 2):
        Medians.append(sortedUnique[index])
    else:
        Medians.append((sortedUnique[index] + sortedUnique[index + 1])/2.0)

##print Unique
##print Median
        
fname = "tweet_output/ft2.txt"
f = open(fname, 'w')
for Median in Medians:
    f.write(str(Median) + "\n")
f.close()
