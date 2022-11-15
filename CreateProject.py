import tkinter as tk
from cryptography.fernet import Fernet
import csv

def new_user():
    global new_user_screen
    new_user_screen = tk.Tk()

    width_initial = 300
    height_initial = 220

    screen_width = new_user_screen.winfo_screenwidth()
    screen_height = new_user_screen.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    new_user_screen.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                              x_coordinate, y_coordinate))
    
    new_user_screen.title('PersonalVault™ New User')
    new_user_screen.columnconfigure([0, 2], minsize=50)
    new_user_screen.rowconfigure([0, 3], minsize=95)
    tk.Button(font='Helvetica', text='Go Back',
              bg='#ae4df4', fg='white', borderwidth=3,
              command=lambda: route_to_initial(new_user_screen)
              ).grid(row=0, column=0, padx=20, pady=8, sticky='nw')
    tk.Label(text='Please enter the following details:', relief='groove',
             bg='white', font='Helvetica').grid(row=0, column=0,
                                                padx=20, pady=20, stick='s')
    in_user = tk.StringVar()
    in_pass = tk.StringVar()
    verify_pass = tk.StringVar()
    tk.Label(text='Username:', font='Helvetica').grid(row=1,column=0,
                                                      padx=20, stick='nw')
    tk.Entry(textvariable=in_user).grid(row=1,column=0, stick='ne')
    tk.Label(text='Password:', font='Helvetica').grid(row=2,column=0,
                                                      padx=20, stick='nw')
    tk.Entry(textvariable=in_pass, show='*').grid(row=2,column=0, stick='ne')
    tk.Label(text='Confirm:', font='Helvetica').grid(row=3,column=0,
                                                     padx=20, stick='nw')
    tk.Entry(textvariable=verify_pass, show='*').grid(row=3,column=0,
                                                      stick='ne')
    tk.Button(text='Register', font='Helvetica', borderwidth=3,
              bg='#ae4df4', fg='white',
              command=lambda: check_new_user(in_user, in_pass, verify_pass)
              ).grid(row=3, column=0, padx=20, stick='ew')

    new_user_screen.mainloop()

def opening_secret_data():
    data = []
    with open('secret_data.csv', 'r') as input_data:
        input_info = csv.reader(input_data, delimiter=',')
        for row in input_info:
            data.append(row)
    decrypt_info = []

    with open('key.txt', 'r') as key:
        key = key.readline()
    f = Fernet(key)
    for row in data:
        temp = []
        for col in row:
            temp_data = f.decrypt(col.encode()).decode()
            temp.append(temp_data)
        decrypt_info.append(temp)
    return decrypt_info

def route_to_register(sender):
    sender.destroy()
    new_user()
    
def username_taken(username):
    new_user_screen.destroy()
    taken_screen = tk.Tk()

    width_initial = 300
    height_initial = 100

    screen_width = taken_screen.winfo_screenwidth()
    screen_height = taken_screen.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    taken_screen.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                           x_coordinate, y_coordinate))
    taken_screen.title('Username Taken')
    message = 'Username "' + username + '" is already taken.'
    tk.Label(text=message, font='Helvetica', relief='groove',
             bg='white').pack(pady=15)
    tk.Button(text='OK', font='Helvetica', bg='#ae4df4', fg='white',
              command=lambda: route_to_register(taken_screen)).pack(pady=5)
    taken_screen.mainloop()
    
def no_match():
    new_user_screen.destroy()
    no_match_pass = tk.Tk()

    width_initial = 300
    height_initial = 100

    screen_width = no_match_pass.winfo_screenwidth()
    screen_height = no_match_pass.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    no_match_pass.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                            x_coordinate, y_coordinate))
    no_match_pass.title('Could not verify passwords')
    tk.Label(text='Passwords do not match',
             font='Helvetica', relief='groove', bg='white').pack(pady=15)
    tk.Button(text='OK', font='Helvetica', bg='#ae4df4', fg='white',
              command=lambda: route_to_register(no_match_pass)).pack(pady=5)
    no_match_pass.mainloop()
    
def no_input():
    new_user_screen.destroy()
    no_input_given = tk.Tk()

    width_initial = 400
    height_initial = 100

    screen_width = no_input_given.winfo_screenwidth()
    screen_height = no_input_given.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    no_input_given.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                             x_coordinate, y_coordinate))
    no_input_given.title('No input provided')
    tk.Label(text='No input detected for either username or password',
             font='Helvetica', relief='groove', bg='white').pack(pady=15)
    tk.Button(text='OK', font='Helvetica', bg='#ae4df4', fg='white',
              command=lambda: route_to_register(no_input_given)).pack(pady=5)
    no_input_given.mainloop()

