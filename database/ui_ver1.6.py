#coding=utf-8
from Tkinter import * 
import tkMessageBox
import QAsystem
import MySQLdb

db = MySQLdb.connect("localhost","root","mysql","wikitest")
cursor = db.cursor()

root = Tk()
root.title("wikidata project")
root.geometry('1200x300')                 


l1 = Label(root, text="query1：")
l1.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
q1_text = StringVar()
w1 = Entry(root, textvariable = q1_text)
q1_text.set(" ")
w1.pack()



l2 = Label(root, text="query2：")
l2.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
q2_text = StringVar()
w2 = Entry(root, textvariable = q2_text)
q2_text.set(" ")
w2.pack()


l3 = Label(root, text="query3:")
l3.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
q3_text = StringVar()
w3 = Entry(root, textvariable = q3_text)
q3_text.set(" ")
w3.pack()




l4 = Label(root, text="query4：")
l4.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
q4_text = StringVar()
w4 = Entry(root, textvariable = q4_text)
q4_text.set(" ")
w4.pack()

l5 = Label(root,text="what's the PROPERTY of NAME")
l5.pack()
q5_text = StringVar()
w5 = Entry(root, textvariable = q5_text)
q5_text.set("property")
w5.pack()

q55_text = StringVar()
w55 = Entry(root, textvariable = q55_text)
q55_text.set("name")
w55.pack()

l6 = Label(root,text = "query6: ")
l6.pack()
q6_text = StringVar()
w6 = Entry(root, textvariable = q6_text)
q6_text.set(" ")
w6.pack()



def on_click_1():
	q1 = q1_text.get().strip(' ')
	string = QAsystem.name_to_entity(db,cursor,q1)
	print("q1：%s" %(q1))
	#tkMessageBox.showinfo(title='result', message = string)
	root_1 = Tk()
	root_1.title("result")
	root_1.geometry("500x500")
	text = Text(root_1)

	text.insert(INSERT,string)
	text.pack()
	root_1.mainloop()

def on_click_2():
	q2 = q2_text.get().strip(' ')
	string = QAsystem.entity_precatry_subs(db,cursor,q2)
	#tkMessageBox.showinfo(title='result', message = string)
	root_2 = Tk()
	root_2.title("result")
	root_2.geometry("500x500")
	text = Text(root_2)
	text.insert(INSERT,string)
	text.pack()
	root_2.mainloop()

def on_click_3():
	q3 = q3_text.get().strip(' ')
	string = QAsystem.entity_stmt_entity(db,cursor,q3)
	#tkMessageBox.showinfo(title='result', message = string)
	root_3 = Tk()
	root_3.title("result")
	root_3.geometry("500x500")
	text = Text(root_3)
	text.insert(INSERT,string)
	text.pack()
	root_3.mainloop()

def on_click_4():
	q4 = q4_text.get().strip(' ')
	string = QAsystem.entity_to_statements(db,cursor,q4)
	#tkMessageBox.showinfo(title='result', message = string)
	root_4 = Tk()
	root_4.title("result")
	root_4.geometry("500x500")
	text = Text(root_4)
	text.insert(INSERT,string)
	text.pack()
	root_4.mainloop()

def on_click_5():
	en = q55_text.get().strip(' ')
	pro = q5_text.get().strip(' ')
	string = QAsystem.what_is_A_of_B(db,cursor,pro,en)
	#print("q5：%s" %(q5))
	#tkMessageBox.showinfo(title='result', message = string)
	root_5 = Tk()
	root_5.title("result")
	root_5.geometry("500x500")
	text = Text(root_5)
	text.insert(INSERT,string)
	text.pack()
	root_5.mainloop()

def on_click_6():
	q6 = q6_text.get().strip(' ')
	string = QAsystem.property_max_entity(db,cursor,q6)
	root_6 = Tk()
	root_6.title("result")
	root_6.geometry("500x500")
	text = Text(root_6)
	text.insert(INSERT,string)
	text.pack()
	root_6.mainloop()

b1 = Button(root, text="show result1", command = on_click_1)
b2 = Button(root, text="show result2", command = on_click_2)
b3 = Button(root, text="show result3", command = on_click_3)
b4 = Button(root, text="show result4", command = on_click_4)
b5 = Button(root, text="show result5", command = on_click_5)
b6 = Button(root, text="show result6", command = on_click_6)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()

d1 = Label(root,text="Given a name,return all the entities that match the name.")
d1.pack()

d2 = Label(root,text="Given an entity,return all preceding categories (instance of and subclass of) it belongs to.")
d2.pack()

d3 = Label(root,text="Given an entity,return all entities that are co-occurred with this entity in one statement.")
d3.pack()

d4 = Label(root,text="Given an entity,return all the properties and statements it possesses.")
d4.pack()

#d5 = Label(root,text="basic Q&A (questioning and answering) system")
#d5.pack()
d6 = Label(root,text="Giving an property, return the entity which has the maximum value on this property.")
d6.pack()

l1.grid(row = 1, column = 0)
l2.grid(row = 3, column = 0)
l3.grid(row = 5, column = 0)
l4.grid(row = 7, column = 0)
l5.grid(row = 9, column = 0)
l6.grid(row = 11, column = 0)

w1.grid(row = 1, column = 2)
w2.grid(row = 3, column = 2)
w3.grid(row = 5, column = 2)
w4.grid(row = 7, column = 2)
w5.grid(row = 9, column = 2)
w6.grid(row = 11, column = 2)

b1.grid(row = 1, column = 3)
b2.grid(row = 3, column = 3)
b3.grid(row = 5, column = 3)
b4.grid(row = 7, column = 3)
b5.grid(row = 9, column = 3)
b6.grid(row = 11, column = 3)

d1.grid(row = 1, column = 1)
d2.grid(row = 3, column = 1)
d3.grid(row = 5, column = 1)
d4.grid(row = 7, column = 1)
w55.grid(row = 9, column = 1)
d6.grid(row = 11, column = 1)

root.mainloop()



