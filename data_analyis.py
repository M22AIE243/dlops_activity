import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def encode_categorical(data):
    """Encode categorical column using one-hot encoding."""
    encoded_data = pd.get_dummies(data, columns=['Class'])
    return encoded_data



def analyze_data(data):
    """Perform basic data analysis."""
    if data is not None:

        data = encode_categorical(data)
        # Display summary statistics
        print("Summary Statistics:")
        print(data.describe())

        # Plot histograms for numeric columns
        print("Histograms:")
        for col in data.select_dtypes(include=['int', 'float']):
            data[col].plot(kind='hist', bins=10)
            plt.title(col)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        
        # Plot bar plot for the class label (string type)
        class_columns = [col for col in data.columns if 'Class_' in col]
        class_label_counts = data[class_columns].sum()
        class_label_counts.plot(kind='bar')
        plt.title('Class Label Distribution')
        plt.xlabel('Class Label')
        plt.ylabel('Count')
        plt.show()


def main():
    file_path = input("Enter the path to the CSV file: ")
    data = load_data(file_path)
    analyze_data(data)

if __name__ == "__main__":
    main()
