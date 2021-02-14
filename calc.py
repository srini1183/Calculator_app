from tkinter import *


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.option_add('*Font', 'arial 20 ')
        self.e = None
        self.root.iconbitmap('calculator.ico')
        
    def button_click(self,button):
        if button == "C":
            self.e.delete(0,END)
        elif button == "=":
            try:
                text = self.e.get()
                self.e.delete(0,END)
                self.e.insert(0,eval(text))
            except:
                self.e.delete(0,END)
                self.e.insert(0,"ERROR!!")    
        else:
            prev = self.e.get()
            self.e.delete(0,END)
            self.e.insert(0,prev+button)

    def add_button(self,num,row,col):
        Button(self.root,text = num,activebackground = "#cdcdcd",relief = FLAT,padx = 50,pady = 20,command = lambda : self.button_click(num)).grid(row = row,column = col,sticky = "NSEW")
    
    def add_buttons(self):
        self.e = Entry(self.root,width = 60,borderwidth = 5)
        self.e.grid(row = 0,column = 0,columnspan = 3)

        nums_list = ["789","456","123","0+-","*/="]
        for i,nums in enumerate(nums_list):
            for j,num in enumerate(nums):
                self.add_button(num,i+1,j)                    

        Button(self.root,text = ".",activebackground = "#cdcdcd",relief = FLAT,padx = 50,pady = 20,command = lambda : self.button_click(".")).grid(row = 7,column = 0)
        Button(self.root,text = "Clear",activebackground = "#cdcdcd",relief = FLAT,padx = 160,pady = 20,command = lambda : self.button_click("C")).grid(row = 7,column = 1,columnspan = 2)




obj = Calculator()
obj.root.title('Calculator')
obj.add_buttons()
obj.root.mainloop()