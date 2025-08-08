# 🏦 Bank Account & Saving Account (Python OOP)

This is a simple **Python Object-Oriented Programming** (OOP) project
that demonstrates **Inheritance** using two classes:

- **Account** → Basic banking operations like deposit and withdraw
- **SavingAccount** → Inherits from Account and adds interest calculation

---

## 📌 Features
- Create an account with a name and initial balance
- Deposit money
- Withdraw money (with balance check)
- Calculate interest for a given time period
- Update balance after adding interest

---

## 🛠 How It Works
1. **Account Class**
   - `deposit()` → Add money to account
   - `withdraw()` → Withdraw money if sufficient balance

2. **SavingAccount Class**
   - Inherits from `Account`
   - Adds `cal_interest()` method to calculate and update balance with interest
