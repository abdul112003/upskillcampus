#pip install pyshorteners

from tkinter import*
import pyshorteners

root= Tk()
root.title("URL Shortener link")
root.geometry("800x300")

def myUrl():
    url_entry=url.get()
    result=pyshorteners.Shortener().tinyurl.short(url_entry)
    urlEntry.insert(END,result)

Label(root, text="Generate Short URL",font=("Georgia 25 bold"), fg="Purple").pack(pady=10)

frame1=Frame(root)
Label(frame1, text="Paste URL here: ", font=("Georgia 15 bold")).pack(side=LEFT)

url = Entry(frame1, width="40", font=("Georgia 15 bold"))

url.pack()

frame1.pack(pady=10)

Button(root , text="Gererate Link", font=("Georgia 15 bold"), command=myUrl).pack(pady=10)

frame2=Frame(root)
Label(frame2, text="Copy URL: ", font=("Georgia 15 bold")).pack(side=LEFT)

urlEntry=Entry(frame2,width="25",fg="blue",font=("Georgia 15 bold"))
urlEntry.pack()
frame2.pack(pady=10)

root.mainloop()

