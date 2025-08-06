# GooglePay-Shared-Expenses
Expense Sharing System – Project Report
 1. Project Overview
The Expense Sharing System simplifies cost distribution among a group of friends by fairly splitting expenses. It calculates who owes whom and how much after all shared expenses are accounted for.

This project is implemented in Python and can be extended with data science tools to analyze spending patterns.

2. Methodology
Expense Splitting Logic:

Equal Contribution:

When an expense is added, the total amount is split equally among all participants.

The payer’s balance increases, and each participant’s balance decreases by their share.

Balance Calculation:

Each person's net balance is maintained.

At the end, people with negative balances (debitors) owe money to those with positive balances (creditors).

Settlement is done by minimizing the number of transactions.

3. Dataset Details and Preprocessing
In this basic version:

Input is taken from the user at runtime (names, amount, payer, and participants).

The data is stored internally in a balance dictionary.

Sample Internal Structure:
self.balance = {
    'Alice': 100.0,
    'Bob': -50.0,
    'Charlie': -50.0
}
Optional Extensions:

Store data in a CSV/JSON file for persistence.

Add timestamps to each transaction.

4. Key Insights and Special Case Handling
Key Functionalities:
Equal splitting of any amount.

Dynamic support for any number of friends or transactions.

Calculates optimal settlements to reduce the number of payments.

Special Cases:
Payer is also a participant — Already handled.

Refunds or missed payments — Not handled yet.

Weighted sharing (unequal splits) — Not implemented but can be added.

Duplicate names or typos — Not handled (could use name validation or selection from a list).

5. Data Science Implementation (Optional Enhancements)
With integration of Pandas, NumPy, and Matplotlib, we can:

a. Track Spending Per Person
import pandas as pd

df = pd.DataFrame([
    {'payer': 'Alice', 'amount': 300, 'participants': ['Alice', 'Bob', 'Charlie']},
    {'payer': 'Bob', 'amount': 150, 'participants': ['Alice', 'Bob']},
])
b. Analyze & Visualize
import matplotlib.pyplot as plt

totals = {'Alice': 450, 'Bob': 150, 'Charlie': 0}
plt.bar(totals.keys(), totals.values())
plt.title("Total Spending Per User")
plt.ylabel("Amount (Rs.)")
plt.show()

6. Sample Inputs and Outputs
Input:
Friends: Alice, Bob, Charlie

Alice paid Rs.300 for Alice, Bob, Charlie  
Bob paid Rs.150 for Alice, Bob  

Output:
Charlie owes Alice : Rs.100.00  
Bob owes Alice : Rs.50.00

7. Challenges Faced
Input sanitization: Preventing errors due to typos or invalid names.

Logic bug in settlement loop placement inside the loop.

Handling floating point precision errors.

8. Possible Improvements
GUI or Web App using Flask or Tkinter

Weighted Contributions (e.g., % based or fixed amount)

CSV Import/Export for expenses

Debt Minimization Algorithm

Mobile App Integration

Group-based analytics and leaderboards

9. Conclusion
This project provides a simple and extendable solution for expense sharing. With Python at its core and optional data science libraries, it offers the potential for real-world use and deep expense analysis.







