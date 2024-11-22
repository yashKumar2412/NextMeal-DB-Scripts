import json

input_file = 'users.json'
output_file = 'sample_' + input_file

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Create a list to store the first 100 records
    records = []
    
    # Iterate over each line in the file (assuming each line is a valid JSON object)
    for i, line in enumerate(f_in):
        item = json.loads(line)  # Parse the JSON object from the line
        records.append(item)  # Add each item to the list
        
        if i == 9999:  # Stop after 10000 records
            break
    
    # Write the first 100 records as a JSON array into the output file
    json.dump(records, f_out, indent=4)