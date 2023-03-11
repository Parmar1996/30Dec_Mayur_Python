import pymysql

try:
    dbconnect=pymysql.connect(host='localhost',user='root',password='',database='demo')
    print("Database Connected!")

except Exception as e:
    print(e)

cr=dbconnect.cursor()

# Table Created 
tbl_create="create table studentinfo(id  integer primary key auto_increment,name text,sub text,city text)"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

'''# Insert data
u_name=input("Enter Name:-")
u_sub=input("Enter Subject:-")
u_city=input("Enter City:-")
#insert_data="insert into studentinfo(name,sub,city) values(f'{u_name}','{u_sub}','{u_city}')"
insert_data=f"insert into studentinfo(name,sub,city) values ('{u_name}','{u_sub}','{u_city}')"

try:

    cr.execute(insert_data)
    dbconnect.commit()    
    print("Record inserted!")
except Exception as e:
    print(e)'''

'''i=int(input("Enter Id which Record are Deleted :-"))
delete_data=f"delete from studentinfo where id={i}"

try:
    cr.execute(delete_data)
    dbconnect.commit()
    print("Record Deleted!")
except Exception as e:
    print("e")'''

u_name=input("Enter Name:-")
i=int(input("Enter Id which record are Updated :-"))

update_data=f"update studentinfo set name='{u_name}' where id={i}"

try:
    cr.execute(update_data)
    dbconnect.commit()
    print("Record Updated!")

except Exception as a:
    print(e)

select_data="select * from studentinfo"

try:
    cr.execute(select_data)
    x=cr.fetchall()
    print(x)

except Exception as a:
    print(e)
 
