class ExpenseSharing:
    def __init__ (self, friends):
        self.friends = friends
        self.balance = {friend : 0 for friend in friends}

    def add_expenses(self, payer, amount, participants):
        split_amount = amount / len(participants)
        for participant in participants:
            self.balance[participant] -= split_amount
        self.balance[payer] += amount

    def calculate_settlement(self):
        creditors = []
        debitors = []
        
        for friend, balance in self.balance.items():
            if balance > 0:
                creditors.append((friend,balance))
            elif balance < 0:
                debitors.append((friend,-balance))
    
            while creditors and debitors:
                debtor, debt_amount = debitors.pop()
                creditor, credit_amount = creditors.pop()
    
                payment = min(debt_amount, credit_amount)
    
                print(f"{debtor} owes {creditor} : Rs.{payment:.2f}")
    
                if debt_amount > payment:
                    debitors.append((debtor, debt_amount - payment))
                if credit_amount > payment:
                    creditors.append((creditor, credit_amount - payment))


if __name__ == "main":
    friends = input("Enter the name of friends , seperated by commas :").split(",")
    friends = [friend.strip() for friend in friend]

    expense_sharing = ExpenseSharing(friends)

    while True:
        payer = input("Enter the name of the friend who paid :")
        if payer.lower() == "done":
            break

        amount = float(input("Enter the amount paid:"))

        participants = input("Enter the name of the participants for this expense seperated by commas :").split(",")
        participants = [participant.strip() for paticipant in participants]

        expense_sharing.add_expense(payer, amount, participants)

        print("\n Final settlement")
        expense_sharing.calculate_settlements()