from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle
import random
import mysql.connector

# Database Connection


def make_conn():
    global mydb
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root@123",
                                   database="my_projects")
    global cursor
    cursor = mydb.cursor()

# Insert data in Database


def insert_db(ven, t1, t2, hr, d, xg1, xga1, gf1, mode, pred):
    make_conn()
    query = "INSERT INTO FOOTBALL_PRED_RES(VENUE,TEAM,OPPONENT,TIME,DAY,XG,XGA,GF,_Mode,Pred_Result) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

    ven = ("Home" if ven == 1 else "Away")

    pred = ("Win" if pred[0] == 1 else "Lose")

    t1 = get_key(t1, team_menu)
    t2 = get_key(t2, team_menu)
    d = get_key(d, day_menu)
    val = (ven, t1, t2, hr, d, xg1, xga1, gf1, mode, pred)

    cursor.execute(query, val)
    mydb.commit()
    print(cursor.rowcount, "Record Inserted")
    cursor.close()

# Prediction


def predictors(ven, t1, t2, hr, d, xg1, xga1, gf1, mode):
    load = pickle.load(
        open(
            "E:\\Development\\Python\\ML\\Sport Match Prediction\\Desktop App\\Final.pkl",
            "rb",
        ))
    pred = load.predict([[ven, t1, t2, hr, d, xg1, xga1, gf1]])

    insert_db(ven, t1, t2, hr, d, xg1, xga1, gf1, mode, pred)

    if pred[0] == 1:
        messagebox.showinfo("Result", "Your Team Wins")
    elif pred[0] == 0:
        messagebox.showinfo("Result", "Your Team Lose/Draw")


# Get Key from Values
def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key


# Label for Auto Fill Warning
def auto_fill_label(X, Y):
    Label(
        pred_layout,
        text="*auto_fill",
        font=("Calibri", 12, "italic"),
        bg="White",
        fg="Green",
    ).place(x=X, y=Y)


# Team1 Search
def search1(event):
    value_to_search = event.widget.get()
    # Team 1
    if value_to_search == "" or value_to_search == " " and team1.get():
        team1["values"] = menu
    else:
        res = []
        for value in menu:
            if value_to_search in value:
                res.append(value)
        team1["values"] = res


# Team2 Search
def search2(event):
    value_to_search = event.widget.get()
    # Team 2
    if value_to_search == "" or value_to_search == " " and team2.get():
        team2["values"] = menu

    else:
        res = []
        for value in menu:
            if value_to_search in value:
                res.append(value)
        team2["values"] = res


# Day Search
def search3(event):
    value_to_search = event.widget.get()
    # Day
    if value_to_search == "" or value_to_search == " " and day.get():
        day["values"] = day_keys
    else:
        res = []
        for value in day_keys:
            if value_to_search in value:
                res.append(value)
        day["values"] = res


# Auto Fill
def auto_fill(event):
    global t1, xg1, xga1, gf1
    t1 = team_menu.get(team1.get())
    # [team,xg,xga,gf]
    val = [
        [0, 14.17, 5.9, 17],
        [1, 6.18, 10.15, 6],
        [2, 11.10, 9.8, 15],
        [3, 11.26, 5.66, 11],
        [5, 8.42, 9.16, 8],
        [6, 7.55, 11.39, 7],
        [7, 7.97, 10.88, 5],
        [8, 8.98, 13.23, 12],
        [9, 9.09, 8.73, 10],
        [10, 6.62, 12.75, 10],
        [11, 14.11, 7.15, 15],
        [12, 17.52, 3.99, 23],
        [13, 8.81, 8.04, 8],
        [14, 11.29, 10.31, 8],
        [17, 7.26, 9.15, 11],
        [18, 12.5, 7.21, 18],
        [21, 7.03, 8.52, 3],
        [22, 6.84, 8.37, 3],
    ]
    for i in range(23):
        if val[i][0] == t1 and (t1 != 4 or t1 != 15 or t1 != 16 or t1 != 19
                                or t1 != 20):
            xg1, xga1, gf1 = val[i][1], val[i][2], val[i][3]
            xg.delete(0, END)
            xg.insert(0, xg1)
            auto_fill_label(220, 270)
            xga.delete(0, END)
            xga.insert(0, xga1)
            auto_fill_label(220, 310)
            gf.delete(0, END)
            gf.insert(0, gf1)
            auto_fill_label(220, 350)
            break


# Auto Prediction Function
def pred_fn_auto():
    t1 = random.randint(0, 22)
    t2 = random.randint(0, 22)
    if ((t1 != t2)
            and (t1 != 4 and t1 != 15 and t1 != 16 and t1 != 19 and t1 != 20)
            and (t2 != 4 and t2 != 15 and t2 != 16 and t2 != 19 and t2 != 20)):
        team1.set(get_key(t1, team_menu))
        team2.set(get_key(t2, team_menu))
        ven = random.choice([0, 1])
        venue.set(ven)

        hr = random.randint(0, 23)
        hour.delete(0, END)
        hour.insert(0, hr)

        d = random.randint(0, 6)
        day.set(get_key(d, day_menu))

        xg1 = round(random.uniform(0.00, 4.60), 2)
        xg.delete(0, END)
        xg.insert(0, xg1)

        xga1 = round(random.uniform(0.00, 5.00), 2)
        xga.delete(0, END)
        xga.insert(0, xga1)

        gf1 = round(random.uniform(0.00, 9.00), 2)
        gf.delete(0, END)
        gf.insert(0, gf1)
        predictors(ven, t1, t2, hr, d, xg1, xga1, gf1, "Auto")

    else:
        pred_fn_auto()  # Recursion


