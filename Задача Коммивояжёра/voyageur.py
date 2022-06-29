import random
import tkinter as tk
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
import itertools
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import mode
import numpy as np
import openpyxl

def download_from_file():    
    table = openpyxl.reader.excel.load_workbook(filename="weigh.xlsx")
    table.active = 0
    sheet = table.active
    i=1
    global weight
    weight = []
    while i in range(17):
        weight.append([sheet['A'+str(i)].value,sheet['B'+str(i)].value,sheet['C'+str(i)].value])
        i=i+1
    del weight[0]

    print("Загружен из файла: ", weight)
    global check_download
    check_download = True
   
def generate():
    global check_download
    check_download = False
    check_errors()
    #создать каркас
    ribs = int(Ncities.get()) - 1
    sum_ribs = ribs
    while (ribs != 0):   
        ribs = ribs - 1
        sum_ribs = sum_ribs + ribs
        
    global weight
    weight = ['123']
    i=0
    while (sum_ribs != 0):
        i=i+1
        for j in range(i):
            weight.append([str(int(Ncities.get())-i)+"-"+str(int(Ncities.get())-j), 0, 0])
            print(sum_ribs)
            sum_ribs = sum_ribs - 1
    del weight[0]
    weight.reverse()
    

    #заполнить каркас
    print ('Сгенерированные веса путей (путь, вес, феромоны)')
    for elements in weight:
        elements[1] = random.randint(5, 50)
        elements[2] = random.randint(1, 3) 
        print (elements)
    res = tk.Label(win, text = "Сгенерированные веса путей:")
    res.grid(row = 0, column = 1)
    k=1;
    
    for i in weight:
       view_weight = tk.Label(win, text = ('Путь: '+ str(i[0])+ ', Вес: '+ str(i[1]))+', Феромоны: '+str(i[2]))
       view_weight.grid(row = k, column = 1)
       k=k+1
    
def check_errors(): #проверяет сгенерированы ли данные
    
    try:
        weight[0][1]
    except:
        messagebox.showerror("ОШИБКА", "Сгенерируйте данные")

    #Проверим ломает ли Полина Валерьевна нашу программу
    try:
        int(N.get())
        int(Ncities.get())
        float(beta.get())
        float(alpha.get())
        float(z.get())
        
        if (check_download==False):     
            if (int(Ncities.get()) < 3 or int(Ncities.get())>9):
                messagebox.showerror("ОШИБКА", "Неккоректное кол-во городов (3-9!)")
            
    except:
        messagebox.showerror("ОШИБКА", "Неккоректные данные, попробуйте другие")
 
#метод расчета пути L (принимает на вход последовательность вершин)
def calculate(way):
    if (check_download == False):
        num = int(Ncities.get())
    else:
        num = 6
    distantse = int(0)
    for i in range(int(num)-1):
        text = way[i]+'-'+way[i+1]
        for elements in weight:
            if (elements[0] == text):
                distantse += elements[1]
        text = way[i+1]+'-'+way[i]
        for elements in weight:
            if (elements[0] == text):
                distantse += elements[1]
    return distantse
    
#метод перемешивания двух случайных вершин пути
def revers(way):
    new_way = ''
    default = []
    if (check_download == False):
        num = int(Ncities.get())
    else:
        num = 6
    for i in range(num):
        default.append(way[i])
    check = 0
    while(check != 1):
            a = random.randint(1,num-1)
            b = random.randint(1,num-1)
            if (a!=b): check = 1
    default [a], default [b] = default [b], default [a] 
    for i in range(num):
        new_way += default[i]
    new_way = new_way + '1'
    return new_way

def most_frequent(List):
    
    val, count = mode(List, axis = 0)
    return val.ravel().tolist()


def edit_pheromone(way, long_way):
    if (float(z.get())>1 or float(z.get())<0):
        messagebox.showerror("ОШИБКА", "Неккоректная забывчивость феромона. Значение должны быть (0-1)")
    Q = 150
    delta_t = Q/long_way
    need_to_edit = []
    for cityes in range(6):
        need_to_edit.append(str(way[cityes])+'-'+str(way[cityes+1]))
        need_to_edit.append(str(way[cityes+1])+'-'+str(way[cityes]))
    for elements in range(14):
        if (weight[elements][0] in need_to_edit):
            #умножим на 0,9 - коэфициент забываемости старых феромонов
            weight[elements][2]=round((float(z.get())*weight[elements][2])+delta_t, 2)
    #print('Феромоны изменились', weight)
    #print('Феромоны изменились на ', round(delta_t, 2))
         
