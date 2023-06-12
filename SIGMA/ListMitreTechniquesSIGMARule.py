# use this script to list all mitre techniques and tactics for each sigma file in the current directory.
import os
import yaml

def read_yaml_files(directory, key_tag):
    # Get all YAML files in the directory
    for filename in os.listdir(directory):
            if filename.endswith('.yml'):
        # Read and process each YAML file
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r') as file:
                    try:
                        data = yaml.safe_load(file)
                        if key_tag in data:
                            value = data[key_tag]
                            print(f"{filename}: {value}")
                    except yaml.YAMLError as e:
                        print(f"Error reading {filename}: {e}")

# Example usage
directory = '.'  # Replace with your directory path
key_tag = 'tags'  # Replace with your key tag

read_yaml_files(directory, key_tag)