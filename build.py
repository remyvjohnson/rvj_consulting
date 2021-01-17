print("Yep, it's working")

# content_pages = [
#     {
#         'input_filename': 'content/index_content.html',
#         'output_filename': 'docs/index.html',
#         'title': 'RVJ. Retail Consulting: Home',
#     },
#     {
#         'input_filename': 'content/services_content.html',
#         'output_filename': 'docs/services.html',
#         'title': 'RVJ. Retail Consulting: Services',
#     },
#     {
#         'input_filename': 'content/about_content.html',
#         'output_filename': 'docs/about.html',
#         'title': 'RVJ. Retail Consulting: About Me',
#     },
#     {
#         'input_filename': 'content/contact_content.html',
#         'output_filename': 'docs/contact.html',
#         'title': 'RVJ. Retail Consulting: Contact Me',
#     },
# ]

import glob
import os

#loop through content files and create a list
content_files = []
for content_file in glob.glob("content/*.html"): 
    content_files.append(content_file)
    # print(content_files)
    print('-PT1 COMPLETE-')

    #extract info from file path names
    all_files = content_files
    i = 0
    content_pages = []
    for all_file in all_files:  
        file_path = all_files[i]
        file_name = os.path.basename(file_path)
        print(file_name)
        name_only, extension = os.path.splitext(file_name)
        print(name_only)
        print('-PT2 COMPLETE-')
        i += 1


        
        # for content_file in content_files:
        content_pages.append({
        "input_filename": "content/"+ file_name,
        "title": name_only,
        "output_filename": "docs/"+ file_name,
        })
        print(content_pages)
        print('-THE END!-')
    




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

def main():
    for content_page in content_pages:
        updated_title_template = templates(content_page)
        file_combination(content_page, updated_title_template)
        print(content_page['title'],'page complete!')

main()