from tkinter import *
from tkinter import messagebox
import pickle
import random

# Predictors


def predictors(t1, t2, ven, hr, d, xg1, xga1, gf1):
    load = pickle.load(
        open('E:\\Development\\Python\\ML\\Sport Match Prediction\\Desktop App\\Final.pkl', 'rb'))
    pred = load.predict([[t1, t2, ven, hr, d, xg1, xga1, gf1]])

    if pred[0] == 1:
        output_win.set("Win")
    else:
        output_lose.set("Lose/Draw")

# Get Key from Values


def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key


# Auto Prediction Function
def pred_fn_auto():
    t1 = random.randint(0, 22)
    t2 = random.randint(0, 22)
    if t1 != t2:
        team1.set(get_key(t1, team_menu))
        team2.set(get_key(t2, team_menu))

        ven = random.randint(0, 1)
        venue.set(ven+1)

        hr = random.randint(0, 23)
        hour.delete(0, END)
        hour.insert(0, hr)

        d = random.randint(0, 6)
        day.set(get_key(d, day_menu))

        xg1 = round(random.uniform(0.0, 4.6), 1)
        xg.delete(0, END)
        xg.insert(0, xg1)

        xga1 = round(random.uniform(0.0, 5.0), 1)
        xga.delete(0, END)
        xga.insert(0, xga1)

        gf1 = round(random.uniform(0.0, 9.0), 1)
        gf.delete(0, END)
        gf.insert(0, gf1)
        predictors(t1, t2, ven, hr, d, xg1, xga1, gf1)

    else:
        pred_fn_auto()  # Recursion


# Prediction Function
def pred_fn():
    try:
        t1 = team_menu.get(team1.get())
        t2 = team_menu.get(team2.get())
        d = day_menu.get(day.get())
        ven = venue.get()
        hr = int(hour.get())
        xg1 = float(xg.get())
        xga1 = float(xga.get())
        gf1 = float(gf.get())

        if hr < 0 or hr >= 24 or xg1 < 0.0 or xga1 < 0.0 or gf1 < 0.0:
            messagebox.showerror("Error", "Invalid values")

        elif t1 == t2:
            messagebox.showwarning("Warning", "Teams cannot be same")

        else:
            predictors(t1, t2, ven, hr, d, xg1, xga1, gf1)
    except:
        messagebox.showwarning("Warning", "Fields can't be NULL")


# Layout
pred_layout = Tk()

# Window Position
window_width = 360
window_height = 480
screen_width = pred_layout.winfo_screenwidth()
screen_height = pred_layout.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
pred_layout.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Configure
pred_layout.configure(bg="White")
pred_layout.title("Football Match Prediction")
pred_layout.resizable(False, False)
# Icon
pred_layout.iconbitmap(
    r'E:\Development\Python\ML\Sport Match Prediction\Desktop App\premier-league-logo-vector.ico')

# Logo
# img = Canvas(pred_layout, height=25, width=25, bg="White")
# img.pack()
# pic = ImageTk.PhotoImage(Image.open(
#     r"E:\Development\Python\ML\Sport Match Prediction\premier-league-logo-vector.png"))
# img.create_image(0, 0, image=pic, anchor=NW)

# Heading
Label(pred_layout, text="Football Match Prediction", font=(
    "Bell MT", 17, "bold", "underline"), bg="White").pack()
Label(pred_layout, text="~ Team No. 407", font=(
    "Bell MT", 8, "bold", "underline"), bg="White").place(x=240, y=35)


# Team 1
team_menu = {'Manchester City': 12, 'Chelsea': 5, 'Arsenal': 0, 'Tottenham Hotspur': 18, 'Manchester United': 13, 'West Ham United': 21, 'Wolverhampton Wanderers': 22, 'Newcastle United': 14, 'Leicester City': 10, 'Brighton and Hove Albion': 3,
             'Brentford': 2, 'Southampton': 17, 'Crystal Palace': 6, 'Aston Villa': 1, 'Leeds United': 9, 'Burnley': 4, 'Everton': 7, 'Watford': 19, 'Norwich City': 15, 'Liverpool': 11, 'Fulham': 8, 'West Bromwich Albion': 20, 'Sheffield United': 16}
