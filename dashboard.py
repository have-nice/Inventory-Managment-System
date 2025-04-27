from tkinter import *
from employees import employee_form
from supplier import supplier_form
from category import category_form
from products import product_form
from employees import connect_database
import time
#Functionality Part

def update():
    cursor,connection=connect_database()
    if not cursor or not connection:
        return
    cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system;')
    cursor.execute('use inventory_system')
    cursor.execute("CREATE TABLE IF NOT EXISTS employee_data (empid INT PRIMARY KEY, name VARCHAR(100),email VARCHAR(100), gender VARCHAR(50), dob VARCHAR(30), contact VARCHAR(30), employment_type VARCHAR(50), education VARCHAR(50), work_shift VARCHAR(50), address VARCHAR(100), doj VARCHAR(30), salary VARCHAR(50),usertype VARCHAR(50), password VARCHAR(50))")
    cursor.execute('CREATE TABLE IF NOT EXISTS supplier_data (invoice INT PRIMARY KEY,name VARCHAR(100),contact VARCHAR(15),description TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS category_data (id INT PRIMARY KEY,name VARCHAR(100),description TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS product_data (id INT AUTO_INCREMENT PRIMARY KEY,category VARCHAR(100),supplier VARCHAR(100),name VARCHAR(100),price DECIMAL(10,2),quantity INT,status VARCHAR(50))')

    cursor.execute('SELECT * from employee_data')
    emp_records=cursor.fetchall()
    total_emp_count_label.config(text=len(emp_records))


    cursor.execute('SELECT * from supplier_data')
    sup_records = cursor.fetchall()
    total_sup_count_label.config(text=len(sup_records))

    cursor.execute('SELECT * from category_data')
    cat_records = cursor.fetchall()
    total_cat_count_label.config(text=len(cat_records))

    cursor.execute('SELECT * from product_data')
    prod_records = cursor.fetchall()
    total_prod_count_label.config(text=len(prod_records))

    date_time = time.strftime('%I:%M:%S %p on %A, %B %d %Y')
    subtitleLabel.config(text=f'Welcome \t\t\t\t\t\t {date_time}')
    subtitleLabel.after(1000,update)
current_frame=None

def show_form(form_function):
    global current_frame
    if current_frame:
        current_frame.place_forget()
    current_frame=form_function(window)

def close_window():
    window.destroy()

#GUI Part
window=Tk()

window.title('Dashboard')
window.geometry('1280x610+0+0')
window.state('zoomed')
#window.resizable(0,0)
window.resizable(True,True)
window.config(bg='white')

bg_image=PhotoImage(file='inventory.png')
titleLabel=Label(window,image=bg_image,compound=LEFT,text='Inventory Management System  ', font=('times new roman',40, 'bold'),bg='#010c48',fg='white', anchor='w',padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

logoutButton=Button(window,text='logout',font=('times new roman', 20, 'bold'),fg='#010c48')
logoutButton.place(x=1400, y=10)

subtitleLabel=Label(window,text='Welcome Admin\t\t Date: 28-01-2025\t\t Time: 12:44:00 am',font=('times new roman', 15),bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

leftFrame=Frame(window)
leftFrame.place(x=0,y=102,width=270,height=610)

logoImage=PhotoImage(file='logo.png')
imageLabel=Label(leftFrame,image=logoImage)
imageLabel.pack()

menuLabel=Label(leftFrame,text='Menu',font=('times new roman',20),bg='#009688')
menuLabel.pack(fill=X)

employee_icon=PhotoImage(file='employees.png')
employee_button=Button(leftFrame,image=employee_icon,compound=LEFT,text='  Employees',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda :show_form(employee_form))
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file='supplier.png')
supplier_button=Button(leftFrame,image=supplier_icon,compound=LEFT,text='  Suppliers',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:show_form(supplier_form))
supplier_button.pack(fill=X)

category_icon=PhotoImage(file='category.png')
category_button=Button(leftFrame,image=category_icon,compound=LEFT,text='  Categories',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:show_form(category_form))
category_button.pack(fill=X)

products_icon=PhotoImage(file='products.png')
products_button=Button(leftFrame,image=products_icon,compound=LEFT,text='  Products',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:show_form(product_form))
products_button.pack(fill=X)

# sales_icon=PhotoImage(file='sales.png')
# sales_button=Button(leftFrame,image=sales_icon,compound=LEFT,text='  Sales',font=('times new roman',20,'bold'),anchor='w',padx=10)
# sales_button.pack(fill=X)

exit_icon=PhotoImage(file='exit.png')
exit_button=Button(leftFrame,image=exit_icon,compound=LEFT,text='  Exit',font=('times new roman',20,'bold'),anchor='w',padx=10,command=close_window)
exit_button.pack(fill=X)

emp_frame=Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
emp_frame.place(x=500,y=125,height=170,width=280)
total_emp_icon=PhotoImage(file='total_emp.png')
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg='#2C3E50')
total_emp_icon_label.pack()

