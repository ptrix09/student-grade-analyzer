import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students_scores.csv")
print("📄 Original Data:")
print(df.head())

# Calculate Total and Average
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Assign grades
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(assign_grade)

print("\n📊 Processed Data with Grades:")
print(df)

# Save processed data
df.to_csv("students_scores_with_grades.csv", index=False)

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("Average Marks per Student")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart as image
plt.savefig("sample_output.png")
plt.show()
