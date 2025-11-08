from faker import Faker
import random
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

fake = Faker()
X = []
# Faker: Generate 500 normal events for training
for i in range(500):
    proc = fake.word()
    length = len(proc)
    severity = random.choice([0,0,0,1])
    if len(X) == 0:
        X = np.array([[length, severity]])
    else:
        X = np.append(X, [[length, severity]], axis=0)

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)
joblib.dump(model, "iso_model.joblib")
print("✅ Model trained and saved as iso_model.joblib")
