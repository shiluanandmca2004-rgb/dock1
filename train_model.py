import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: hours studied vs grade
X = np.array([[1], [2], [3], [4], [5], [6], [7]])
y = np.array([35, 45, 55, 65, 70, 80, 90])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "grade_model.pkl")

print("Model trained and saved!")
