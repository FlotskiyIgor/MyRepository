import tkinter as tk
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import xlwings as xw
import pandas as pd
import openpyxl
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import r2_score
import matplotlib.image as mpimg
from PIL import ImageTk, Image 
global check1
check1= float(0)
global check2
check2= float(0)

def load_file():
    
    root = tk.Tk()
    root.withdraw()
    try:      
        global file_path
        file_path = filedialog.askopenfilename()
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        
    except:
        messagebox.showerror("ОШИБКА", "Неккоректный файл. Выберите документ .xlsx")
    #define our column
    table['columns'] = (sheet['A1'].value, sheet['B1'].value, sheet['C1'].value, sheet['D1'].value, sheet['E1'].value,sheet['F1'].value,sheet['G1'].value,sheet['H1'].value,sheet['I1'].value,sheet['J1'].value,sheet['K1'].value,sheet['L1'].value,sheet['M1'].value)
    
    # format our column
    table.column("#0", width=0,  stretch=NO)
    table.column(sheet['A1'].value,anchor=CENTER, width=80)
    table.column(sheet['B1'].value,anchor=CENTER, width=80)
    table.column(sheet['C1'].value,anchor=CENTER, width=80)
    table.column(sheet['D1'].value,anchor=CENTER, width=80)
    table.column(sheet['E1'].value,anchor=CENTER, width=80)
    table.column(sheet['F1'].value,anchor=CENTER, width=80)
    table.column(sheet['G1'].value,anchor=CENTER, width=80)
    table.column(sheet['H1'].value,anchor=CENTER, width=80)
    table.column(sheet['I1'].value,anchor=CENTER, width=80)
    table.column(sheet['J1'].value,anchor=CENTER, width=80)
    table.column(sheet['K1'].value,anchor=CENTER, width=80)
    table.column(sheet['L1'].value,anchor=CENTER, width=80)
    table.column(sheet['M1'].value,anchor=CENTER, width=80)
    
    #Create Headings 
    table.heading("#0",text="",anchor=CENTER)   
    table.heading(sheet['A1'].value,text=sheet['A1'].value,anchor=CENTER)
    table.heading(sheet['B1'].value,text=sheet['B1'].value,anchor=CENTER)
    table.heading(sheet['C1'].value,text=sheet['C1'].value,anchor=CENTER)
    table.heading(sheet['D1'].value,text=sheet['D1'].value,anchor=CENTER)
    table.heading(sheet['E1'].value,text=sheet['E1'].value,anchor=CENTER)
    table.heading(sheet['F1'].value,text=sheet['F1'].value,anchor=CENTER)
    table.heading(sheet['G1'].value,text=sheet['G1'].value,anchor=CENTER)
    table.heading(sheet['H1'].value,text=sheet['H1'].value,anchor=CENTER)
    table.heading(sheet['I1'].value,text=sheet['I1'].value,anchor=CENTER)
    table.heading(sheet['J1'].value,text=sheet['J1'].value,anchor=CENTER)
    table.heading(sheet['K1'].value,text=sheet['K1'].value,anchor=CENTER)
    table.heading(sheet['L1'].value,text=sheet['L1'].value,anchor=CENTER)
    table.heading(sheet['M1'].value,text=sheet['M1'].value,anchor=CENTER)


    #add data 
    for i in range(2,200):
        table.insert(parent='',index='end',iid=i,text='',
        values=(sheet['A'+str(i)].value,sheet['B'+str(i)].value,sheet['C'+str(i)].value,sheet['D'+str(i)].value,sheet['E'+str(i)].value,sheet['F'+str(i)].value,sheet['G'+str(i)].value,sheet['H'+str(i)].value,sheet['I'+str(i)].value,sheet['J'+str(i)].value,sheet['K'+str(i)].value,sheet['L'+str(i)].value,sheet['M'+str(i)].value))  
    table.pack()
    
    
