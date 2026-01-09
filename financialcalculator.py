import tkinter as tk
from tkinter import messagebox


def NPV(cashflows, rate):
    npv = 0
    for n, cf in enumerate(cashflows):
        npv += cf / (1 + rate) ** n
    return npv

def IRR(cashflows):
    npv_prev = NPV(cashflows, 0)
    for r in [x / 10000 for x in range(1, 10000)]:  # 0%–100%
        npv_curr = NPV(cashflows, r)
        if npv_prev > 0 and npv_curr < 0:
            return round((r + (r - 0.0001)) / 2, 5)  # average of boundary
        npv_prev = npv_curr
    return None


def calculate():
    try:
        # Get user input
        cashflows = list(map(float, cashflow_entry.get().split(',')))
        rate = float(rate_entry.get()) / 100  # convert % to decimal

        # Calculate NPV
        npv_value = NPV(cashflows, rate)
        npv_label.config(text=f"NPV = {npv_value:,.2f}")

        # Calculate IRR
        irr_value = IRR(cashflows)
        if irr_value is not None:
            irr_label.config(text=f"IRR = {irr_value * 100:.2f}%")
            message = ""
            if irr_value > rate:
                message = "Project is profitable (IRR > Discount Rate)"
            else:
                message = "Project not attractive (IRR < Discount Rate)"
            result_label.config(text=message)
        else:
            irr_label.config(text="IRR not found")
            result_label.config(text="Cashflows may not produce a valid IRR")

    except Exception:
        messagebox.showerror("Input Error", "Please enter valid numbers separated by commas.")

#GUI Layout 

root = tk.Tk()
root.title("Financial Calculator NPV & IRR")
root.geometry("600x500")
root.configure(bg="#f3f6f9")

# Title
title_label = tk.Label(root, text="FINANCIAL CALCULATOR", font=("Times New Roman", 24, "bold"), bg="#f3f6f9")
title_label.pack(pady=10)

# Cashflow input
tk.Label(root, text="Enter Cashflows ( comma separated):", bg="#f3f6f9", font=("Times New Roman", 15)).pack()
cashflow_entry = tk.Entry(root, width=40, justify="center")
cashflow_entry.insert(0, "-1000, 300, 680, 500,600")
cashflow_entry.pack(pady=5)

# Rate input
tk.Label(root, text="Enter Discount Rate (%):", bg="#f3f6f9", font=("Times New Roman", 15)).pack()
rate_entry = tk.Entry(root, width=15, justify="center")
rate_entry.insert(0, "11")
rate_entry.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", font=("Times New Roman", 13, "bold"), bg="#0078D7", fg="white", command=calculate)
calc_button.pack(pady=10)

# Result Labels
npv_label = tk.Label(root, text="NPV = ", font=("Times New Roman", 13, "bold"), bg="#f3f6f9")
npv_label.pack()

irr_label = tk.Label(root, text="IRR = ", font=("Times New Roman", 13, "bold"), bg="#f3f6f9")
irr_label.pack()

result_label = tk.Label(root, text="", font=("Times New Roman", 12), bg="#f3f6f9", fg="green")
result_label.pack(pady=10)

root.mainloop()
