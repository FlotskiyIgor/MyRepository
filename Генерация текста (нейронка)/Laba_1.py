import string
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
figsize(10, 10)
# инструмент для визуализации многомерных данных.
from sklearn.manifold import TSNE
import gensim.downloader as api
import nltk
from nltk.corpus import brown
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

model = api.load("word2vec-ruscorpora-300")
nltk.download("brown")

print ("Введите слово для поиска")
word = str(input())+"_NOUN"

result=model.most_similar(positive=[word])

main_word=word.replace("_NOUN", "")
plt.scatter(main_word, 1)

plt.title("Cхожесть по словарю")
plt.xticks(rotation = 35)
from translate import Translator
translator= Translator(from_lang="russian",to_lang="english")
#Вывод схожих слов
translation_list = []
for x in result: 
    only_word=x[0].replace("_NOUN", "")
    only_word=only_word.replace("_ADJ", "")
    only_word=only_word.replace("_VERB", "")
    only_word=only_word.replace("_ADV", "")
    only_word=only_word.replace("_INTJ", "")
    check1 =':' in only_word
    check2 =' ' in translator.translate(only_word)
    if (check1 == False and check2 == False):
        print ("Найдено слово: ",only_word, ". Коэф. схожести:", x[1])
        plt.scatter(only_word, x[1])
        translation = translator.translate(only_word)
        string.punctuation
        #пунктуацию будем удалять в цикле
        for p in string.punctuation:
            if p in translation:
                #замена символа в строке
                translation = translation.replace(p, '')
        translation_list.append(translation.lower())
        
print ("Google translate")
print (translation_list)

plt.show()
 
#Переходим к другой библиотеке для работы с английским словарем и создадим модель

document = brown.sents()
data = []
for sent in document:
  new_sent = []
  for word in sent:
    new_word = word.lower()
    if new_word[0] not in string.punctuation:
      new_sent.append(new_word)
  if len(new_sent) > 0:
    data.append(new_sent)
 
# Creating Word2Vec
model = Word2Vec(
    sentences = data,
    vector_size = 50,
    window = 10,
    epochs = 20,
)

# Vector for word
print("Вектор для слова:", main_word)
print(model.wv[translator.translate(main_word)])
print()

#сменим язык
translator= Translator(from_lang="english",to_lang="russian")

#Visualizing data
words = translation_list
print ('Все переведенные слова', words)
#Удалим слова, которых нет в Базе модели
for i in range(5):
    for word in words:
        check3 = word in model.wv.key_to_index
        if (check3==False):
            words.remove(word)
            print('В словаре нет слова: ', word)
print(words)
for word in words:
    print("Многомерный вектор для слова:", translator.translate(word))
    print(model.wv[word])

X = model.wv[words]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
 
pyplot.scatter(result[:, 0], result[:, 1])
for i, word in enumerate(words):
    pyplot.annotate(translator.translate(word), xy=(result[i, 0], result[i, 1]))
pyplot.title("Многомерные вектора в представлении плоскости")
pyplot.show()

# Переводим в TSNE

embed = TSNE(n_components=2)
ax = plt.axes()
    
for word in words:
    print("TSNE: ", translator.translate(word))
    double_vec = model.wv[word].reshape(2,-1) 
    double_vec = embed.fit_transform(double_vec)
    print(double_vec)
    ax.arrow(double_vec[0][0], double_vec[0][1], double_vec[1][0]-double_vec[0][0], double_vec[1][1]-double_vec[0][1], fc='lightblue', 
ec='black', width = 150, head_length = 150)
    plt.annotate(translator.translate(word), xy = (double_vec[1][0], double_vec[1][1]))
    
plt.grid()

pyplot.title("TSNE, 2D Вектора")
pyplot.show()





