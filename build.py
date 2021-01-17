print("Build.py Starting!")

import glob
import os

#loop through content files and create a list
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
print('-Content Page List Successfully Created-')

# Template Function - pulls in base.html and updates the title
def templates(content_page):
    template = open('templates/base.html').read()
    updated_title_template = template.replace("{{title}}", content_page['title'])
    return updated_title_template

#File Combination Function - reads content pages, embeds the content into the base file, and creates a combined file
def file_combination(content_page, updated_title_template):
    file_content = open(content_page['input_filename']).read()
    combined_file = updated_title_template.replace("{{content}}", file_content)
    open(content_page['output_filename'], 'w+').write(combined_file)

#loops through content_pages and creates output (doc) files
def main():
    for content_page in content_pages:
        updated_title_template = templates(content_page)
        file_combination(content_page, updated_title_template)
    print('-Doc Files Successfully Created-')
    print('Build.py Complete!')
main()