#!C:\Users\Vishal\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi, cgitb
import pymysql

print("content-type: text/html\r\n\r\n")
form=cgi.FieldStorage()

con = pymysql.connect(host="localhost", user="root", password="", database="DairyProduct")
cur=con.cursor()

Brand_Query="""insert into B_Char (Amul, Britania, Gokul, Dairy_Craft, Gowardhan) values (%s, %s, %s, %s, %s);"""

Brand_Value=(form.getvalue('Amul'),form.getvalue('Britania'),form.getvalue('Gokul'),form.getvalue('Dairy_Craft'),form.getvalue('Gowardhan'))

cur.execute(Brand_Query,Brand_Value)
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
