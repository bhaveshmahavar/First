from tkinter import *
root = Tk()
root.geometry("500x300")

Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

name= Label(root, text="name")
mobile= Label(root, text="mobile")
gender= Label(root, text="gender")
email= Label(root, text="email")
paymentmode= Label(root, text="paymentmode")

name.grid(row=1, column=2)
mobile.grid(row=2, column=2)
gender.grid(row=3, column=2)
email.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)


namevalue= StringVar
mobiolevalue= StringVar
gendervalue= StringVar
emailvalue= StringVar
paymentmodevalue= StringVar
checkvalue= IntVar

nameentry = Entry(rooy, textvariable = namevalue)
mobileentry = Entry(rooy, textvariable = mobilevalue)
genderentry = Entry(rooy, textvariable = gendervalue)
emailentry = Entry(rooy, textvariable = emailvalue)
paymentmodeentry = Entry(rooy, textvariable = paymentmodevalue)


nameentry.grid(row=1, column=3)
mobileentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)
root.mainloop()