def monte_carlo_method(): 
    if (check_download == False):      
        check_errors()
    
    default=""
    num = 0
    if (check_download == False):
        num = int(Ncities.get())
    else:
        num = 6
    for i in range(num):
        default = default + str(i)
    default = default[1:]
    default = default + Ncities.get() + "1"
    
    shourt_way = default
    L = calculate(shourt_way)
    print ('Начальный путь: ', shourt_way)
    print ('Длина нач. пути: ', L)
    temp = 100
    e = 2.71
    while (temp > 0.000000005): #пока температура не упадет максимально близко к 0
        #Найдем длину нового проверяемого пути
        example = revers(shourt_way)
        L_new = calculate(example)
        if (L_new < L):
            shourt_way = example
            L = L_new
            print('Новый путь shourt_way: ', example)
            print('Путь укорочен, L: ', L)
        #т.к. алгоритм не "жадный", даем возможность большему пути на прохождение дальше   
        else:
            P = 100*e**(-(L_new-L)/temp)
            #Генерируем случайное число 1-100 для сравнения (Если P больше случ. ч-ла то берем путь)
            if (P>random.randint(1, 100)):
                shourt_way = example
                L = L_new
                print('Алгоритм принял более длинный путь')
                print('Новый путь shourt_way: ', example)
                print('Путь L: ', L)
         #снижаем температуру в два раза 
        temp = 0.5*temp 
        print('Температура: ', temp)
    print('Кратчайший путь: ', shourt_way)
    print('Длина пути: ', L)
    draw_graphic(shourt_way, 'Метод отжига')
    
def colony_optimization():
    print()
    print ('Муравьиный алгоритм')
        
    check_errors()
    
    #Создадим список путей муравьев
    all_ways = [] 
    
    num = 0
    if (check_download == False):
        num = int(Ncities.get())-1
    else:
        num = 6
        
    for muravey in range(int(N.get())): #возьмем 100 муравьев
       
        now_city = '1' #город в котором находится муравей в данный момент времени
        stop_cities = ['7'] #массив городов в которых уже были
        for i in range(num-1): #выбор ребра, 1го, 2го ... 6го
            maybe_ways = []#возможные пути
            for element in weight:
                if (element[0][0]==now_city or element[0][2]==now_city):
                    if (element[0][2] not in stop_cities and element[0][0] not in stop_cities):
                        maybe_ways.append(element)
            print('Возможные пути: ', maybe_ways)
            
            ways = [] #массив шансов встать на путь
           
            #чем больше значение, тем меньше значимость
            #alpha "Чутье" короткого пути
            #beta "Чутье" феромона
            
            sum_ost = float(0)
            for k1 in range(len(maybe_ways)): #выбор 1-й дороги (вычисляется сумма для формулы)
                sum_ost = sum_ost + maybe_ways[k1][2]/maybe_ways[k1][1]     
                     
            for first in range(len(maybe_ways)):
                #P - это шанс пойти ну одну из дорог
                P = (100*((1/maybe_ways[first][1])**float(alpha.get()))*(maybe_ways[first][2])**float(beta.get()))/sum_ost
                ways.append([round(P, 2),maybe_ways[first][0]])
                print ('Шансы пойти на путь ', ways[first])
    
            r=random.randint(1,99)
            print('Сгенерировано: ', r)
            #Создадим массив из границ отрезков
            mas_offcut = []
            
            mas_offcut.append(0)
            
            fix = 0
            for j in range(len(maybe_ways)-1):
                mas_offcut.append(fix + ways[j][0])
                fix = fix + ways[j][0]
                
            mas_offcut.append(100)  
    
            print('Границы отрезков: '+ str(mas_offcut))
            
            next_city = [[],[]] #хранит значение следующего города (куда пойдем)
            
            for j in range(len(maybe_ways)):
                if (mas_offcut[j]<=r<=mas_offcut[j+1]):
                    if (mas_offcut[j]==0):
                        next_city = maybe_ways[0]
                        
                    if (mas_offcut[j+1]==100):
                        next_city = ways[j]
                    else:
                        next_city = ways[j]
                        
            print('Случайно взвешенно выбран путь: ', next_city)
    
    
            stop_cities.append(now_city)
            if (next_city[1][2] != now_city):
                now_city = next_city[1][2]
            else:
                now_city = next_city[1][0]
                
        stop_cities.append(now_city)
        stop_cities.append('1')
        stop_cities.remove('7')
        
        result = ''
        for cityes in stop_cities:
            result = result+cityes
        
        all_ways.append([result, calculate(result)])
        print('Муравей №:', muravey, 'Пройден путь: ', result, 'Длина пути: ', calculate(result))
        edit_pheromone(result, calculate(result))
    print('Самый частый путь муравьев: ', most_frequent(all_ways))
    draw_graphic(most_frequent(all_ways)[0], 'Муравьиный алгоритм')

