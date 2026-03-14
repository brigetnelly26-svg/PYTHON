import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'Hours': [1, 2, 3, 4.5, 5, 6, 7, 8, 9, 10],
    'Scores': [20, 30, 50, 52, 60, 62, 70, 78, 85, 95]
}
df = pd.DataFrame(data)
print(df)

print(df.describe())

print(df.isnull().sum())
df = df.fillna(df.mean())

correlation = df['Hours'].corr(df['Scores'])
print(f"Correlation: {correlation}")

m, b = np.polyfit(df['Hours'], df['Scores'], 1)

plt.scatter(df['Hours'], df['Scores'], color='blue', label='Actual Data')
plt.plot(df['Hours'], m*df['Hours'] + b, color='red', label=f'Trend Line (y={m:.2f}x+{b:.2f})')

plt.title('Student Study Hours vs Scores')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.legend()
plt.show()

def predict_score():
    try:
        user_hours = float(input("Enter number of study hours: "))
        estimated_score = m * user_hours + b
        print(f"Estimated Score: {estimated_score:.2f}")
    except ValueError:
        print("Please enter a valid number.")

predict_score()