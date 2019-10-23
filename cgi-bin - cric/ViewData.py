#!C:\Users\Vishal\AppData\Local\Programs\Python\Python37-32\python.exe
import pymysql
print("Content-Type: text/html \r\n\r\n")
#To run this progrm on web - http://localhost/cgi-bin/cric/ViewData.py
con=pymysql.connect(host="localhost", user="root", password="", database="cgiinfo")
cur=con.cursor()
cur.execute("select * from cric_info;")
data=cur.fetchall()

print("""<table border="1" >
<tr>
    <th>Id</th>
    <th>Player Name</th>
    <th>Country</th>
    <th>Batting Style</th>
    <th>Average</th>
    <th>Runs</th>
    <th>Matches</th>
</tr>
""")

for no, name, country, bs, avg, runs, match in data:
    print("""<tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td><form method="POST" action="/cric/UpdateForm.py">
        <input type="hidden" name="id" value={}>
         <input type="submit" value="Update">
         </form>
    </td>
    </tr>""".format(no, name, country, bs, avg, runs, match, no))

print("""
    
</table>""")



con.close()
