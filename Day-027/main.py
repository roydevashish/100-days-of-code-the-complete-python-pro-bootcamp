import tkinter

WindowApp = tkinter.Tk()
WindowApp.title("Mile to KM Convertor")
WindowApp.config(padx=80, pady=20)

mile_entry = tkinter.Entry(width=7)
mile_entry.grid(row=0, column=1)

mile_label = tkinter.Label(text="Miles")
mile_label.grid(row=0, column=2)

a_label = tkinter.Label(text="is equal to")
a_label.grid(row=1, column=0)

km_label = tkinter.Label(text="0")
km_label.grid(row=1, column=1)

mile_label = tkinter.Label(text="KM")
mile_label.grid(row=1, column=2)

def MileToKM():
    update_text = round(float(mile_entry.get()) * 1.609)
    km_label["text"] = f"{update_text}"

calculate_button = tkinter.Button(text="Calculate", command=MileToKM)
calculate_button.grid(row=2, column=1)

WindowApp.mainloop()