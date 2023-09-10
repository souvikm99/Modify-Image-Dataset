import os
import chardet

# Sample dictionary for replacement
replacement_dict = {
    'Tomato' : '0',
    'Apple' : '1',
    'Grape' : '2',
    'Banana' : '3',
    'Watermelon' : '4',
    'Mango' : '5',
    'Carrot' : '6',
    'Cucumber' : '7',
    'Pineapple' : '8',
    'Orange' : '9',
    'Broccoli' : '10',
    'Lemon' : '11',
    'Strawberry' : '12'
    # Add more key-value pairs as needed
}

# Specify the path to the input folder containing text files
input_folder_path = '/Users/souvikmallick/Desktop/CC_New_Dataset_GoogleOI/ValidationData/Label'

# Specify the path to the output folder
output_folder_path = '/Users/souvikmallick/Desktop/CC_New_Dataset_GoogleOI/ValidationData/changedLabels'

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Get a list of all files in the input folder
files = os.listdir(input_folder_path)

# Process each file in the input folder
for file_name in files:
    input_file_path = os.path.join(input_folder_path, file_name)
    output_file_path = os.path.join(output_folder_path, file_name)

    # Detect the encoding of the input file
    with open(input_file_path, 'rb') as input_file:
        encoding = chardet.detect(input_file.read())['encoding']

    # Read the input file with the detected encoding
    with open(input_file_path, 'r', encoding=encoding) as input_file:
        lines = input_file.readlines()

    # Process each line and replace keys from the dictionary with their corresponding values
    modified_lines = []
    for line in lines:
        for key, value in replacement_dict.items():
            line = line.replace(key, value)
        modified_lines.append(line.strip())

    # Save the modified lines to the output file with the same name as the original file
    with open(output_file_path, 'w', encoding=encoding) as output_file:
        output_file.write('\n'.join(modified_lines))
