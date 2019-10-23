#!C:\Users\Vishal\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi, cgitb
print("content-type: text/html\r\n\r\n")

form = cgi.FieldStorage()

if form.getvalue('maths'):
    math_flag="ON"
else:
    math_flag="OFF"

if form.getvalue('physics'):
    physics_flag="ON"
else:
    physics_flag="OFF"

print("<html>")
print("<body>")
print("<h2>Checkbox math is : %s</h2>" % math_flag)
print("<h2>Checkbox physics is : %s</h2>" % physics_flag)
print("</html>")
print("</body>")