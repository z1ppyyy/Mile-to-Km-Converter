from tkinter import *

def convert_miles_to_km():
    """Convert the value from the miles_input Entry field from miles to kilometers and update the km_result_label."""
    user_input_miles = float(miles_input.get())
    km_result = user_input_miles * 1.609
    km_result_label.config(text=round(km_result, 2))

# Create and configure the window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=170)
window.config(padx=50, pady=35)

# Create and configure the labels
km_result_label = Label(text="0")
is_equal_label = Label(text="is equal to")
miles_label = Label(text="Miles")
kms_label = Label(text="Km")

# Create and configure the button and input field
calculate_button = Button(text="Calculate", command=convert_miles_to_km)
miles_input = Entry(width=10)

# Place the widgets on the grid
km_result_label.grid(column=1, row=1)
is_equal_label.grid(column=0, row=1)
miles_label.grid(column=2, row=0)
kms_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)
miles_input.grid(column=1, row=0)

window.mainloop()