def draw_graphic(shourt_way, title): #отрисовка
    A = 1
    result = []
    for i in range(0, len(shourt_way), A):
        result.append(int(shourt_way[i : i + A]))
    graph = nx.Graph()
    G=nx.Graph()
    G2=nx.Graph()
    for i in range(0,len(result)):
        graph.add_node(str(result))
        graph.nodes()
    
    def add_edge(f_item, s_item, graph=True):
        graph.add_edge(f_item, s_item)
        graph.add_edge(s_item, f_item) 
    
    cities = {1,2,3,5,6,4}

    G.add_nodes_from(cities)
    for i in range (6):
       for k in range(6):
         G.add_edge(i+1 ,k+1, graph=graph)
         nx.draw_circular(G,
         node_color='white',
         node_size=500,
         edge_color='green',
         with_labels=True)
    
    cities = {1,2,3,5,6,4}
    G2.add_nodes_from(cities)
         
         
    for i in range(0,len(result)):
        nx.draw_circular(G,
         node_color='white',
         node_size=500,
         edge_color='green',
         with_labels=True)
        G2.add_edge(result[i-1], result[i] , graph=graph)
        nx.draw_circular(G2,
             node_color='white',
             node_size=500,
             edge_color= 'red',
             with_labels=True)
    plt.title(title)
    plt.show()    
    
win = tk.Tk()
win.title("Задача коммивояжёра")
win.geometry("800x400")

lbl = ttk.Label(win, text = "Количество муравьев:").grid(column = 0, row = 1) 
N = tk.StringVar() 
NEntered = ttk.Entry(win, width = 12, textvariable = N).grid(column = 0, row = 2)

lb2 = ttk.Label(win, text = "Альфа(Чутье пути, степень):").grid(column = 0, row = 3) 
alpha = tk.StringVar()  
alphaEntered = ttk.Entry(win, width = 12, textvariable = alpha).grid(column = 0, row = 4)
 
lb2 = ttk.Label(win, text = "Бета(Чутье феромонов, степень):").grid(column = 0, row = 5)
beta = tk.StringVar()  
betaEntered = ttk.Entry(win, width = 12, textvariable = beta).grid(column = 0, row = 6)

lb2 = ttk.Label(win, text = "Колличество городов(3-9):").grid(column = 0, row = 7) 
Ncities = tk.StringVar()  
NcitiesEntered = ttk.Entry(win, width = 12, textvariable = Ncities).grid(column = 0, row = 8)

lb2 = ttk.Label(win, text = "Забывчивость феромона (0-1):").grid(column = 0, row = 9)
z = tk.StringVar()  
zEntered = ttk.Entry(win, width = 12, textvariable = z).grid(column = 0, row = 10)

generate_but = Button(text="Сгенерировать", command = generate).grid(row=11, column=0)

download_but = Button(text="Загрузить из файла", command = download_from_file).grid(row=12, column=0)

fire_but = Button(text="Метод отжига", command = monte_carlo_method).grid(row=13, column=0)
Colony_but = Button(text="Муравьиный алгоритм", command = colony_optimization).grid(row=14, column=0)
win.mainloop()






