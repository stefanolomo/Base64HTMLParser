import base64
import re
import os

def convert_html_image_to_base64(html_file):
  # Read the HTML file
  with open(html_file, 'r') as f:
    html = f.read()

  # Find all image tags using a regular expression
  image_tags = re.findall(r'<img .*?>', html)

  # Get the directory of the HTML file
  html_dir = os.path.dirname(html_file)

  # Iterate over each image tag
  for image_tag in image_tags:
    # Extract the src attribute using a regular expression
    src_match = re.search(r'src="(.*?)"', image_tag)
    if src_match:
      # Construct the full path to the image file
      image_file = os.path.join(html_dir, src_match.group(1))

      # Read the image file and convert it to base64 encoding
      with open(image_file, 'rb') as f:
        image_data = f.read()
      base64_image = base64.b64encode(image_data).decode('utf-8')

      # Replace the src attribute with the base64 encoded image
      image_tag_new = image_tag.replace(f'src="{src_match.group(1)}"', f'src="data:image/jpg;base64,{base64_image}"')

      # Replace the original image tag with the modified image tag
      html = html.replace(image_tag, image_tag_new)

  # Write the modified HTML back to the same file
  with open(html_file, 'w') as f:
    f.write(html)

# Test the function
html_file = input('Enter the path to the HTML file: ')
convert_html_image_to_base64(html_file)
