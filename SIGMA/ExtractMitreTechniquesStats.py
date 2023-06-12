# This script can be put in a directory with SIGMA rules. The script will output statistics on the mitre techniques and tactics that are present in an output file named: mitre_statistics.txt
# List will be done both on current directory as well as child directories.
import os
import yaml
from collections import Counter

def count_tag_values_in_yaml_files(directory, key_tag):
    tag_values = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.yml'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as file:
                    try:
                        data = yaml.safe_load(file)
                        if key_tag in data:
                            value = data[key_tag]
                            tag_values.extend(value)
                    except yaml.YAMLError as e:
                        print(f"Error reading {filename}: {e}")

    tag_counts = Counter(tag_values)
    return tag_counts

# Example usage
directory = '.'  # Replace with your directory path
key_tag = 'tags'  # Replace with your key tag
output_file = 'mitre_statistics.txt'  # Specify the output file path

tag_counts = count_tag_values_in_yaml_files(directory, key_tag)

# Write the tag statistics to a file
with open(output_file, 'w') as file:
    file.write("Tag Statistics:\n")
    for tag, count in tag_counts.items():
        file.write(f"{tag}: {count}\n")

print(f"Tag statistics saved in {output_file}.")