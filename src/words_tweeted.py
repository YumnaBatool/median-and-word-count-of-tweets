f = open("tweet_input/tweets.txt", "r")                             #opening tweets.txt file
tweet = f.read()                                                    #reading tweets from the text file
words = tweet.split()                                               #spliting tweet words by white space
WordFrequency = {}                                                  #initializing dict to store word frequencies

for word in words:                                                  #loop for each word in text file
    if word in WordFrequency.keys():                                #if word is present in keys of dict
        WordFrequency[word] += 1                                    #increment its value by 1
    else:                                                           #if word is not present in keys of dict 
        WordFrequency[word] = 1                                     #place it in dict as key with value = 1

keylist = WordFrequency.keys()                                      #saving words from dict keys in a keylist
keylist.sort()                                                      #sorting dict keys alphabetically

fname = "tweet_output/ft1.txt"                                      #defining name of output file
f = open(fname, 'w')                                                #opening output file
for key in keylist:                                                 #loop for every word in keylist
    f.write(key + ": " + str(WordFrequency[key]) + "\n")            #writing each word and its frequency in single line
f.close()                                                           #closing the file
