import nltk
f = open('F:\ppp.txt')
ff = f.read()
ttt = nltk.word_tokenize(ff)
print(ttt[3])
for kkkkk in ttt:
    print(kkkkk)