def regression():

    #read data frame
    df = pd.read_excel(file_path)
    df = df.dropna()
    
    #drop text columns
    df1 = df.drop('institution', axis = 1)     
    df1 = df1.drop('country', axis = 1)
    
    #lower size to 2 columns
    x = StandardScaler().fit_transform(df1)
    
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(x)
    principalDf = pd.DataFrame(data = principalComponents
    , columns = ['X', 'Y'])
    
    #print to console new table
    print(principalDf.head(5))
    
    corel = principalDf['X'].cov(principalDf['Y'])
    print('Результат корреляции главных параметров: ',corel)

    finalDf = pd.concat([principalDf, df[['institution']]], axis = 1)
    print(finalDf.head(5))
    #send new table to tkinter
    global new_table_frame
    new_table_frame = Frame(win)
    new_table_frame.pack()
    global new_table_scroll
    #scrollbar
    new_table_scroll = Scrollbar(new_table_frame)
    new_table_scroll.pack(side=RIGHT, fill=Y)
    
    new_table_scroll = Scrollbar(new_table_frame,orient='horizontal')
    new_table_scroll.pack(side= BOTTOM,fill=X)
    global new_table
    new_table = ttk.Treeview(new_table_frame,yscrollcommand=new_table_scroll.set, xscrollcommand =new_table_scroll.set)
    
    new_table.pack()
    
    new_table_scroll.config(command=table.yview)
    new_table_scroll.config(command=table.xview)
    
    columns = finalDf.columns
    new_table['columns'] = (columns[0], columns[1], columns[2])
    
    # format our column
    new_table.column("#0", width=0,  stretch=NO)
    new_table.column(columns[0],anchor=CENTER, width=80)
    new_table.column(columns[1],anchor=CENTER, width=80)
    new_table.column(columns[2],anchor=CENTER, width=80)

    #Create Headings 
    new_table.heading("#0",text="",anchor=CENTER)   
    new_table.heading(columns[0],text=columns[0],anchor=CENTER)
    new_table.heading(columns[1],text=columns[1],anchor=CENTER)
    new_table.heading(columns[2],text=columns[2],anchor=CENTER)
      

    #add data 
    for i in range(0,199):
        new_table.insert(parent='',index='end',iid=i,text='',
        values=(finalDf.loc[i]['X'],finalDf.loc[i]['Y'],finalDf.loc[i]['institution']))
        
    new_table.pack()
    
    x = StandardScaler().fit_transform(df1)
    
    plt.axis([-4,7,-4,4])
    plt.title('Расположение данных')

    for index, row in principalDf.iterrows():
        plt.plot(row['X'],row['Y'],'og')

    plt.xlabel('Corelation: '+str(corel)+', Determination: '+str(corel*corel), fontsize=10, color='blue')
    x = principalDf['X']
    y = principalDf['Y']
    
     
    plt.scatter(x, y)
    
    '''
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")
    '''
    
    plt.plot(x,y,"o", ms=5, mec="k")
    z = np.polyfit(x, y, 1)
    y_hat = np.poly1d(z)(x)
    
    plt.plot(x, y_hat, "r--", lw=1)
    text = f"$y={z[0]}\;x{z[1]}$"
    plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
    fontsize=9, verticalalignment='top')

    plt.savefig('plot.png')
    plt.show()
    global lab
    global Label
    img  = Image.open("plot.png") 
    photo=ImageTk.PhotoImage(img)
    lab=Label(image=photo).place(x=25,y=300)
    global check1
    check1 = 1
        
    
    

def search_y():
    global check1
    if check1 == 1:
        x = float(podbor_x.get())
        a = str((1.67690265*10**(-17))*x - 1.350771689*10**(-17))
        lb3.config(text=a)
    else:
        messagebox.showerror("ОШИБКА", "Для начала, проведите регрессию")

def clear():
    for i in table.get_children():
        table.delete(i)
    for i in new_table.get_children():
        new_table.delete(i)
    new_table.heading= ("")
    new_table['columns']= ("")
    new_table.delete()
    new_table_frame.destroy()
    new_table_scroll.destroy()
    new_table.column= ("")
    lb3.config(text=" ")
    
    global lab
    global Label
    img  = Image.open("fon.png") 
    photo=ImageTk.PhotoImage(img)
    lab1=Label(image=photo).place(x=25,y=300)
    global check1
    check1 = 0
    global check2
    сheck2 = 0
        
win = tk.Tk()
win.title("Регрессия")
win.geometry("1200x800")

load_but = Button(text="Загрузить из файла", command = load_file).pack()

win['bg'] = '#AC99F2'
table_frame = Frame(win)
table_frame.pack()

#scrollbar
table_scroll = Scrollbar(table_frame)
table_scroll.pack(side=RIGHT, fill=Y)

table_scroll = Scrollbar(table_frame,orient='horizontal')
table_scroll.pack(side= BOTTOM,fill=X)

table = ttk.Treeview(table_frame,yscrollcommand=table_scroll.set, xscrollcommand =table_scroll.set)

table.pack()

table_scroll.config(command=table.yview)
table_scroll.config(command=table.xview)

size_lower_but = Button(text="Регрессия", command = regression).pack()
lb1 = ttk.Label(win, text = "подбор параметра x:")
lb1.place(x=800,y=300)
lb2 = ttk.Label(win, text = "подобранное значение y:")
lb2.place(x=800,y=330)

podbor_x = tk.StringVar() 
podbor_xEntered = ttk.Entry(win, width = 12, textvariable = podbor_x)
podbor_xEntered.place(x=935,y=300)

lab=ttk.Label(win, image= '')
lab.place(x=25,y=300)
lab1=ttk.Label(win, image= '')
lab1.place(x=25,y=300)
lb3 = ttk.Label(win, text = "")
lb3.place(x=950,y=330)

podbor = Button(text="Подбор", command = search_y).pack()
clear_bt = Button(text="Очистка", command = clear).pack()

win.mainloop()