def route_to_account(username, password, old_msg, sender):
    sender.destroy()
    account(username, password, old_msg)

def sign_off():
    account_page.destroy()
    initial_screen_page()

def account(username, password, old_msg):
    global account_page
    account_page = tk.Tk()

    width_initial = 850
    height_initial = 500

    screen_width = account_page.winfo_screenwidth()
    screen_height = account_page.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    account_page.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                            x_coordinate, y_coordinate))
    account_page.title(username + '\'s PersonalVault™')
    account_page.rowconfigure([0, 1], minsize=60)
    account_page.columnconfigure([0, 1], minsize=425)

    logo = tk.PhotoImage(file = r'vaultLargeLogo.png')
    tk.Label(image=logo, relief='groove').grid(row=0, column=0, stick='w',
                                               padx=20, pady=20)
    tk.Button(text='Sign Off', font='Helvetica', bg='#ae4df4', borderwidth=3,
              fg='white', command=sign_off).grid(row=2, column=0, stick='nw',
                                                 padx=20, pady=13)
    secret_info = tk.Text(height=20, width=50)
    secret_info.grid(row=1, column=0, padx=20, stick='w')
    if len(old_msg) != 0:
        secret_info.insert(tk.END, old_msg)
    how_to = 'To use your PersonalVault™, type your secret message in the text'
    how_to += 'editor, hit "Save and Secure" for your message to be encrypted'
    how_to += 'and stored away for the next time you log on.'
    tk.Label(text=how_to, wraplength=400, font='Helvetica', bg='white',
             relief='groove').grid(row=0, column=1, stick='nw', pady=20)
    tk.Button(text='Save and Secure', font='Helvetica', bg='#ae4df4',
              borderwidth=3, fg='white',
              command=lambda: secure_input(username, password, secret_info)
              ).grid(row=1, column=1, stick='w')
    account_page.mainloop()

def secure_input(username, password, secret_info):
    data = secret_info.get('1.0', 'end-1c')
    with open('key.txt', 'r') as key:
        key = key.readline()
    f = Fernet(key)
    login = False
    decrypt_info = opening_secret_data()
    encrypt_data = []
    for row in decrypt_info:
        if username == row[0]:
            row[2] = data
            login = True
            for row in decrypt_info:
                temp = []
                for col in row:
                    temp_data = f.encrypt(col.encode()).decode()
                    temp.append(temp_data)
                encrypt_data.append(temp)
            break    
    if login == False:
        for row in decrypt_info:
            temp = []
            for col in row:
                temp_data = f.encrypt(col.encode()).decode()
                temp.append(temp_data)
            encrypt_data.append(temp)
        encrypt_user = f.encrypt(username.encode()).decode()
        encrypt_pass = f.encrypt(password.encode()).decode()
        encrypt_msg = f.encrypt(data.encode()).decode()
        temp = [encrypt_user, encrypt_pass, encrypt_msg]
        encrypt_data.append(temp)
        
    with open('secret_data.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerows(encrypt_data)
    return success_encrypt(username, password, data)
    
def success_encrypt(username, password, old_msg):
    global success_input
    account_page.destroy()
    success_input = tk.Tk()

    width_initial = 400
    height_initial = 100

    screen_width = success_input.winfo_screenwidth()
    screen_height = success_input.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    success_input.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                            x_coordinate, y_coordinate))
 
    success_input.title('Successful Input')
    tk.Label(text='Your message is now secret safe with your account!',
             font='Helvetica', relief='groove', bg='white').pack(pady=15)
    tk.Button(text='OK', font='Helvetica', bg='#ae4df4', fg='white',
              command=lambda: route_to_account(username, password,
                                               old_msg, success_input)
              ).pack(pady=5)
    success_input.mainloop()  
    
def check_new_user(username, password, verify_pass):
    if len(username.get()) == 0 or len(password.get()) == 0:
        return no_input()
    secret_data = opening_secret_data()
    for row in secret_data:
        if row[0] == username.get():
            return username_taken(row[0])
    if password.get() != verify_pass.get():
        return no_match()
    data = ''
    return route_to_account(username.get(), password.get(), data,
                            new_user_screen)

def about():
    initial_screen.destroy()
    about_page = tk.Tk()

    width_initial = 300
    height_initial = 300

    screen_width = about_page.winfo_screenwidth()
    screen_height = about_page.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    about_page.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                         x_coordinate, y_coordinate))
    about_page.title('About Page')
    about_page.rowconfigure([0, 1], minsize=60)
    about_page.columnconfigure(0, minsize=425)

    tk.Button(text='Go Back', font='Helvetica', bg='#ae4df4', fg='white',
              borderwidth=3, command=lambda: route_to_initial(about_page)
              ).grid(stick='nw', padx=20, pady=8, row=0)

    message = 'Hey there!\n\n You stumbled upon Version 2.0 of my secure storage program.'
    message += '\n\nThis program uses csv, tkinter, and cryptography to have an'
    message += 'easy way to access and securely store your messages.'
    message += '\n\nEnjoy and stay secure!'
    tk.Label(text=message, font='Helvetica', bg='white', justify=tk.LEFT,
             wraplength=257).grid(row=1, stick='nw', padx=20)
    about_page.mainloop()
    
