import gensim.downloader as api
model = api.load("word2vec-ruscorpora-300")

x = open('example.txt','r')
text = x.readline()
print('Text: ')
print(text)
x.close()

punctuation = ' ,:@.-()/'
 
L = text.split()
for si in punctuation:
    LTemp = []
    n = len(L)
    for i in range(n):
        l = L[i].split(str(si))
        while 1:
            try:
                l.remove('')
            except ValueError:
                break
        #for k in l:
        #    if 
        LTemp = LTemp + l
        if i == n-1:
            L = LTemp[:]
print(L)

f = open('result.txt', 'w')
         
Parts = ['_NOUN', '_ADJ', '_VERB', '_ADV', '_INTJ']
for word in L:
    check = 0;
    for part in Parts:
        try:
            sinonim=model.most_similar(positive=[word+part], topn=1)
            check = 1
            new = sinonim[0][0].replace("_NOUN", "")
            new=new.replace("_ADJ", "")
            new=new.replace("_VERB", "")
            new=new.replace("_ADV", "")
            new=new.replace("_INTJ", "")
            f.write(new+' ')
            print(new)
            break
        except Exception:
            check = check + 1
        if (check == 5):
            print(word)
            f.write(word+' ')
f.close()

        