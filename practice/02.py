from tkinter import *
from tkinter.filedialog import askopenfilename

file_name=""
def fileopen():
    global file_name
    file_name = askopenfilename()
    #e.configure(text=file_name)

def showResult():
    f = open(file_name)
    S = f.read()
    # 알파벳 빈도수
    histogram = [0] * 26
    new = S.lower()
    for c in new:
        if c.isalpha():
            histogram[ord(c) - ord('a')] += 1
    for i in range(26):
        text.insert(END, chr(i + ord('a')) + " = " + str(histogram[i]) + "\n")
    f.close()

window=Tk()
window.title("Alpha")
frame1=Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=Y)
text=Text(frame1,width=50,height=15,wrap=WORD,yscrollcommand=scrollbar.set)
text.pack()
frame2=Frame(window)
frame2.pack()
Label(frame2,text="File name").pack(side=LEFT)
e = Entry(frame2,text="")
e.pack(side=LEFT)
Button(frame2,text="Open",command=fileopen).pack(side=LEFT)
Button(frame2,text="Result",command=showResult).pack(side=LEFT)
window.mainloop()



