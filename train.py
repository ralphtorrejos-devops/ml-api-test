import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

X_train = train.drop('Outcome', axis=1)
y_train = train['Outcome']
X_test = test.drop('Outcome', axis=1)
y_test = test['Outcome']

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model test
joblib.dump(model, 'model.pkl')

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
