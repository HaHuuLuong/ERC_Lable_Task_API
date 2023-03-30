import re
import csv

import glob

for file_name in glob.glob('*_content_lable.txt'):
    with open(file_name,encoding="utf-8") as f:
        for line in f:
        #    lines = f.readlines()
           lines = line.split()

# for input_file in ['1_content_lable.txt','2_content_lable.txt','3_content_lable.txt']:
#     with open(input_file 'r', encoding="utf-8") as f:
#         # Read all lines into a list
#         lines = f.readlines()

# Initialize an empty list to store the extracted fields
fields = []

# Loop through each line in the list of lines
for line in lines:
    # Use regex to extract the fields from each line
    match = re.search(r'(\d+) - \[(.*)-(\d+)\] \((.*)\): (.*),(.*)', line) #:(.*)\,(.*)
    if match:
        # Extract the fields from the regex match object
        utterance_id = match.group(1)
        speaker = match.group(2)
        id_speaker = match.group(3)
        datetime = match.group(4)
        utterance = match.group(5)
        emotion=match.group(6)
        fields.append({
            'Utterance': utterance,
            'Speaker': speaker,
            'Id_speaker': id_speaker,
            'Emotion': emotion,
            'Utterance_id': utterance_id,
            'Date': datetime.split()[0],
            'Time': datetime.split()[1]
        })

# Open a CSV file for writing
with open('example_ERC.csv', 'w', newline='', encoding="utf-8") as f:
    # Create a CSV writer object
    writer = csv.DictWriter(f, fieldnames=fields[0].keys())

    # Write the header row to the CSV file
    writer.writeheader()

    # Loop through each field dictionary in the list of fields
    for field in fields:
        # Write the field dictionary as a row to the CSV file
        writer.writerow(field)