import pandas as pd
import matplotlib.pyplot as plt

# 📥 Read processed data
df = pd.read_csv("students_scores.csv")

# 📊 Calculate average marks
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# 🏆 Assign grades based on average
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(assign_grade)

# 🎨 Color mapping for grades
grade_colors = {
    "A+": "green",
    "A": "limegreen",
    "B": "gold",
    "C": "orange",
    "D": "red"
}
colors = df["Grade"].map(grade_colors)

# 📤 Save processed data
df.to_csv("students_scores_with_grades.csv", index=False)

# 📈 Visualization
plt.figure(figsize=(10, 6))
bars = plt.bar(df["Name"], df["Average"], color=colors)

# Add grade labels above each bar
for bar, grade in zip(bars, df["Grade"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        grade,
        ha='center',
        fontsize=10,
        fontweight='bold',
        color='black'
    )

plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("Average Marks per Student with Grades")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("sample_output.png")
plt.show()

