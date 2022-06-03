import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL, ttk
import idleWindow as iw

def main():
    

    root = tk.Tk()

    root.config(cursor="none")
    # Theme
    theme='#4d97fe'


    # Main window settings
    width_of_window = 700
    height_of_window = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

    root.overrideredirect(1)

    # Main window's Frame Settings
    frame = tk.Frame(root,width=800,height=480,bg=theme).place(x=0,y=0)


    # Label
    l1=tk.Label(root,text='Integrated',fg='white',bg=theme)
    lst1=('Calibri (Body)',28,'bold')
    l1.config(font=lst1)
    l1.place(x=120,y=160)

    l2=tk.Label(root,text='RasPi Security',fg='white',bg=theme)
    lst2=('Calibri (Body)',28)
    l2.config(font=lst2)
    l2.place(x=350,y=160)

    l3=tk.Label(root,text='DREAMTEAM01',fg='white',bg=theme)
    lst3=('Calibri (Body)',17)
    l3.config(font=lst3)
    l3.place(x=120,y=215)


    # Progress Bar Style
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
    progress=Progressbar(root,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=1000,mode='determinate',)


    # Progress Bar Function
    def bar():

        l4=tk.Label(root,text='Loading...',fg='white',bg=theme)
        lst4=('Calibri (Body)',15)
        l4.config(font=lst4)
        l4.place(x=28,y=440)
        
        import time
        for r in range(100):
            progress['value']=r
            root.update_idletasks()
            time.sleep(0.03)
            r=r+1
        
        root.destroy()
        iw.loopingWindow()
        
        
    progress.place(x=-10,y=465)


    # Buttons
    button1 = tk.Button(frame, width=7, height=2, text="QUIT", fg="red", border=0, command=quit, bg='white',  activebackground='white', activeforeground='red')
    button1.place(x=200,y=309)
    lg=('Calibri (Body)',16)
    button1.config(font=lg)
    slogan = tk.Button(frame, width=7, height=2, text="START", fg=theme, border=0, command=bar, bg='white', activebackground='white', activeforeground=theme)
    slogan.place(x=360,y=309)
    slogan.config(font=lg)
    
    
    root.mainloop()
    
    
if __name__ == "__main__":
    main()