total_emp_icon_label=Label(emp_frame,text='Total Employees',bg='#2C3E50',fg='white',font=('times new roman',15,'bold'))
total_emp_icon_label.pack()

total_emp_count_label=Label(emp_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
total_emp_count_label.pack()

sup_frame=Frame(window,bg='#8E44AD',bd=3,relief=RIDGE)
sup_frame.place(x=1000,y=125,height=170,width=280)
total_sup_icon=PhotoImage(file='total_sup.png')
total_sup_icon_label=Label(sup_frame,image=total_sup_icon,bg='#8E44AD')
total_sup_icon_label.pack()

total_sup_icon_label=Label(sup_frame,text='Total Suppliers',bg='#8E44AD',fg='white',font=('times new roman',15,'bold'))
total_sup_icon_label.pack()

total_sup_count_label=Label(sup_frame,text='0',bg='#8E44AD',fg='white',font=('times new roman',30,'bold'))
total_sup_count_label.pack()

cat_frame=Frame(window,bg='#27AE60',bd=3,relief=RIDGE)
cat_frame.place(x=500,y=310,height=170,width=280)
total_cat_icon=PhotoImage(file='total_cat.png')
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg='#27AE60')
total_cat_icon_label.pack()

total_cat_icon_label=Label(cat_frame,text='Total Categories',bg='#27AE60',fg='white',font=('times new roman',15,'bold'))
total_cat_icon_label.pack()

total_cat_count_label=Label(cat_frame,text='0',bg='#27AE60',fg='white',font=('times new roman',30,'bold'))
total_cat_count_label.pack()

prod_frame=Frame(window,bg='#2980B9',bd=3,relief=RIDGE)
prod_frame.place(x=1000,y=310,height=170,width=280)
total_prod_icon=PhotoImage(file='total_prod.png')
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg='#2980B9')
total_prod_icon_label.pack()

total_prod_icon_label=Label(prod_frame,text='Total Products',bg='#2980B9',fg='white',font=('times new roman',15,'bold'))
total_prod_icon_label.pack()

total_prod_count_label=Label(prod_frame,text='0',bg='#2980B9',fg='white',font=('times new roman',30,'bold'))
total_prod_count_label.pack()

# sales_frame=Frame(window,bg='#E74C3C',bd=3,relief=RIDGE)
# sales_frame.place(x=750,y=500,height=170,width=280)
# total_sales_icon=PhotoImage(file='total_sales.png')
# total_sales_icon_label=Label(sales_frame,image=total_sales_icon,bg='#E74C3C')
# total_sales_icon_label.pack()
#
# total_sales_icon_label=Label(sales_frame,text='Total Sales',bg='#E74C3C',fg='white',font=('times new roman',15,'bold'))
# total_sales_icon_label.pack()
#
# total_sales_count_label=Label(sales_frame,text='0',bg='#E74C3C',fg='white',font=('times new roman',30,'bold'))
# total_sales_count_label.pack()
update()

window.mainloop()
