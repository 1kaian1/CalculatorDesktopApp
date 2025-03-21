import tkinter as tk
root = tk.Tk()

root.title("Kalkulacka")
root.geometry("600x800+100+200")
root.resizable(False,False)
root.configure(bg="#DDDDDD")

buttonWidth = 4
buttonHeight = 2
buttonColor = "#000000"
textColor = "#FFFFFF"
font = ("arial",30)

buttonX = (15, 165, 315, 465)
buttonY = (135, 255, 375, 495, 615)

label = tk.Label(root,width=23, height=2, font=("arial",30),bg="#7cc7a9").place(x=12,y=12)

tk.Button(root,text="!",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[0], y=buttonY[0])
tk.Button(root,text="x^n",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[1], y=buttonY[0])
tk.Button(root,text="n√x",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[2], y=buttonY[0])
tk.Button(root,text="%",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[3], y=buttonY[0])

tk.Button(root,text="7",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[0], y=buttonY[1])
tk.Button(root,text="8",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[1], y=buttonY[1])
tk.Button(root,text="9",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[2], y=buttonY[1])
tk.Button(root,text="/",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[3], y=buttonY[1])

tk.Button(root,text="4",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[0], y=buttonY[2])
tk.Button(root,text="5",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[1], y=buttonY[2])
tk.Button(root,text="6",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[2], y=buttonY[2])
tk.Button(root,text="*",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[3], y=buttonY[2])

tk.Button(root,text="1",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[0], y=buttonY[3])
tk.Button(root,text="2",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[1], y=buttonY[3])
tk.Button(root,text="3",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[2], y=buttonY[3])
tk.Button(root,text="-",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[3], y=buttonY[3])

tk.Button(root,text="0",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[0], y=buttonY[4])
tk.Button(root,text=".",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[1], y=buttonY[4])
tk.Button(root,text="=",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[2], y=buttonY[4])
tk.Button(root,text="+",width=buttonWidth,height=buttonHeight,fg=textColor,bg=buttonColor,font=font).place(x=buttonX[3], y=buttonY[4])

tk.Button(root,text="C",width=2,height=1,fg="red",bg="#FFFFFF",font=font).place(x=165, y=735)
tk.Button(root,text="CE",width=2,height=1,fg="#FF0000",bg="white",font=font).place(x=315, y=735)


global equation_text

def show(label, text):
    label.config(text = equation)

def buttonPress(num):
    equation_text = equation_text + str(num)
    show(label, equation_text)


    

def calculate():
    global equation
    result = ""
    
    if (equation != ""):
        try:
            result = eval(equation)
        except:
            result = ZeroDivisionError
            equation = ""
            
    label.config(text = equation)

root.mainloop()

