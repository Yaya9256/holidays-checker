# Import modules.
import datetime as dt
import smtplib
from email.mime.text import MIMEText
from tkinter import *

# create TKinter canvas.
canvas = Tk()
canvas.title("WAS THE HOLIDAY FOUND?")

# MY OWN FUNCTIONS.
# Close TKinter window.
def klik():
    canvas.destroy()

# Send e-mail.
def sendMail():
    global cislo
    while cislo != 0:
        s=smtplib.SMTP(mail_ucet, port)
        s.ehlo()
        s.starttls()
        s.login(mail_login_name, mail_login_pass)

        msg = MIMEText(str(sprava[cislo-1]))
        msg['subject'] = msg_subject
        msg['from'] = msg_from
        msg['To'] = msg_to

        s.sendmail(str(mail_login_name),([email[cislo-1]]), msg.as_string())
        print("email sent!")
        cislo -= 1

# Find type of holiday.
def najdi():
    if stack == "BIRTHDAY":
        return najdi2
    elif stack == "DAY OF NAME":
        return najdi1
    elif stack == "HOLIDAY":
        return najdi4
    elif stack == "DAY":
        return najdi5
    else:
        return najdi3

# Insert text in to e-mail, message to the recipient.
def spravaTEXT():
    if stack == "BIRTHDAY":
        return ("All the best to yours today " + str(stary) +
                ". We wish you good health and happiness on your birthday.")
    elif stack == "DAY OF NAME":
        return "We wish you all the best for your day of name, good luck and health."
    elif stack == "HOLIDAY":
        return "TODAY IS HOLIDAY."
    elif stack == "DAY":
        return "TODAY IS RESERVED DAY."
    else:
        return najdi3

# Základné premenné
dateNow = dt.datetime.now()
year, month, day = dateNow.year, dateNow.month, dateNow.day
den, mesiac, rok, meno, sviatok = [], [], [], [], [],
mail, data, strukt, sprava, email = [], [], [], [], []

najdi1 = "Holiday found: DAY OF NAME."
najdi2 = "Holiday found: BIRTHDAY."
najdi3 = "Holiday not found! No email to send today!"
najdi4 = "Holiday found: HOLIDAY."
najdi5 = "Holiday found: RESERVED DAY"

mail1 = "E-MAIL sent successfully."
mailPocet = ""

stack = ""
vek = ""
menoTk = ""

sprava1 = "We wish you all the best for your day of name, good luck and health."
sprava2 = ("All the best to yours today " + str(vek) +
           ". We wish you good health and happiness on your birthday.")
sprava3 = "NO MESSAGE"

# It opens and retrieves the data needed to log in to the e-mail.
with open("mail copy.txt") as file:
    for line in file:
        account = line.split(",")
        ucet, passw = account[0], account[1]

# Parameters needed to log in to the account and send an email.
mail_ucet ="smtp.gmail.com"
port = 25
mail_login_name = ucet
mail_login_pass = passw
msg_subject = "found HOLIDAY"
msg_from = "pybot-sviatky"
msg_to = "addressee"

# Converts int output to str and adds 0 to the string if i is a single digit.
if day < 10:
    pday = "0" + str(day)
else:
    pday = str(day)
if month < 10:
    pmonth = "0" + str(month)
else:
    pmonth = str(month)

# program logic, open file reads data, compares and evaluates, further controls the program.
with open("data copy.txt") as file:
    for line in file:
        data = line.split(",")
        den, mesiac, rok, meno, sviatok, mail = data[0], data[1], data[2], data[3], data[4], data[5]
        vek = int(year) - int(rok)
        vek1 = vek

        if pday == den and pmonth == mesiac:
            strukt = meno, sviatok
            global stary
            stary = vek
            menoTk = meno

            try:
                if strukt[1] == 'BIRTHDAY':
                    sprava.append("Today is " + str(day) + "." + str(month) + " and " +
                                  sviatok + " has " + meno + " and has " + str(vek)+" years." +
                                  "\n\nAll the best to yours today " + str(vek) +
                                  ". We wish you good health and happiness on your birthday.")
                    email.append(mail)
                    print(najdi2)
                    stack = strukt[1]

                elif strukt[1] == 'DAY OF NAME':
                    sprava.append("Today is "+str(day)+"."+str(month)+" and "+sviatok+" has "+meno +"\n\nWe wish you all the best for your day of name, good luck and health.")
                    email.append(mail)
                    print(najdi1)
                    stack = strukt[1]

                elif strukt[1] == "HOLIDAY":
                    sprava.append("Today is "+str(day)+"." +str(month)+" and is "+meno)
                    email.append(mail)
                    print(najdi4)
                    stack = strukt[1]

                elif strukt[1] == "DAY":
                    sprava.append("Today is "+str(day)+"."+str(month)+" and is "+meno)
                    email.append(mail)
                    print(najdi5)
                    stack = strukt[1]

            except IndexError:
                print(najdi3)
                stack = strukt[1]

cislo = len(sprava)
str(email)

# The e-mail function itself calls.
sendMail()

# Labels for Tkinter window in windows.
popis = Label(canvas, text="RESULT: ", font=("Helvetica", 15))
popis.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

vysledok = Label(canvas, text=najdi(), font=("Helvetica", 15))
vysledok.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

meno = Label(canvas, text=menoTk, font=("Helvetica", 15))
meno.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

sprava = Entry(canvas, width=100, borderwidth=2, font=("Helvetica", 12))
sprava.insert(0, spravaTEXT())
sprava.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

but1 = Button(canvas, text="CLOSE WINDOW!", comman=klik, font=("Helvetica", 15))
but1.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

# Loop to keep the window open.
canvas.mainloop()

# End of program.
