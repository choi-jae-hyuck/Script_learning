from tkinter import *
from tkinter.filedialog import askopenfilename

def fileopen():
    file_name = e.get()
    f = open(file_name)
    S = f.read()
    # 알파벳 빈도수
    histogram = [0] * 26
    new = S.lower()
    for c in new:
        if c.isalpha():
            histogram[ord(c) - ord('a')] += 1
    maxCount=max(histogram)
    barW=(600-20)/26
    for i in range(26):
        canvas.create_rectangle(10+i*barW,290-(300*histogram[i]/maxCount)*0.9, 10+(i+1)*barW,300-10)
        canvas.create_text(10 + i * barW + 10, 300 - 5, text=chr(i + ord('a')))
        canvas.create_text(10 + i * barW + 10, 290 - (300 * histogram[i] / maxCount) * 0.9 - 10, text=histogram[i])
    f.close()


window=Tk()
window.title("Alpha")
frame1=Frame(window)
frame1.pack()
canvas = Canvas(frame1, bg="white", width=600, height=300)
canvas.pack()
frame2=Frame(window)
frame2.pack()
Label(frame2,text="Input URL").pack(side=LEFT)
e = Entry(frame2,text="")
e.pack(side=LEFT)
Button(frame2,text="Result",command=fileopen).pack(side=LEFT)
window.mainloop()





