# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Load the SMS Spam Collection dataset (Ensure you replace the path with your actual file path)
# Assuming you saved the dataset as 'SMSSpamCollection.csv'
df = pd.read_csv('SMSSpamCollection.csv', delimiter='\t', header=None, names=['label', 'text'])

# Display first few rows of the dataset to understand the structure
print(df.head())

# Step 1: Data Preprocessing (optional)
# Convert the labels (ham/spam) to binary values (1 for spam, 0 for ham)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Step 2: Text Vectorization (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)  # limit to 5000 features

# Convert the text column to numerical vectors using TF-IDF
X = vectorizer.fit_transform(df['text'])

# The labels (0 for ham, 1 for spam) are our target variable
y = df['label']

# Step 3: Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train a Naive Bayes Model
nb_model = MultinomialNB()

# Train the model on the training data
nb_model.fit(X_train, y_train)

# Step 5: Make Predictions
y_pred = nb_model.predict(X_test)

# Step 6: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy Score: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Optional: Show some predictions
sample_data = X_test[:5]  # Display predictions for the first 5 test samples
sample_pred = nb_model.predict(sample_data)
sample_texts = vectorizer.inverse_transform(sample_data)

print("\nSample Text Predictions:")
for text, pred in zip(sample_texts, sample_pred):
    print(f"Text: {' '.join(text)} => Predicted Label: {'Spam' if pred == 1 else 'Ham'}")
