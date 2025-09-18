import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    df = load_data('data/Vodafone_Customer_Churn_Sample_Dataset.csv')
    print(df.head())