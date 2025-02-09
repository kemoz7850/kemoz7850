def submit(num, window=None):
    if num == "login":
        file1 = open("data.txt", "r+")
        name = name_var.get() or " "
        password = passw_var.get() or " "
        lst = file1.readlines(0)
        for i in range(len(lst)):
            lst[i] = lst[i].strip("\n")
        for i in range(len(lst)):
            if name == lst[i] and password == lst[i + 1]:
                messagebox.showinfo(title="successful", message="logged in successfully")
                lst.append("true")
                print("done")
                break
        if lst[len(lst) - 1] != "true":
            messagebox.showerror("unsuccessful", "Wrong Username or Password")

        file1.close()
        name_var.set("")
        passw_var.set("")
    if num == "register":
        file1 = open("data.txt", "a")
        name1 = name_var1.get()
        password1 = passw_var1.get()
        if name1 and password1 != "":
            if len(password1) >= 8:
                root.deiconify()
                file1.write(f"{name1}\n")
                file1.writelines(f"{password1}\n")
                file1.close()
                name_var1.set("")
                passw_var1.set("")
                if window:
                    window.destroy()  # Close the registration window after successful registration
            else:
                messagebox.showerror("unsuccessful", "Password must be higher than 8")
        else:
            messagebox.showerror("unsuccessful", "Invalid Format")

def regstr(g='1'):
    newWindow = Toplevel(root)
    newWindow.resizable(0, 0)
    newWindow.title("Register")
    username = tk.Label(newWindow, text="Username: ")
    name_entry = tk.Entry(newWindow, textvariable=name_var1, font=('calibre', 10, 'normal'))
    password = tk.Label(newWindow, text="Password: ")
    passw_entry = tk.Entry(newWindow, textvariable=passw_var1, font=('calibre', 10, 'normal'), show='*')
    sub_btn = tk.Button(newWindow, text='Submit', command=lambda: submit("register", newWindow))
    username.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    password.grid(row=1, column=0)
    passw_entry.grid(row=1, column=1)
    sub_btn.grid(row=2, column=1)

root.title("Login")
username = tk.Label(root, text="Username: ")
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
password = tk.Label(root, text="Password: ")
passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
sub_btn = tk.Button(root, text='Submit', command=lambda: submit("login"))
register = tk.Button(root, text='Register', command=regstr)
username.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
password.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)
register.grid(row=2, column=0)
mainloop()