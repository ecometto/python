# import tkinter as tk



# def window():
    
#     global counter
#     counter=1
    
#     def setEntry():
#         global counter
#         actualText= finalLb.cget('text')
#         finalText= actualText + ' ' + 'Line Nº ' + str(counter) +': ' + entry.get() +'\n' 
#         finalLb.config(text=finalText)
#         entry.delete(0, tk.END)
#         entry.focus_set()
#         counter=counter +1
    
    
#     win = tk.Tk()

#     win.geometry('400x400')
#     win.title("Greetings")

#     lb = tk.Label(win, text='Enter yur greeting here !')
#     lb.pack()

#     entry = tk.Entry(win)
#     entry.pack()

#     button = tk.Button(win, text="add", command=setEntry)
#     button.pack(pady=4)


#     finalLb=tk.Label(win)
#     finalLb.pack()

#     entry.focus_set()
#     win.mainloop()

# window()