def initial_screen_page():
    global initial_screen
    initial_screen = tk.Tk()

    width_initial = 300
    height_initial = 425

    screen_width = initial_screen.winfo_screenwidth()
    screen_height = initial_screen.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    initial_screen.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                             x_coordinate, y_coordinate))
    
    initial_screen.title('PersonalVault™ Landing')
    logo = tk.PhotoImage(file = r'C:\Users\dshpu\Desktop\stuff\FieldSess\GUI-File-Login-System\vaultLogo.png')
    tk.Button(image=logo, borderwidth=3, command=about).pack()
    
    tk.Label(width='45', height='2', 
             text='Please select whether you are a new or returning user.',
             font='Helvetica', bg='white',
             wraplength='250', relief='groove').pack(pady=6)
    
    tk.Button(width='15', height='1', text='New User', font='Helvetica',
              borderwidth=3, bg='#ae4df4', fg='white',
              command=lambda: route_to_register(initial_screen)).pack(pady=6)
    
    tk.Button(width='15', text='Returning User', height='1', borderwidth=3,
              font='Helvetica', bg='#ae4df4', fg='white',
              command=lambda: route_to_login(initial_screen)).pack(pady=6)
    
    initial_screen.mainloop()

def route_to_login(sender):
    sender.destroy()
    old_user()

def old_user():
    global old_user_screen
    old_user_screen = tk.Tk()

    width_initial = 300
    height_initial = 225

    screen_width = old_user_screen.winfo_screenwidth()
    screen_height = old_user_screen.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    old_user_screen.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                              x_coordinate, y_coordinate))
    old_user_screen.title('PersonalVault™ New User')
    old_user_screen.columnconfigure([0, 2], minsize=50)
    old_user_screen.rowconfigure([0, 3], minsize=95)

    tk.Button(font='Helvetica', text='Go Back',
              bg='#ae4df4', fg='white', borderwidth=3,
              command=lambda: route_to_initial(old_user_screen)
              ).grid(row=0, column=0, padx=20, pady=8, sticky='nw')
    tk.Label(text='Please enter the following details:', relief='groove',
             bg='white', font='Helvetica').grid(row=0, column=0,
                                                padx=20, pady=20, stick='s')
    in_user = tk.StringVar()
    in_pass = tk.StringVar()

    tk.Label(text='Username:', font='Helvetica').grid(row=1,column=0,
                                                      padx=20, stick='nw')
    tk.Entry(textvariable=in_user).grid(row=1,column=0, stick='ne')
    tk.Label(text='Password:', font='Helvetica').grid(row=2,column=0,
                                                      padx=20, stick='nw')
    tk.Entry(textvariable=in_pass, show='*').grid(row=2,column=0, stick='ne')
    tk.Button(text='Login', font='Helvetica',
              bg='#ae4df4', fg='white', borderwidth=3,
              command=lambda: check_old_user(in_user, in_pass)
              ).grid(row=3, column=0, padx=20, stick='ew')
    old_user_screen.mainloop()

def check_old_user(username, password):
    secret_data = opening_secret_data()
    for row in secret_data:
        if row[0] == username.get():
            if row[1] == password.get():
                return route_to_account(username.get(), password.get(),
                                        row[2], old_user_screen)
    return invalid_login()

def invalid_login():
    global bad_login_page
    old_user_screen.destroy()
    bad_login_page = tk.Tk()

    width_initial = 300
    height_initial = 100

    screen_width = bad_login_page.winfo_screenwidth()
    screen_height = bad_login_page.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_initial/2)
    y_coordinate = (screen_height/2) - (height_initial/2)

    bad_login_page.geometry('%dx%d+%d+%d' % (width_initial, height_initial,
                                             x_coordinate, y_coordinate))
    bad_login_page.title('Failed Login')
    tk.Label(text='Invalid Username or Password!',
             font='Helvetica', relief='groove', bg='white').pack(pady=15)
    tk.Button(text='OK', font='Helvetica', bg='#ae4df4', fg='white',
              command=lambda: route_to_login(bad_login_page)).pack(pady=5)
    bad_login_page.mainloop()  

def route_to_initial(sender):
    sender.destroy()
    initial_screen_page()


initial_screen_page()
