import tkinter as tk


root = tk.Tk()
root.title("Automatic Traffic Lights")


canvas = tk.Canvas(root, width=200, height=600, bg='black')
canvas.pack()


canvas.create_rectangle(50, 50, 150, 550, fill='gray')

red_light = canvas.create_oval(50, 50, 150, 200, fill='gray')
yellow_light = canvas.create_oval(50, 225, 150, 375, fill='gray')
green_light = canvas.create_oval(50, 400, 150, 550, fill='gray')


def change_light():
    current_color = canvas.itemcget(red_light, 'fill')
    if current_color == 'red':
        canvas.itemconfig(red_light, fill='gray')
        canvas.itemconfig(yellow_light, fill='yellow')
        root.after(3000, change_light)  
    elif current_color == 'yellow':
        canvas.itemconfig(yellow_light, fill='gray')
        canvas.itemconfig(green_light, fill='green')
        root.after(3000, change_light)  
    else:
        canvas.itemconfig(green_light, fill='gray')
        canvas.itemconfig(red_light, fill='red')
        root.after(3000, change_light) 

canvas.itemconfig(red_light, fill='red')
root.after(3000, change_light) 

root.mainloop()
