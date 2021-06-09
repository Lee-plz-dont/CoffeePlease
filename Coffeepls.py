from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from typing import ValuesView
import smtplib
server = smtplib.SMTP("smtp.gmail.com", 587)

# sets radio var output to blank
output = ""

# creates window


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # creates menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        self.pack(fill=BOTH, expand=1)

        # handles File menu
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        # submit button
        SubmitButton = Button(self, text="Submit",
                              style='W.TButton', command=self.clickSubmit)

        # style submit button
        st = Style()
        st.configure('W.TButton', background='#afb5fc',
                     foreground='black', font=('Arial, 14'))

        # place submit button at pos
        SubmitButton.place(x=150, y=350)

        # logical test for radio selection and setting the global var 'output' to the radio selection
        def sel():
            global output
            choice = (var.get())
            if choice == 1:
                output = "Coffee"
                

            elif choice == 2:
                output = "Tea"
                

            elif choice == 3:
                output = "Snacks"
                

            else:

                output = "Invalid selection"
                

        var = IntVar()
        # creates radio buttons
        R1 = Radiobutton(root, text="Coffee", variable=var, value=1,
                         command=sel)
        R1.place(x=50, y=100)

        R2 = Radiobutton(root, text="Tea", variable=var, value=2,
                         command=sel)
        R2.place(x=50, y=150)

        R3 = Radiobutton(root, text="Snacks", variable=var, value=3,
                         command=sel)
        R3.place(x=50, y=200)

    # defines submit button behaviour
    def clickSubmit(self):
        server.starttls()
        server.login('<youremail@gmail.com>', '<YourAppKeyOrEmailPassword>')
        server.sendmail('<yourEmail@gmail.com>',
                        '<recipientEmail@domain.com>', "Hi, Can I have some " + str(output) + "please!")
        return messagebox.showinfo('your ask nicely has been placed', 'Thank you, your ask nicely has been placed and <Person Name> will make your ' + str(output) + ' shortly')

    # defines file menu exit behaviour
    def exitProgram(self):
        exit()


# defines window config
root = Tk()
app = Window(root)
root.wm_title("Coffeepls")
root.geometry("400x600")
# loops over main to persist window
root.mainloop()



# 100
