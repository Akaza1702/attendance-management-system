class DeleteRecord(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label1=tk.Label(self,text="Delete Record",font=("Times",24))
		label2=tk.Label(self,text="This action will delete the record,continue?",font=("Times",12))
		bt2=tk.Button(self,text="YES",bg="green",font=("Times",16),height=2,width=17,command=lambda:self.delrecord(controller))
		
		bt3=tk.Button(self,text="Back to home",bg="red",font=("Times",16),height=2,width=17,command=lambda:controller.show_frame(StartPage))
		label1.pack()
		label2.pack()
		bt2.pack()
		bt1.pack()
		bt3.pack()
	def delrecord(self,controller):
		conn=sql.connect('attend') 
		cur=conn.cursor()
		cur.execute('DROP TABLE IF EXISTS attable')	
		conn.commit()
		conn.close()
		messagebox.showinfo("Alert!", "records deleted")
		controller.show_frame(StartPage)	
