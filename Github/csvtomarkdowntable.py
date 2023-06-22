import csv

def csv_to_markdown(csv_file):
    table = []
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            table.append(row)
    
    markdown = ''
    
    # Generating the header row
    markdown += '| ' + ' | '.join(table[0]) + ' |\n'
    markdown += '| ' + ' | '.join(['---'] * len(table[0])) + ' |\n'
    
    # Generating the data rows
    for row in table[1:]:
        markdown += '| ' + ' | '.join(row) + ' |\n'
    
    return markdown

# Example usage
csv_file_path = 'cloud.csv'  # Replace with the path to your CSV file
markdown_table = csv_to_markdown(csv_file_path)

output_file_path = 'output.md'  # Replace with the desired output file path
with open(output_file_path, 'w') as output_file:
    output_file.write(markdown_table)

print(f"Markdown table has been written to '{output_file_path}'")
