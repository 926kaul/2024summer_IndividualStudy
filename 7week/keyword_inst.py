import os
import json

# Load the data from the JSON file
with open('7week/fixed_data.json', 'r') as json_file:
    gpts = json.load(json_file)

# Keywords to search for
keywords = ["account", "malicious", "ID", "password", "send", "request", ".com", "http", "ignore", "post", "token", "action", "API", "regardless", "server", "append", "ad", "change"]

# Create a dictionary to hold results
result = {key: [] for key in keywords}

# Iterate through each entry in the loaded JSON data
for gpt_lst in gpts.values():
    for gpt in gpt_lst:
        try:
            content = gpt["instructions"]
            name = gpt["name"]

            # Check each keyword and process files accordingly
            for keyword in keywords:
                if keyword in content:
                    # Create directory if it does not exist
                    dst_dir = f"C:/MyCode/7week/inspections/{keyword}/"
                    if not os.path.exists(dst_dir):
                        os.makedirs(dst_dir)

                    # Define file path and write content
                    dst_file = os.path.join(dst_dir, f"{name}.txt")
                    with open(dst_file, 'w', encoding='utf-8') as file:
                        file.write(content)

        except Exception as e:
            print(f"Error occurred while processing the file: {e}")
