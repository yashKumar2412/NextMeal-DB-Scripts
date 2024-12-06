import json

input_file = 'reviews.json'
output_file = 'sample_' + input_file

sample_count = 199999

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    records = []
    
    for i, line in enumerate(f_in):
        item = json.loads(line)
        records.append(item)
        
        if i == sample_count:
            break
    
    json.dump(records, f_out, indent=4)