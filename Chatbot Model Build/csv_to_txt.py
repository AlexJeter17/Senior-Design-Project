import pandas as pd

# Path to the CSV file
csv_file_path = 'Training Data CSV\SocialMediaUsersDataset.csv'
# Output text file path
output_text_file_path = 'input_training.txt'

# Load the dataset
df = pd.read_csv(csv_file_path)

# Assuming you want to convert the entire DataFrame to a text file
# Here, we're converting it to a tab-separated values file without headers or indices
df.to_csv(output_text_file_path, index=False, header=None, sep='\t')

print(f"Data has been written to {output_text_file_path}")
