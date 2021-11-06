from tkinter import *
from tkinter.font import BOLD

window = Tk()
window.title("Simple Interest Calculator")
window.geometry("400x450")
window.configure(bg="lightgreen")

def calculate_si():
    p = float(principle_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    result_label.destroy()
    message = Label(result_frame, text="Interest on rs. "+str(p)+" at rate of interest "+str(r)+" for "+str(t)+" is Rs. "+str(interest), bg="lightgreen", font=("Calibri", 12), wraplength=300)
    message.place(x=20, y=40)
    message.pack()

app_label = Label(window, text="Simple Interest Calculator", fg="black", bg="lightgreen", font=("Comic Sans MS", 20, BOLD))
app_label.place(x=25, y=10)

principle_label = Label(window, text="Enter principal:", fg="black", bg="lightgreen", font=("Comic Sans MS", 12))
principle_label.place(x=20, y=90)
principle_entry = Entry(window, text="", bd=2, width=25)
principle_entry.place(x=200, y=95)

rate_label = Label(window, text="Enter rate(in rs.):", fg="black", bg="lightgreen", font=("Comic Sans MS", 12))
rate_label.place(x=20, y=130)
rate_entry = Entry(window, text="", bd=2, width=25)
rate_entry.place(x=200, y=135)

time_label = Label(window, text="Enter time(in years):", fg="black", bg="lightgreen", font=("Comic Sans MS", 12))
time_label.place(x=20, y=170)
time_entry = Entry(window, text="", bd=2, width=25)
time_entry.place(x=200, y=175)

calculate_button = Button(window, text="Calculate", fg="black", bg="green", bd=4, command=calculate_si)
calculate_button.place(x=160, y=225)

result_frame = LabelFrame(window, text="Result", bg="lightgreen", font=("Comic Sans MS", 12), width=400)
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

result_label = Label(result_frame, text=" ", bg="lightgreen", font=("Calibri",12), width=40)
result_label.place(x=20, y=20)
result_label.pack()

window.mainloop()
