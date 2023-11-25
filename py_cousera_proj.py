punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
def get_pos(x):
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())  
    x=x.lower()
    for i in x:
        if i=="!" or i=="#":
            x=x.replace(i," ")
    x=x.split(" ")
    sum_pos=0
    for i in range(len(x)):
        if x[i] in positive_words:
            sum_pos+=1
    return sum_pos

def get_neg(x):
    negative_words = []
    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())  
    x=x.lower()
    for i in x:
        if i=="." or i==",":
            x=x.replace(i," ")
    x=x.split(" ")
    sum_neg=0
    for i in range(len(x)):
        if x[i] in negative_words:
            sum_neg+=1
    return sum_neg

f = open("project_twitter_data.csv", "r")
data=f.read()
neg=0
pos=0
for i in data:
    neg+=get_neg(i)
    pos+=get_pos(i)
net=pos-neg
ne = str(neg)
po = str(pos)
netd = str(net)
filer = open('resulting_data.csv','w')
result = filer.write('Number of Retweets, Number of Replies, Positive Score, Negtive Score, Net Score\n')
result = filer.write('0, 0, ' + ne +', ' + po +", " + netd + '\n')