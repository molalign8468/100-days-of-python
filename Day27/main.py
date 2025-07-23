import tkinter

def miles_to_km():
    miles = float(miles_input.get()) 
    km = miles * 1.60934           
    kilometer_result_label.config(text=f"{km:.2f} km") 

window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=150) 
window.config(padx=20, pady=20) 

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0) 

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(text="0 km")
kilometer_result_label.grid(column=1, row=1)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()