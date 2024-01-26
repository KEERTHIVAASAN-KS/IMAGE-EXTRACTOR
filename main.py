import requests
import extractor
import tkinter
import os

def get(url):
    request=requests.get(url)
    con=request.content
    con=con.decode("utf-8")
    return str(con)
def button():
    content=get(entry.get())
    dirname=(entry.get()).split("//")
    dirname=dirname[1].split("/")
    dirname=dirname[0]
    os.mkdir(dirname)
    extractor.getimage(content,dirname)

window=tkinter.Tk()

window.title("IMAGE EXTRACTOR")
window.geometry("360x50")

text=tkinter.Label(window,text="Enter URL:")
text.place(x=0,y=0)

entry=tkinter.Entry(window)
entry.place(x=70,y=0,width=200)

btn=tkinter.Button(window,text="EXTRACT",command=button)
btn.place(x=275,y=0)

window.mainloop()