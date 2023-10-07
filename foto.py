
#openai.api_key = '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'
import openai
import os
import json
from base64 import b64decode
import string
# Input prompt
prompt = input('The prompt: ')

# Set your OpenAI API key here
openai.api_key = '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'

# Generate image using OpenAI API
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='256x256',
    response_format='b64_json'
)

# Save API response data to a JSON file
with open('data.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

# Construct a valid file name from the prompt
# Remove any characters that are not valid in file names
valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
file_name = ''.join(c for c in prompt if c in valid_chars)

# Save the image with the valid file name
image_data = b64decode(response['data'][0]["b64_json"])
with open(f'{file_name}.png', 'wb') as file:
    file.write(image_data)

print(f'Image saved as {file_name}.png')
