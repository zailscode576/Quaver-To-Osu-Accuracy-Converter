import decimal
import tkinter as tk

def calculate_accuracy():
    try:
        m = int(marvelous_var.get())
    except ValueError:
        m = 0
    try:
        p = int(perfect_var.get())
    except ValueError:
        p = 0
    try:
        g = int(great_var.get())
    except ValueError:
        g = 0
    try:
        o = int(good_var.get())
    except ValueError:
        o = 0
    try:
        b = int(bad_var.get())
    except ValueError:
        b = 0
    try:
        mi = int(miss_var.get())
    except ValueError:
        mi = 0

    t = m + p + g + o + b + mi

    if t == 0:
        Acc_percentage = 0
    else:
        mc = decimal.Decimal(m) * 1
        pc = decimal.Decimal(p) * 1
        if toggle_var.get():  # Check if toggle button is activated
            pc *= decimal.Decimal(.98366666)
        gc = decimal.Decimal(g) * decimal.Decimal(2/3)
        oc = decimal.Decimal(o) * decimal.Decimal(1/3)
        bc = decimal.Decimal(b) * decimal.Decimal(1/6)
        mi = decimal.Decimal(m) * 0

        ALLc = mc + pc + gc + oc + bc + mi

        Acc = ALLc / t
        Acc = round(Acc, 5)

        Acc_percentage = Acc * 100

    accuracy_label.config(text=f"Accuracy: {Acc_percentage:.5f}%", fg="#ffffff")

def toggle_perfect_calculation():
    if toggle_var.get():
        toggle_var.set(False)  # Set toggle state to False (Off)
        toggle_button.config(text="v2 Off")
    else:
        toggle_var.set(True)   # Set toggle state to True (On)
        toggle_button.config(text="v2 On")

# GUI setup
root = tk.Tk()
root.title("QuaToOsu Acc Converter")
root.geometry("300x210")  # Adjust width and height as needed
root.configure(bg="#424549")

marvelous_var = tk.StringVar(value="0")
perfect_var = tk.StringVar(value="0")
great_var = tk.StringVar(value="0")
good_var = tk.StringVar(value="0")
bad_var = tk.StringVar(value="0")
miss_var = tk.StringVar(value="0")

toggle_var = tk.BooleanVar(value=False)  # Initialize toggle button state

tk.Label(root, text="Enter the number of marvelous:", bg="#424549", fg="#ffffff").grid(row=0, column=0, sticky="e")
tk.Entry(root, textvariable=marvelous_var).grid(row=0, column=1)
tk.Label(root, text="Enter the number of perfect:", bg="#424549", fg="#ffffff").grid(row=1, column=0, sticky="e")
tk.Entry(root, textvariable=perfect_var).grid(row=1, column=1)
tk.Label(root, text="Enter the number of great:", bg="#424549", fg="#ffffff").grid(row=2, column=0, sticky="e")
tk.Entry(root, textvariable=great_var).grid(row=2, column=1)
tk.Label(root, text="Enter the number of good:", bg="#424549", fg="#ffffff").grid(row=3, column=0, sticky="e")
tk.Entry(root, textvariable=good_var).grid(row=3, column=1)
tk.Label(root, text="Enter the number of bad:", bg="#424549", fg="#ffffff").grid(row=4, column=0, sticky="e")
tk.Entry(root, textvariable=bad_var).grid(row=4, column=1)
tk.Label(root, text="Enter the number of miss:", bg="#424549", fg="#ffffff").grid(row=5, column=0, sticky="e")
tk.Entry(root, textvariable=miss_var).grid(row=5, column=1)

info_label = tk.Label(root, text="Make sure to use the custom quaver judgements to setup a profile for whicher OD you are trying to convert to.\nOD9: marv = 16.5ms, perf = 37.5ms great = 70.5ms, good = 100.5ms, meh = 124.5ms ", bg="#424549", fg="#ffffff", wraplength=200, justify="left")
info_label.grid(row=0, column=2, rowspan=6, padx=(10, 0), sticky="w")

calculate_button = tk.Button(root, text="Calculate Accuracy", command=calculate_accuracy, bg="#ffffff", fg="#000000")
calculate_button.grid(row=6, column=0, columnspan=2)

accuracy_label = tk.Label(root, text="", bg="#424549", fg="#ffffff")
accuracy_label.grid(row=7, column=0, columnspan=2)

toggle_button = tk.Button(root, text="v2 Off", command=toggle_perfect_calculation, bg="#ffffff", fg="#000000")
toggle_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))

root.mainloop()
