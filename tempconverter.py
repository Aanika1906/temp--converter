from tkinter import *
window=Tk()#creates window
window.geometry("500x500")#the measureemnts of the window
window.title("my first tkinter app")
window.config(background="pink")

def convert():
    celsius=int(celsiusentry.get())
    farehnhite=(celsius*(9/5))+32
    result.config(text="The temperature in fahrenheit is "+ str(farehnhite))



heading=Label(window,text="TEMPERATURE CONVERTER",font=("Arial",20),background="pink",foreground="dark blue")
celsius=Label(window,text="enter the celsius",font=("Arial",14),background="pink",foreground="dark blue")
celsiusentry=Entry(window,foreground="dark blue")
celsius.place(x=50,y=90)
celsiusentry.place(x=200,y=95)

submit_button=Button(window,text="calculate farenheit",command=convert)
submit_button.place(x=170,y=205)

result=Label(window,text=" total price:",font=("Arial",17),background="pink",foreground="blue")
result.place(x=120,y=285)

window.mainloop()
