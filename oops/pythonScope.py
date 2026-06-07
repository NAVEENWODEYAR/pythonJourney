"""
Python Developer Scope in AI/ML
-------------------------------
This program demonstrates typical tasks performed by
a Python AI/ML developer:

1. Load dataset
2. Explore data
3. Preprocess data
4. Train ML model
5. Evaluate model
6. Make predictions
"""

# Import required libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# =====================================================
# STEP 1: LOAD DATASET
# =====================================================

print("STEP 1: Loading Dataset")

iris = load_iris()

# Create DataFrame
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target

print(df.head())

# =====================================================
# STEP 2: DATA EXPLORATION
# =====================================================

print("\nSTEP 2: Dataset Information")

print("Shape:", df.shape)

print("\nTarget Classes:")
print(df["target"].value_counts())

# =====================================================
# STEP 3: FEATURE SELECTION
# =====================================================

X = df.drop("target", axis=1)
y = df["target"]

# =====================================================
# STEP 4: TRAIN TEST SPLIT
# =====================================================

print("\nSTEP 3: Splitting Dataset")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================================
# STEP 5: FEATURE SCALING
# =====================================================

print("STEP 4: Scaling Features")

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =====================================================
# STEP 6: MODEL TRAINING
# =====================================================

print("STEP 5: Training Model")

model = LogisticRegression()

model.fit(X_train, y_train)

print("Model Training Completed")

# =====================================================
# STEP 7: MODEL EVALUATION
# =====================================================

print("\nSTEP 6: Evaluating Model")

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# =====================================================
# STEP 8: PREDICTION ON NEW DATA
# =====================================================

print("\nSTEP 7: Prediction")

new_flower = [[5.1, 3.5, 1.4, 0.2]]

new_flower = scaler.transform(new_flower)

prediction = model.predict(new_flower)

flower_name = iris.target_names[prediction[0]]

print("Predicted Flower Type:", flower_name)

# =====================================================
# PYTHON DEVELOPER RESPONSIBILITIES IN AI/ML
# =====================================================

print("\nPython Developer Scope in AI/ML:")
print("✓ Data Collection")
print("✓ Data Cleaning")
print("✓ Data Analysis")
print("✓ Feature Engineering")
print("✓ Model Building")
print("✓ Model Evaluation")
print("✓ Model Deployment")
print("✓ API Development")
print("✓ Automation")
print("✓ MLOps Integration")