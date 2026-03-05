transactions = [
    {"user_id": 1, "amount": 120},
    {"user_id": 2, "amount": 5400},
    {"user_id": 3, "amount": 230},
    {"user_id": 4, "amount": 12000},
    {"user_id": 5, "amount": 80}
]

suspicious_transactions = []

for transaction in transactions:
    if transaction["amount"] > 3000:
        suspicious_transactions.append(transaction)

print("Подозрительные транзакции:")
print(suspicious_transactions)
