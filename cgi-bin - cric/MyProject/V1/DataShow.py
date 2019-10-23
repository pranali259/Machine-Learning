#!C:\Users\Vishal\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi, cgitb
import pymysql
print("content-type: text/html\r\n\r\n")

form=cgi.FieldStorage()
print("<html>")
print("<body>")
print("<h2>Checkbox checked is : %s</h2>" % form.getvalue('Amul_Cheese'))
print("<h2>Checkbox checked is : %s</h2>" % form.getvalue('GW_Butter'))
print("</body>")
print("</html>")


