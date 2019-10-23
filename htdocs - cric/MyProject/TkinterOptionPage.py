#My Dairy product project

from tkinter import *
import numpy as np
import mysql.connector as conn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlalchemy
from openpyxl.workbook import Workbook

def ShowDataPIE():
    con=conn.connect(host="localhost",
                         user="root",
                         passwd="",
                         database="DairyProduct")
    sql1="select count(*) from Product_Data where Amul_Cheese='Amul_Cheese';"
    sql2="select count(*) from Product_Data where Amul_Butter='Amul_Butter';"
    sql3="select count(*) from Product_Data where Amul_Ghee='Amul_Ghee';"
    sql4="select count(*) from Product_Data where Gowardhan_Cheese='Gowardhan_Cheese';"
    sql5="select count(*) from Product_Data where Gowardhan_Butter='Gowardhan_Butter';"
    sql6="select count(*) from Product_Data where Gowardhan_Ghee='Gowardhan_Ghee';"
    sql7="select count(*) from Product_Data where Britannia_Cheese='Britannia_Cheese';"
    sql8="select count(*) from Product_Data where Britannia_Butter='Britannia_Butter';"
    sql9="select count(*) from Product_Data where Britannia_Ghee='Britannia_Ghee';"
    sql10="select count(*) from Product_Data where Gokul_Cheese='Gokul_Cheese';"
    sql11="select count(*) from Product_Data where Gokul_Butter='Gokul_Butter';"
    sql12="select count(*) from Product_Data where Gokul_Ghee='Gokul_Ghee';"
    sql13="select count(*) from Product_Data where DairyCraft_Cheese='DairyCraft_Cheese';"
    sql14="select count(*) from Product_Data where DairyCraft_Butter='DairyCraft_Butter';"
    sql15="select count(*) from Product_Data where DairyCraft_Ghee='DairyCraft_Ghee';"
    List1=[]
    cur=con.cursor()
    cur.execute(sql1)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql2)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql3)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql4)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql5)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql6)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql7)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql8)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql9)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql10)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql11)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql2)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql13)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql14)
    data=cur.fetchall()
    List1.append(data[0])
    cur.execute(sql15)
    data=cur.fetchall()
    List1.append(data[0])
    print(List1)
    df=pd.DataFrame(List1,columns=["Count"])
    print(df)
    #DataFrame=pd.read_sql(sql1,db)
    #print(DataFrame)
    #print(data)
    #print(data[0])
    #List1=[]
    #List1.append(data[0])
    #print(List1)
    Brands= ['Amul_Cheese','Amul_Butter','Amul_Ghee','Gowardhan_Cheese','Gowardhan_Butter','Gowardhan_Ghee','Britannia_Cheese','Britannia_Butter','Britannia_Ghee','Gokul_Cheese','Gokul_Butter','Gokul_Ghee','DairyCraft_Cheese','DairyCraft_Butter','DairyCraft_Ghee']
    #count1=data
    exp=np.full((15,),0.2)
    plt.pie(List1,labels=Brands,autopct='%1.1f%%',shadow=True,radius=1.3,explode=exp)
    #Count = [1.2,2.2,8.8,8,7.7,6.7]
    #colors = ["red","yellow","blue","pink","orange","green"]

    #explode = (0.1,0,0,0,0,0)
    #plt.pie(popularity, explode=explode, labels=languages, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.show()
    
def ShowDataExcel():
    db=conn.connect(host="localhost",
                         user="root",
                         passwd="",
                         database="DairyProduct")
    sql1="select * from Product_Data;"
    DataFrame=pd.read_sql(sql1,db)
    print(DataFrame)
    DataFrame.to_excel("ProductData.xlsx",sheet_name="Data")
    sql2="select * from B_Char;"
    DataFrame=pd.read_sql(sql2,db)
    print(DataFrame)
    DataFrame.to_excel("ProductChar.xlsx",sheet_name="Product characteristics")
    print("Data is inserted")

Win=Tk()
Win.geometry('700x700+200+20')
Win.title("Show data of products")

FormTitle=Label(Win,text="Show data options",width=20,font=("bold",20))
FormTitle.place(x=200,y=50)

ShowData = Button(Win,text="ShowData in excel",bg='brown',fg='white',font=("bold",13),width=40,command=ShowDataExcel)
ShowData.place(x=180,y=150)

ShowDataPIE = Button(Win,text="ShowData in PE",bg='brown',fg='white',font=("bold",13),width=40,command=ShowDataPIE)
ShowDataPIE.place(x=180,y=250)

ShowDataB = Button(Win,text="ShowData in excel",bg='brown',fg='white',font=("bold",13),width=40)
ShowDataB.place(x=180,y=350)

ShowDataQ = Button(Win,text="ShowData in excel",bg='brown',fg='white',font=("bold",13),width=40)
ShowDataQ.place(x=180,y=450)
Win.mainloop()