Label(pred_layout, text="Your Team :", font=(
    "Bell MT", 15), bg="White").place(x=35, y=70)


menu = sorted(team_menu.keys(), reverse=False)
team1 = StringVar()
team1.set("Choose Team")
menu1 = OptionMenu(pred_layout, team1, *menu)
menu1.configure(font=("Times New Roman", 11), bg="White",
                highlightthickness=0.2, highlightbackground='Black')
menu1.place(x=155, y=70)

# Team 2
Label(pred_layout, text="Opponent :", font=(
    "Bell MT", 15), bg="White").place(x=35, y=110)

team2 = StringVar()
team2.set("Choose Team")
menu2 = OptionMenu(pred_layout, team2, *menu)
menu2.configure(font=("Times New Roman", 11), bg="White",
                highlightthickness=0.2, highlightbackground='Black')
menu2.place(x=155, y=110)

# Venue
Label(pred_layout, text="Venue :", font=(
    "Bell MT", 15), bg="White").place(x=35, y=150)
venue = IntVar()
Radiobutton(pred_layout, text="Away", font=("Times New Roman", 15),
            bg="White", value=1, variable=venue).place(x=155, y=150)
Radiobutton(pred_layout, text="Home", font=("Times New Roman", 15),
            bg="White", value=2, variable=venue).place(x=240, y=150)

# Hour
Label(pred_layout, text="Hour  :", font=(
    "Bell MT", 15), bg="White").place(x=35, y=190)
hour = Entry(pred_layout, width=4, font=("Times New Roman", 15))
hour.place(x=155, y=190)

# Day
day_menu = {'Monday': 4, 'Tuesday': 5, 'Wednesday': 6,
            'Thursday': 0, 'Friday': 1, 'Saturday': 2, 'Sunday': 3}
Label(pred_layout, text="Day :", font=(
    "Bell MT", 15), bg="White").place(x=35, y=230)

day_keys = list(day_menu.keys())
day = StringVar()
day.set("Choose Day")
menu3 = OptionMenu(pred_layout, day, *day_keys)
menu3.configure(font=("Times New Roman", 11), bg="White",
                highlightthickness=0.2, highlightbackground='Black')
menu3.place(x=155, y=230)

# xg
Label(pred_layout, text="XG :", font=(
    "Bell MT", 15), bg="White").place(x=35, y=270)
xg = Entry(pred_layout, width=4, font=("Times New Roman", 15))
xg.place(x=155, y=270)

# xga
Label(pred_layout, text="XG Against :", font=(
    "Bell MT", 15), bg="White").place(x=35, y=310)
xga = Entry(pred_layout, width=4, font=("Times New Roman", 15))
xga.place(x=155, y=310)

# gf
Label(pred_layout, text="Goal for :", font=(
    "Bell MT", 15), bg="White").place(x=35, y=350)
gf = Entry(pred_layout, width=4, font=("Times New Roman", 15))
gf.place(x=155, y=350)

# Output
output_win = StringVar()
result = Label(pred_layout, text='', textvariable=output_win, font=(
    "Times New Roman", 20), bg="White")
result.config(highlightbackground='Black')
result.place(x=150, y=385)

output_lose = StringVar()
result = Label(pred_layout, text='', textvariable=output_lose, font=(
    "Times New Roman", 20), bg="White")
result.config(highlightbackground='Black')
result.place(x=110, y=385)

# Output Button (Manual)
predict = Button(pred_layout, text="Predict", font=(
    15), width=16, bg="Gray", fg="White", command=pred_fn)
predict.place(x=0, y=440)

# Output Button (Automated)
predict_auto = Button(pred_layout, text="Auto Predict", font=(
    15), width=16, bg="Gray", fg="White", command=pred_fn_auto)
predict_auto.place(x=180, y=440)

pred_layout.mainloop()
