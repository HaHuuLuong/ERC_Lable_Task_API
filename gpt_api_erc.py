import os
import openai
import time
import re
import csv
openai.api_key = "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"

# read input file
# data = open("./result_regex.txt", encoding="utf-8").read().splitlines()

prompt = """Label each sentence in the following dialogue with one of the labels: [joy],[excited],[sadness],[anger],[surprise],[fear],[frustration],[disgust],[neutral]
Output format: prompt, label"""

# for item in data:
#     prompt += f"\n- {item}"

with open("3_content.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if i == len(lines):
            prompt +=f'\n{i} - {line.strip()}.'
        else:
            prompt +=f'\n{i} - {line.strip()}'

def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.2,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["Human:", " AI:"]
    )

    return response.choices[0].text

a = time.time()
ans = openai_create(prompt)
b = time.time()
print(f"Request time: {b - a}")  # print request time

print(ans)

with open("3_content_lable.txt", "w", encoding="utf-8" ) as f:
    f.write(ans)

# with open('result_ERC.txt', 'r', encoding="utf-8") as f:
#     # Read all lines into a list
#     lines = f.readlines()


# # Initialize an empty list to store the extracted fields
# fields = []

# # Loop through each line in the list of lines
# for line in lines:
#     # Use regex to extract the fields from each line
#     match = re.search(r'(\d+) - \[(.*)-(\d+)\] \((.*)\): (.*),(.*)', line) #:(.*)\,(.*)
#     if match:
#         # Extract the fields from the regex match object
#         utterance_id = match.group(1)
#         speaker = match.group(2)
#         id_speaker = match.group(3)
#         datetime = match.group(4)
#         utterance = match.group(5)
#         emotion=match.group(6)
#         fields.append({
#             'Utterance': utterance,
#             'Speaker': speaker,
#             'Id_speaker': id_speaker,
#             'Emotion': emotion,
#             'Utterance_id': utterance_id,
#             'Date': datetime.split()[0],
#             'Time': datetime.split()[1]
#         })

# # Open a CSV file for writing
# with open('example_ERC.csv', 'w', newline='', encoding="utf-8") as f:
#     # Create a CSV writer object
#     writer = csv.DictWriter(f, fieldnames=fields[0].keys())

#     # Write the header row to the CSV file
#     writer.writeheader()

#     # Loop through each field dictionary in the list of fields
#     for field in fields:
#         # Write the field dictionary as a row to the CSV file
#         writer.writerow(field)


