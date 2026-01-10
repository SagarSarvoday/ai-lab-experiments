# STEP 1: Import required libraries
from sklearn.tree import DecisionTreeClassifier

# STEP 2: Training data
# Input: [hours_studied]
# Output: 1 = Pass, 0 = Fail
X = [[1], [2], [3], [4], [5], [6], [7]]
y = [0, 0, 0, 0, 1, 1, 1]

# STEP 3: Create AI model
model = DecisionTreeClassifier()

# STEP 4: Train the model
model.fit(X, y)

# STEP 5: Take input from user
hours = int(input("Enter number of hours studied: "))

# STEP 6: AI Prediction
prediction = model.predict([[hours]])

# STEP 7: Output result
if prediction[0] == 1:
    print("AI Prediction: Student will PASS")
else:
    print("AI Prediction: Student will FAIL")
