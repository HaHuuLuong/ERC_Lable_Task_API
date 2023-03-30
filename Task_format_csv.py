# import os
# import re
# import csv

# # input_dir = 'ERC_TASK'
# output_file = 'output.csv'
# fields = []
# with open(output_file, 'w', newline='', encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(['Utterance', 'Speaker', 'Id_speaker', 'Emotion', 'Utterance_id', 'Date', 'Time'])
#     for filename in ['1_content_lable.txt', '2_content_lable.txt', '3_content_lable.txt']:
#         with open( filename, 'r', encoding="utf-8") as f:
#             lines = f.readlines()
        
#         for line in lines:
#             match = re.search(r'(\d+) - \[(.*)-(\d+)\] \((.*)\): (.*),(.*)', line) #:(.*)\,(.*)
#             if match:
#                 # Extract the fields from the regex match object
#                 utterance_id = match.group(1)
#                 speaker = match.group(2)
#                 id_speaker = match.group(3)
#                 datetime = match.group(4)
#                 utterance = match.group(5)
#                 emotion=match.group(6)
#                 fields.append({
#                     'Utterance': utterance,
#                     'Speaker': speaker,
#                     'Id_speaker': id_speaker,
#                     'Emotion': emotion,
#                     'Utterance_id': utterance_id,
#                     'Date': datetime.split()[0],
#                     'Time': datetime.split()[1]
#                 })
#         for field in fields:
#         # Write the field dictionary as a row to the CSV file
#             writer.writerow(field)
#             # match = re.search(r'(\d+)\s-\s\[(.*)-(\d+)\]\s\((.*)\):\s(.*)\s?(.*)?', line)
#             # if match:
#             #     writer.writerow([match.group(5), match.group(2), match.group(3), match.group(4), match.group(1), match.group(6), match.group(7)])


import os
import re
import csv
import glob
input_dir = 'C:\\Users\\LENOVO\\Desktop\\crawl_data\\ChatGPT_API\\ERC_TASK'
output_file = 'output.csv'

with open(output_file, 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Utterance', 'Speaker', 'Id_speaker', 'Emotion', 'Utterance_id', 'Date', 'Time'])
    # for filename in ['1_content_lable.txt', '2_content_lable.txt', '3_content_lable.txt']:
    for filename in glob.glob('*_content_lable.txt'):

        filepath = os.path.join(input_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding="utf-8") as f:
                lines = f.readlines()
            for line in lines:
                # match = re.search(r'(\d+)\s-\s\[(.*)-(\d+)\]\s\((.*)\):\s(.*)\s?(.*)?', line)
                match = re.search(r'(\d+) - \[(.*)-(\d+)\] \((.*)\): (.*),(.*)', line) #:(.*)\,(.*)

                if match:
                    writer.writerow([match.group(5), match.group(2), match.group(3), match.group(6), match.group(1), match.group(4).split()[0],match.group(4).split()[1]])
        else:
            print(f"File {filepath} does not exist.")