# from tkinter import *
# import tempChecker as tpp
# 
# def tryTempGUIs():
# 
#     theme='#4d97fe'
# 
#     def tryTempGUIOne():
#         window.destroy()
#         
#     window = Tk()
#     window.title("IOT")
#     window.geometry('800x480')
#     lbl=Label(window,text="Please Scan your Temperature", fg='black')
#     lst=('Calibri (Body)', 15, 'bold')
#     lbl.config(font=lst)
#     lbl.place(x=320,y=160)
#     if(tpp.tempTsek()[0]):
#         lbl2=Label(window,text="Your Temp is "+ str(tpp.tempTsek()[1]), fg='black')
#         lbl2.config(font=lst) 
#         lbl2.place(x=320,y=200)
#     buttn = Button(window, width=10, height=1, text="PROCEED", fg=theme, border=0, command=tryTempGUIOne, bg='white')
#     buttn.place(x=345,y=230)
#         
#     window.mainloop()
# 