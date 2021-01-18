print("Build.py Starting!")

import glob
import os
from jinja2 import Template

# loop through content files and create a list
content_files = []
for content_file in glob.glob("content/*.html"): 
    content_files.append(content_file)
    # print(content_files)

    #make content_files list available, loop through list, extract from file path
    all_files = content_files
    i = 0
    content_pages = []
    for all_file in all_files:  
        file_path = all_files[i]
        file_name = os.path.basename(file_path)
        # print(file_name)
        name_only, extension = os.path.splitext(file_name)
        # print(name_only)
        i += 1
        
        # create content_pages list
        content_pages.append({
        "input_filename": "content/"+file_name,
        "title": name_only,
        "output_filename": "docs/"+ file_name,
        })
        # print(content_pages)
# print('-Content Page List Successfully Created-')

        # move contents file into variable
        content_html = open("content/"+file_name).read()

        # move base file into variable and assign to template
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        
        # render template and sub in title and content
        final_html = template.render(
            title= name_only,
            content=content_html,
        )

        # write final docs file
        open('docs/'+ file_name, 'w+').write(final_html)

print('Build.py Complete!')