# Prediction Function
def pred_fn():

    try:
        t2 = team_menu.get(team2.get())
        ven = venue.get()
        hr = int(hour.get())
        d = day_menu.get(day.get())
        if hr <= 0 or hr >= 24 or xg1 < 0.0 or xga1 < 0.0 or gf1 < 0.0:
            messagebox.askretrycancel("Invalid Values", "Try again?")

        elif t1 == t2:
            messagebox.askretrycancel("Same Teams", "Try again?")
        else:
            predictors(ven, t1, t2, hr, d, xg1, xga1, gf1, "Manual")
    except:
        messagebox.showwarning("Warning", "Fields can't be NULL")


# Layout
pred_layout = Tk()

# Window Position
window_width = 360
window_height = 440
screen_width = pred_layout.winfo_screenwidth()
screen_height = pred_layout.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
pred_layout.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Configure
pred_layout.configure(bg="White")
pred_layout.title("Football Match Prediction")
pred_layout.resizable(False, False)
# Icon
pred_layout.iconbitmap(
    r"E:\Development\Python\ML\Sport Match Prediction\Desktop App\premier-league-logo-vector.ico"
)

# Heading
Label(
    pred_layout,
    text="Football Match Prediction",
    font=("Bell MT", 17, "bold", "underline"),
    bg="White",
).pack()
Label(
    pred_layout,
    text="~ Team No. 407",
    font=("Bell MT", 8, "bold", "underline"),
    bg="White",
).place(x=240, y=35)

# Team 1
team_menu = {
    "Manchester City": 12,
    "Chelsea": 5,
    "Arsenal": 0,
    "Tottenham Hotspur": 18,
    "Manchester United": 13,
    "West Ham United": 21,
    "Wolverhampton Wanderers": 22,
    "Newcastle United": 14,
    "Leicester City": 10,
    "Brighton and Hove Albion": 3,
    "Brentford": 2,
    "Southampton": 17,
    "Crystal Palace": 6,
    "Aston Villa": 1,
    "Leeds United": 9,
    "Everton": 7,
    "Liverpool": 11,
    "Fulham": 8,
}
Label(pred_layout, text="Your Team :", font=("Bell MT", 15),
      bg="White").place(x=35, y=70)
menu = sorted(team_menu.keys(), reverse=False)
team1 = ttk.Combobox(pred_layout, values=menu, width=21)
team1.configure(font=("Times New Roman", 12))
team1.place(x=155, y=70)
team1.set("Team 1")
team1.bind("<<ComboboxSelected>>", auto_fill)
team1.bind("<KeyRelease>", search1)
# Team 2
Label(pred_layout, text="Opponent :", font=("Bell MT", 15),
      bg="White").place(x=35, y=110)
team2 = ttk.Combobox(pred_layout, values=menu, width=21)
team2.configure(font=("Times New Roman", 12))
team2.place(x=155, y=110)
team2.set("Team 2")
team2.bind("<KeyRelease>", search2)

# Venue
Label(pred_layout, text="Venue :", font=("Bell MT", 15),
      bg="White").place(x=35, y=150)
venue = IntVar()

r0 = Radiobutton(
    pred_layout,
    text="Away",
    font=("Times New Roman", 12),
    bg="White",
    variable=venue,
    value=0
)
r0.place(x=155, y=150)

r1 = Radiobutton(
    pred_layout,
    text="Home",
    font=("Times New Roman", 12),
    bg="White",
    variable=venue,
    value=1
)
r1.place(x=240, y=150)
venue.set(None)

# Hour
Label(pred_layout, text="Hour  :", font=("Bell MT", 15),
      bg="White").place(x=35, y=190)
hour = Entry(pred_layout, width=4, font=("Times New Roman", 15))
hour.place(x=155, y=190)

# Day
day_menu = {
    "Monday": 4,
    "Tuesday": 5,
    "Wednesday": 6,
    "Thursday": 0,
    "Friday": 1,
    "Saturday": 2,
    "Sunday": 3,
}
Label(pred_layout, text="Day :", font=("Bell MT", 15), bg="White").place(x=35,
                                                                         y=230)
day_keys = list(day_menu.keys())
day = ttk.Combobox(pred_layout, values=day_keys, width=11)
day.configure(font=("Times New Roman", 11))
day.place(x=155, y=230)
day.set("Day")
day.bind("<KeyRelease>", search3)

# xg
Label(pred_layout, text="XG :", font=("Bell MT", 15), bg="White").place(x=35,
                                                                        y=270)
xg = Entry(pred_layout, width=6, font=("Times New Roman", 15))
xg.place(x=155, y=270)

# xga
Label(pred_layout, text="XG Against :", font=("Bell MT", 15),
      bg="White").place(x=35, y=310)
xga = Entry(pred_layout, width=6, font=("Times New Roman", 15))
xga.place(x=155, y=310)

# gf
Label(pred_layout, text="Goal for :", font=("Bell MT", 15),
      bg="White").place(x=35, y=350)
gf = Entry(pred_layout, width=6, font=("Times New Roman", 15))
gf.place(x=155, y=350)

# Output Button (Manual)
predict = Button(
    pred_layout,
    text="Predict",
    font=(15),
    width=16,
    bg="Gray",
    fg="White",
    command=pred_fn,
)
predict.place(x=-1, y=400)

# Output Button (Automated)
predict_auto = Button(
    pred_layout,
    text="Auto Predict",
    font=(15),
    width=16,
    bg="Gray",
    fg="White",
    command=pred_fn_auto,
)
predict_auto.place(x=180, y=400)

pred_layout.mainloop()
