#!C:\Users\Vishal\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import pymysql

print("Content-Type: text/html \r\n\r\n")
form = cgi.FieldStorage()

con=pymysql.connect(host="localhost", user="root", password="", database="cgidemo")
cur=con.cursor()
insert_query="""insert into cric_info (name, country, batting_style, avg, runs, matches) values (%s, %s, %s, %s, %s, %s);"""
insert_values=(form.getvalue('fname'),form.getvalue('country'),form.getvalue('batting_Style'),form.getvalue('average'),form.getvalue('runs'),form.getvalue('matches'))
cur.execute(insert_query,insert_values)
con.commit()
con.close()
print("""
<html>
    <title>CGI script python </title>
    <body>
        <h4>Record stored succesfully...</h4>
        <a href="/cric/insert.html">Go back to Insert</a>
    </body>
</html>
""")