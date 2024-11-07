from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False, False)

def Reset():
    entry_dosa.delete(0, END)
    entry_cookies.delete(0, END)
    entry_tea.delete(0, END)
    entry_coffee.delete(0, END)
    entry_juice.delete(0, END)
    entry_pancakes.delete(0, END)
    entry_eggs.delete(0, END)

def Total():
    try:a1=int(dosa.get())
    except:a1=0

    try:a2=int(cookies.get())
    except:a2=0

    try:a3=int(tea.get())
    except:a3=0

    try:a4=int(coffee.get())
    except:a4=0

    try:a5=int(juice.get())
    except:a5=0

    try:a6=int(pancakes.get())
    except:a6=0

    try:a7=int(eggs.get())
    except:a7=0

    # define cost of each item per quantity
    c1 = 60*a1
    c2 = 30*a2
    c3 = 7*a3
    c4 = 100*a4
    c5 = 20*a5
    c6 = 15*a6
    c7 = 7*a7

    lbl_total = Label(f3, font=("aria", 20, "bold"), text="Total", width=18, fg="lightyellow", bg="black")
    lbl_total.place(x=0, y=84)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs." + str(totalcost)
    Total_bill.set(string_bill)

    entry_total=Entry(f3, font=("aria", 20, "bold"), textvariable=Total_bill, bd=6, width=12, bg="lightgreen")
    entry_total.place(x=60, y=140)

Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri",33), width=50, height=2).pack()

# MENU CARD
f1=Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f1.place(x=10, y=122)

Label(f1, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=80, y=0)

Label(f1, text="Dosa......Rs.60/plate", font=("Lucida Calligraphy", 15, "bold"), fg="black", bg="lightgreen").place(x=10, y=90)
Label(f1, text="Cookies...Rs.30/plate", font=("Lucida Calligraphy", 15, "bold"), fg="black", bg="lightgreen").place(x=10, y=120)
Label(f1, text="Tea.......Rs.7/cup", font=("Lucida Calligraphy", 15, "bold"), fg="black", bg="lightgreen").place(x=10, y=150)
Label(f1, text="Coffee....Rs.100/cup", font=("Lucida Calligraphy", 15, "bold"), fg="black", bg="lightgreen").place(x=10, y=180)
Label(f1, text="Juice.....Rs.20/glass", font=("Lucida Calligraphy", 15, "bold"), fg="black", bg="lightgreen").place(x=10, y=210)
Label(f1, text="Pancakes....Rs.15/pack", font=("Lucida Calligraphy", 15, "bold"), fg="black", bg="lightgreen").place(x=10, y=240)
Label(f1, text="Eggs......Rs.7/egg", font=("Lucida Calligraphy", 15, "bold"), fg="black", bg="lightgreen").place(x=10, y=270)

# BILL
f3=Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, height=370, width=300)
f3.place(x=690, y=122)

Bill=Label(f3, text="Bill", font=("calibri", 30), bg="lightyellow")
Bill.place(x=120, y=20)

# ENTRY WORK
f2=Frame(root, height=380, width=300, bd=5, relief=RAISED)
f2.pack()

dosa = StringVar()
cookies=StringVar()
tea=StringVar()
coffee=StringVar()
juice=StringVar()
pancakes=StringVar()
eggs=StringVar()
Total_bill=StringVar()

# Label
lbl_dosa=Label(f2, font=("aria", 20, "bold"), text="Dosa", width=10, fg="blue4")
lbl_cookies=Label(f2, font=("aria", 20, "bold"), text="Cookies", width=10, fg="blue4")
lbl_tea=Label(f2, font=("aria", 20, "bold"), text="Tea", width=10, fg="blue4")
lbl_coffee=Label(f2, font=("aria", 20, "bold"), text="Coffee", width=10, fg="blue4")
lbl_juice=Label(f2, font=("aria", 20, "bold"), text="Juice", width=10, fg="blue4")
lbl_pancakes=Label(f2, font=("aria", 20, "bold"), text="Pancakes", width=10, fg="blue4")
lbl_eggs=Label(f2, font=("aria", 20, "bold"), text="Eggs", width=10, fg="blue4")
lbl_dosa.grid(row=1, column=0)
lbl_cookies.grid(row=2, column=0)
lbl_tea.grid(row=3, column=0)
lbl_coffee.grid(row=4, column=0)
lbl_juice.grid(row=5, column=0)
lbl_pancakes.grid(row=6, column=0)
lbl_eggs.grid(row=7, column=0)

# Entry
entry_dosa=Entry(f2, font=("aria", 20, "bold"), textvariable=dosa, bd=6, width=10, bg="lightpink")
entry_cookies=Entry(f2, font=("aria", 20, "bold"), textvariable=cookies, bd=6, width=10, bg="lightpink")
entry_tea=Entry(f2, font=("aria", 20, "bold"), textvariable=tea, bd=6, width=10, bg="lightpink")
entry_coffee=Entry(f2, font=("aria", 20, "bold"), textvariable=coffee, bd=6, width=10, bg="lightpink")
entry_juice=Entry(f2, font=("aria", 20, "bold"), textvariable=juice, bd=6, width=10, bg="lightpink")
entry_pancakes=Entry(f2, font=("aria", 20, "bold"), textvariable=pancakes, bd=6, width=10, bg="lightpink")
entry_eggs=Entry(f2, font=("aria", 20, "bold"), textvariable=eggs, bd=6, width=10, bg="lightpink")
entry_dosa.grid(row=1, column=1)
entry_cookies.grid(row=2, column=1)
entry_tea.grid(row=3, column=1)
entry_coffee.grid(row=4, column=1)
entry_juice.grid(row=5, column=1)
entry_pancakes.grid(row=6, column=1)
entry_eggs.grid(row=7, column=1)

# buttons

btn_reset=Button(f2, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=12, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_total=Button(f2, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=12, text="Total", command=Total)
btn_total.grid(row=8, column=1)

root.mainloop()