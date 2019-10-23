#!C:\Users\Vishal\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi, cgitb
import pymysql

print("content-type: text/html\r\n\r\n")
form=cgi.FieldStorage()

con = pymysql.connect(host="localhost", user="root", password="", database="DairyProduct")
cur=con.cursor()

#Use database columns names in below query
insert_query="""insert into Product_Data (Amul_Cheese, Amul_Butter, Amul_Ghee, Gowardhan_Cheese, Gowardhan_Butter, Gowardhan_Ghee, Britannia_Cheese, Britannia_Butter, Britannia_Ghee, Gokul_Cheese, Gokul_Butter, Gokul_Ghee, DairyCraft_Cheese, DairyCraft_Butter, DairyCraft_Ghee) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

#use html value names in below query
insert_value=(form.getvalue('Amul_Cheese'), form.getvalue('Amul_Butter'), form.getvalue('Amul_Ghee'), form.getvalue('GW_Cheese'), form.getvalue('GW_Butter'), form.getvalue('GW_Ghee'), form.getvalue('B_Cheese'), form.getvalue('B_Butter'), form.getvalue('B_Ghee'), form.getvalue('Gokul_Cheese'), form.getvalue('Gokul_Butter'), form.getvalue('Gokul_Ghee'), form.getvalue('DC_Cheese'), form.getvalue('DC_Butter'), form.getvalue('DC_Ghee'))
cur.execute(insert_query,insert_value)
con.commit()
con.close()

print("""
<html>
    <title>CGI script python </title>
    <body>
        <h4>Record stored succesfully...</h4>        
    </body>
</html>
""")
