import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data(filepath):
    """
    Load the medical data from a CSV file and return a DataFrame.
    """
    return pd.read_csv(filepath)

# Preprocess data
def preprocess_data(df):
    """
    Preprocess the medical data for analysis and visualization.
    """
    # Example preprocessing steps
    df['BMI'] = df['weight'] / (df['height'] / 100) ** 2  # Calculate BMI
    df['high_cholesterol'] = df['cholesterol'] > 200      # Flag high cholesterol
    df['hypertension'] = df['blood_pressure'] > 140       # Flag hypertension
    return df

# Visualization functions
def plot_age_distribution(df):
    """
    Plot the age distribution of the patients.
    """
    plt.figure(figsize=(10, 5))
    sns.histplot(df['age'], bins=30, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

def plot_bmi_vs_cholesterol(df):
    """
    Plot BMI vs. cholesterol levels, highlighting high cholesterol.
    """
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x='BMI', y='cholesterol', hue='high_cholesterol', data=df)
    plt.title('BMI vs. Cholesterol')
    plt.xlabel('BMI')
    plt.ylabel('Cholesterol')
    plt.show()

def plot_blood_pressure_distribution(df):
    """
    Plot the distribution of blood pressure, highlighting hypertension cases.
    """
    plt.figure(figsize=(10, 5))
    sns.histplot(df['blood_pressure'], bins=30, kde=True, color='skyblue')
    plt.axvline(140, color='red', linestyle='--')
    plt.title('Blood Pressure Distribution')
    plt.xlabel('Blood Pressure')
    plt.ylabel('Frequency')
    plt.show()

# Main function
if __name__ == "__main__":
    # Load and preprocess data
    df = load_data('medical_data.csv')
    df = preprocess_data(df)

    # Visualize data
    plot_age_distribution(df)
    plot_bmi_vs_cholesterol(df)
    plot_blood_pressure_distribution(df)
