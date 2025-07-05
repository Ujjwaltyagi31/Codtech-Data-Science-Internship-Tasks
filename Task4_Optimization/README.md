# 📊 Task 4 – Optimization Model: Resource Allocation using Linear Programming | CodTech Data Science Internship

This project solves a **real-world resource allocation problem** using **Linear Programming (LP)** with the `PuLP` library in Python.

---

## 📌 Objective

To determine the **optimal number of units to produce** for two products (A & B) in a factory setting, in order to **maximize total profit**, while considering limited machine hours as constraints.

---

## 🧠 Problem Statement

A company produces two products:

| Product     | Machine 1 (hrs) | Machine 2 (hrs) | Profit per Unit |
|-------------|------------------|------------------|-----------------|
| Product A   | 2                | 1                | ₹30             |
| Product B   | 1                | 1                | ₹20             |

- **Machine 1** is available for **100 hours**
- **Machine 2** is available for **80 hours**

### 🎯 Goal:  
Maximize profit while staying within machine hour constraints.

---

## 🧮 Linear Programming Formulation

**Decision Variables:**
- `x`: Units of Product A
- `y`: Units of Product B

**Objective Function (Maximize):**  
`30x + 20y`

**Subject to Constraints:**
- `2x + y ≤ 100` (Machine 1)
- `x + y ≤ 80` (Machine 2)

---

## 🛠️ Tools Used

- Python
- [PuLP – Linear Programming Library](https://coin-or.github.io/pulp/)
- Optional: Matplotlib (for visualization)

---

## 📁 Files Included

| File Name                | Description                               |
|--------------------------|-------------------------------------------|
| `optimization_model.py` | Python script for LP model                |
| `README.md`              | Documentation for Task 4                  |

---

## ▶️ How to Run

1. Install the required library:
   ```bash
   pip install pulp
2. Run the optimization script:
   ```bash
   python optimization_model.py

    ```

   ---

## ✅ Output Example
   
Produce 20 units of Product A
Produce 60 units of Product B
Maximum Profit: ₹1800

---

## 📈 Insights
The model helps identify the most profitable production strategy within resource limits.

Easily adaptable to more complex real-world supply chain or manufacturing scenarios.

---

## 🏅 Internship
This project is completed as part of the Data Science Internship at CodTech IT Solutions, under Task 4 – Optimization Using Python.

---
### Data is valuable, but optimized decisions powered by data are priceless. Task 4 helped me experience that firsthand!
