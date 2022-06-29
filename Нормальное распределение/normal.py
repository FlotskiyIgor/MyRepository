import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

mu = 20 # среднее значение данных
sigma = 2 # среднее отколенение данных
students = np.random.normal(mu, sigma, 500) # создадим массив и 500 студентов

#Цикл для округления до целого числа возраста в массиве
for index, item in enumerate(students): 
    students[index] = round(students[index])
    
print (students)

#bins - кол-во интервалов
plt.hist(students, density=True, bins=25, label="Ages")

#макс значние x = макс значение кол-ва представителей какого либо возраста
mn, mx = plt.xlim()
plt.xlim(mn, mx)

#не получилась линия
kde_xs = np.linspace(mn, mx, 100)
kde = st.gaussian_kde(students)

#названия
plt.plot(kde_xs, kde.pdf(kde_xs), label="line")
plt.legend(loc="upper left")
plt.ylabel('Amount (плотность)')
plt.xlabel('Ages')
plt.title("Гистограмма");

