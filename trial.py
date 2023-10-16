import pandas as pd
from faker import Faker
import random

# Initialize a Faker generator
fake = Faker()

# Define categories
categories = ['Spam', 'Ham', 'OTP', 'Social']

# Generate data for each category
def generate_email_data(category, num_samples=1500):
    data = []
    for _ in range(num_samples):
        email_data = {
            "Subject": fake.sentence(),
            "Email_Body": fake.text(),
            "Category": category,
        }
        data.append(email_data)
    return data

# Number of rows per category
rows_per_category = 1500

# Create a dataset
dataset = []

# Generate data for each category
for category in categories:
    dataset.extend(generate_email_data(category, rows_per_category))

# Convert the dataset to a pandas DataFrame
df = pd.DataFrame(dataset)

# Shuffle the dataset
df = df.sample(frac=1).reset_index(drop=True)

# If you want to save the DataFrame as a CSV file, you can do so
df.to_csv('email_data.csv', index=False)

# Display the DataFrame
print(df)
