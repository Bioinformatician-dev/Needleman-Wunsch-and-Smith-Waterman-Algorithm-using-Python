from Bio import SeqIO
import os
from collections import defaultdict


def count_features_in_genbank_files(directory):
    feature_counts = defaultdict(lambda: defaultdict(int))

    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.gb') or filename.endswith('.gbk'):
            file_path = os.path.join(directory, filename)
            # Parse the GenBank file
            with open(file_path, 'r') as file:
                for record in SeqIO.parse(file, 'genbank'):
                    # Count features
                    for feature in record.features:
                        feature_type = feature.type
                        feature_counts[filename][feature_type] += 1

    return feature_counts


# Example usage
if __name__ == "__main__":
    directory_path = 'path/to/genbank/files'  # Replace with your directory path
    counts = count_features_in_genbank_files(directory_path)

    # Print the feature counts
    for file, features in counts.items():
        print(f"Feature counts for {file}:")
        for feature_type, count in features.items():
            print(f"  {feature_type}: {count}")
