import sqlite3
from employee import Employee
from OTP import sending_email

flag = False
con = sqlite3.connect('employee.db')
cursor = con.cursor()

# cursor.execute("""CREATE TABLE employee(
# 				first_name text,
# 				second_name text,
# 				pay int,
# 				email text,
# 				authorized bool DEFAULT False
# 				)""")


e = Employee(input('Enter name: '),input('Enter last name: '),input('Enter salary: '))


# e = Employee('Dmitry','Voljin',6700)

if input("Would you like to like to fully authorize by confurming your email? (Y/N): ") == "Y":
	while flag == False: flag = sending_email(e.set_email()); e.authorized = flag

cursor.execute("""INSERT INTO employee VALUES (?,?,?,?,?)""",(e.first_name,e.last_name,e.payment,e.set_email(),e.authorized))
con.commit()

# cursor.execute("SELECT email FROM employee where email=?", (e.set_email(),))

# print(cursor.fetchone()[0])

# cursor.execute("SELECT email FROM employee")
# print(cursor.fetchall())
# con.commit()
# con.close()


# sending_email('dmitryvoljin@gmail.com')


