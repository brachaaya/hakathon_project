import tkinter as tk

# from pygame.examples.scrap_clipboard import screen
#
# def on_english_click():
#     print("english")
# def on_hebrew_click():
#     print("hebrew")

root= tk.Tk()
root.geometry('750x730')
root.resizable(width=False, height=False)

color1='#020f12'
color2='#05d7ff'
color3='#65e7ff'
color4= 'BLACK'

screen_frame= tk.Frame(root, bg=color1, pady=40)
screen_frame.pack(fill=tk.BOTH, expand=True)
screen_frame.columnconfigure(0, weight=1)
screen_frame.rowconfigure(0, weight=1)
screen_frame.rowconfigure(1, weight=1)

english_button= tk.Button(
    screen_frame,
    background=color2,
    foreground=color4,
    activebackground=color3,
    activeforeground=color4,
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    width=13,
    height=2,
    border=0,
    text='English',
    font=('Arial', 16, 'bold'),
    command= on_english_click()
)

english_button.grid(column=0, row=0)

hebrew_button= tk.Button(
    screen_frame,
    background=color2,
    foreground=color4,
    activebackground=color3,
    activeforeground=color4,
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    width=13,
    height=2,
    border=0,
    text='Hebrew',
    font=('Arial', 16, 'bold'),
    command= on_hebrew_click()
)
hebrew_button.grid(column=0, row=1)

root.mainloop()