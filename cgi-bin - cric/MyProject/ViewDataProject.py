#!C:\Users\Vishal\AppData\Local\Programs\Python\Python37-32\python.exe
import pymysql
print("Content-Type: text/html \r\n\r\n")
#To run this progrm on web - http://localhost/cgi-bin/cric/ViewData.py
con=pymysql.connect(host="localhost", user="root", password="", database="DairyProduct")
cur=con.cursor()
cur.execute("select * from Product_Data;")
data=cur.fetchall()

print("""<table border="1" >
<tr>
    <th>Id</th>
    <th>Amul_Cheese</th>
    <th>Amul_Butter</th>
    <th>Amul_Ghee</th>
    <th>Gowardhan_Cheese</th>
    <th>Gowardhan_Butter</th>
    <th>Gowardhan_Ghee</th>
    <th>Britannia_Cheese</th>
    <th>Britannia_Butter</th>
    <th>Britannia_Ghee</th>
    <th>Gokul_Cheese</th>
    <th>Gokul_Butter</th>
    <th>Gokul_Ghee</th>
    <th>DairyCraft_Cheese</th>
    <th>DairyCraft_Butter</th>
    <th>DairyCraft_Ghee)(Amul_Cheese</th>
    <th>Amul_Butter</th>
    <th>Amul_Ghee</th>
    <th>Gowardhan_Cheese</th>
    <th>Gowardhan_Butter</th>
    <th>Gowardhan_Ghee</th>
    <th>Britannia_Cheese</th>
    <th>Britannia_Butter</th>
    <th>Britannia_Ghee</th>
    <th>Gokul_Cheese</th>
    <th>Gokul_Butter</th>
    <th>Gokul_Ghee</th>
    <th>DairyCraft_Cheese</th>
    <th>DairyCraft_Butter</th>
    <th>DairyCraft_Ghee</th>
</tr>
""")

for Id, Amul_Cheese, Amul_Butter, Amul_Ghee, Gowardhan_Cheese, Gowardhan_Butter, Gowardhan_Ghee, Britannia_Cheese, Britannia_Butter, Britannia_Ghee, Gokul_Cheese, Gokul_Butter, Gokul_Ghee, DairyCraft_Cheese, DairyCraft_Butter, DairyCraft_Ghee in data:
    print("""<tr>
    <th>{}</th>
    <th>{}</th>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    </tr>""".format(Id, Amul_Cheese, Amul_Butter, Amul_Ghee, Gowardhan_Cheese, Gowardhan_Butter, Gowardhan_Ghee, Britannia_Cheese, Britannia_Butter, Britannia_Ghee, Gokul_Cheese, Gokul_Butter, Gokul_Ghee, DairyCraft_Cheese, DairyCraft_Butter, DairyCraft_Ghee))

print("""
    
</table>""")



con.close()
