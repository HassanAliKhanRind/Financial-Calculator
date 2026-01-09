# Financial-Calculator
📌 Project Overview

This project is a Python-based Financial Calculator that computes Net Present Value (NPV) and Internal Rate of Return (IRR) for a given series of cash flows.
It includes a Graphical User Interface (GUI) built using Tkinter, making it user-friendly for finance students and beginners.

The tool helps evaluate whether an investment project is financially viable based on discount rate comparison.

🎯 Features

Calculates Net Present Value (NPV)

Calculates Internal Rate of Return (IRR)

Interactive Tkinter GUI

Accepts comma-separated cash flows

Accepts discount rate in percentage

Displays profitability decision based on IRR vs Discount Rate

Error handling for invalid inputs

🛠 Tech Stack

Python

Tkinter (GUI)

Basic Financial Mathematics

🧮 Financial Logic Used

NPV Formula

𝑁
𝑃
𝑉
=
∑
𝐶
𝐹
𝑡
(
1
+
𝑟
)
𝑡
NPV=∑
(1+r)
t
CF
t
	​

	​


IRR Calculation:
IRR is calculated using an iterative approach, where the discount rate is adjusted until NPV changes sign.
