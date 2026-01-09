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

NPV Formula:

NPV=∑(1+r)tCFt​​
	​	

IRR Calculation:
IRR is calculated using an iterative approach, where the discount rate is adjusted until NPV changes sign.

Net Present Value (NPV): At a discount rate of 11%, the NPV is 583.01, which indicates that the project creates value and generates returns above the cost of capital.

Internal Rate of Return (IRR): The calculated IRR is 33.79%, representing the project’s expected annual return.

Since the IRR (33.79%) is significantly higher than the discount rate (11%), the project is financially profitable and acceptable.
