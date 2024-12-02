import tkinter as tk
import random
import pyautogui

def move_cursors(event):
    for i, cursor in enumerate(cursors):
        x_offset, y_offset = initial_positions[i]
        x = event.x + x_offset
        y = event.y + y_offset
        canvas.coords(cursor, x, y)

screen_width, screen_height = 1920, 1080
random_x = random.randint(0, screen_width)
random_y = random.randint(0, screen_height)
pyautogui.moveTo(random_x, random_y)

root = tk.Tk()
root.attributes('-fullscreen', True)  
root.attributes('-topmost', True)  
root.configure(bg="black") 
root.title("100 Cursors Overlay")
root.bind("<Escape>", lambda e: root.destroy())

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

cursor_image = tk.PhotoImage(file="cursor.png")

initial_positions = [(random.randint(-screen_width, screen_width),
                      random.randint(-screen_height, screen_height))
                     for _ in range(100)]

cursors = []
for x_offset, y_offset in initial_positions:
    cursor = canvas.create_image(x_offset, y_offset, image=cursor_image)
    cursors.append(cursor)

canvas.bind("<Motion>", move_cursors)

root.mainloop()
