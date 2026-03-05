import pandas as pd

data = {
    "user_id": [1,2,3,4,5],
    "age": [23,35,31,28,40],
    "purchases": [5,2,7,3,6]
}

df = pd.DataFrame(data)

print("Средний возраст:", df["age"].mean())
print("Среднее число покупок:", df["purchases"].mean())

top_users = df[df["purchases"] > 4]

print("Активные пользователи:")
print(top_users)
