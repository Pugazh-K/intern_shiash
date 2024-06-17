import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Automatic Traffic Lights")

# Create a canvas to draw the traffic lights
canvas = tk.Canvas(root, width=200, height=600, bg='black')
canvas.pack()

# Draw the traffic light structure
canvas.create_rectangle(50, 50, 150, 550, fill='gray')

# Create circles for the red, yellow, and green lights
red_light = canvas.create_oval(50, 50, 150, 200, fill='gray')
yellow_light = canvas.create_oval(50, 225, 150, 375, fill='gray')
green_light = canvas.create_oval(50, 400, 150, 550, fill='gray')

# Function to change the traffic light colors
def change_light():
    current_color = canvas.itemcget(red_light, 'fill')
    if current_color == 'red':
        canvas.itemconfig(red_light, fill='gray')
        canvas.itemconfig(yellow_light, fill='yellow')
        root.after(3000, change_light)  # Change to yellow after 3 seconds
    elif current_color == 'yellow':
        canvas.itemconfig(yellow_light, fill='gray')
        canvas.itemconfig(green_light, fill='green')
        root.after(3000, change_light)  # Change to green after 3 seconds
    else:
        canvas.itemconfig(green_light, fill='gray')
        canvas.itemconfig(red_light, fill='red')
        root.after(3000, change_light)  # Change to red after 3 seconds

# Start with the red light on
canvas.itemconfig(red_light, fill='red')
root.after(3000, change_light)  # Start the light change cycle after 3 seconds

# Run the Tkinter event loop
root.mainloop()
