f = open("tweet_input/tweets.txt", "r")       #opening file tweets.txt
text = f.read()                               #reading tweets from the text file
tweets = text.split("\n")                     #spliting tweets by line break
Unique = []                                   #initiating list for saving unique words count
Medians = []                                  #initiating list for saving median of unique words count

for tweet in tweets:                          #loop for each tweet
    words = tweet.split()                     #spliting each tweet by blank space 
    number = len(set(words))                  #counting unique words in each tweet
    ##print number
    Unique.append(number)                     #saving unique word count in list
    
    sortedUnique = sorted(Unique)             #sorting list for median
    UniqueLen = len(Unique)                   #length of unique words count list
    index = (UniqueLen - 1) // 2              #getting the middle index of list

    if (UniqueLen % 2):                       #if list is of odd numbers
        Medians.append(sortedUnique[index])                                     #middle number is median
    else:                                                                       #if list is of even numbers
        Medians.append((sortedUnique[index] + sortedUnique[index + 1])/2.0)     #mean of two middle numbers

##print Unique
##print Median
        
fname = "tweet_output/ft2.txt"                #defining file name
f = open(fname, 'w')                          #opening file to write output
for Median in Medians:                        #for each median
    f.write(str(Median) + "\n")               #writing median after each tweet in single line
f.close()                                     #closing file
