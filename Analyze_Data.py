import pandas as pd 

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85, 90, 95, 80]
}

df = pd.DataFrame(data)

print("Student Scores:\n")
print(df)

print("Average Score:", df["Score"].mean())