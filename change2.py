import os
import chardet
#1-redchilliS
#2-soya
#3-tomato
# Specify the path to the input folder containing text files
input_folder_path = '/Users/souvikmallick/Desktop/TEST/inpt'

# Specify the path to the output folder
output_folder_path = '/Users/souvikmallick/Desktop/TEST/res/'

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

    # Process each line and modify the first integer
    modified_lines = []
    for line in lines:
        parts = line.strip().split(' ')
        new_first_integer = 3  # Set the desired new first integer value here

        # Modify the first integer
        parts[0] = str(new_first_integer)

        # Join the modified line back into a string
        modified_line = ' '.join(parts)

        # Append the modified line to the list
        modified_lines.append(modified_line)

    # Save the modified lines to the output file with the same name as the original file
    with open(output_file_path, 'w', encoding=encoding) as output_file:
        output_file.write('\n'.join(modified_lines))
