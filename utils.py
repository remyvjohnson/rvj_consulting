print("utils.py loaded!")

import glob
import os
from jinja2 import Template

# loop through content files and create a list
content_files = []
for content_file in glob.glob("content/*.html"): 
    content_files.append(content_file)
# print(content_files)

#loop through content_file list and extract from file path
content_pages = []
for file in content_files:
    file_name = os.path.basename(file)
    name_only, extension = os.path.splitext(file_name)
    # print(file_name)
    # print(name_only)
    
    # create content_pages list
    content_pages.append({
    "filename": file_name,
    "input_filename": "content/"+file_name,
    "title": name_only,
    "output_filename": "docs/"+ file_name,
    })
# print(content_pages)

# loop through content_pages list and move html into variable
for page in content_pages:
    content_html = open(page['input_filename']).read()
    
    # move base file into variable and assign to template
    template_html = open("templates/base.html").read()
    template = Template(template_html)
    
        
    # render template and sub in title and content
    final_html = template.render(
        title = name_only,
        content=content_html,
        content_pages = content_pages,
        filename = file_name
    )
    
    #write final docs files
    open(page['output_filename'], 'w+').write(final_html)
    # print(page['output_filename'])
# print('Doc Creation Complete!')
