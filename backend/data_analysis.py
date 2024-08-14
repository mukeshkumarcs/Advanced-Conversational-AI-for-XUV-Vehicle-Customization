import pandas as pd
import matplotlib.pyplot as plt

def generate_feature_popularity_report():
    df = pd.read_csv('user_interactions.csv')
    feature_counts = df['selected_feature'].value_counts()

    plt.figure(figsize=(10, 6))
    feature_counts.plot(kind='bar')
    plt.title('Popularity of XUV Features')
    plt.xlabel('Feature')
    plt.ylabel('Selection Count')
    plt.tight_layout()
    plt.savefig('feature_popularity.png')
