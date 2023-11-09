import random
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt

# Define the possible values for each attribute
genders = ["Male", "Female"]
ages = list(range(18, 71))  # Age between 18 and 70
pos_state_of_mind = [0, 1]
music_preferences = ["Classical", "Jazz", "Pop", "Rock", "Hip-Hop", "Country", "Electronic", "R&B"]
religious_preferences = ["Atheist", "Agnostic", "Christian", "Muslim", "Buddhist", "Hindu", "Jewish", "Other"]

# Generate 500 rows of data
data = []
for _ in range(100_000):
    gender = random.choice(genders)
    age = random.choice(ages)
    state_of_mind = random.choice(pos_state_of_mind)
    music_pref = random.choice(music_preferences)
    religious = random.choice(religious_preferences)
    data.append([gender, age, state_of_mind, music_pref, religious])

# Store the data in a CSV file
df = pd.DataFrame(data, columns=["Gender", "Age", "Pos_State_of_Mind", "Music_Pref", "Religious"])
df.to_csv("generated_data.csv", index=False)

# Display the first few rows of the Pandas DataFrame
print(df.dtypes)


# Encode categorical variables
label_encoder = LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
df["Religious"] = label_encoder.fit_transform(df["Religious"])


# Split the data into features (X) and target (y)
X = df[['Gender', 'Age']]
y = df["Music_Pref"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Selecting the model - decision tree



dtModel = DecisionTreeClassifier()



# Fitting the model
dtModel.fit(X_train, y_train)