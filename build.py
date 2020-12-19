print("Yep, it's working")

content_pages = [
    {
        'input_filename': 'content/index_content.html',
        'output_filename': 'docs/index.html',
        'title': 'RVJ. Retail Consulting: Home',
    },
    {
        'input_filename': 'content/services_content.html',
        'output_filename': 'docs/services.html',
        'title': 'RVJ. Retail Consulting: Services',
    },
    {
        'input_filename': 'content/about_content.html',
        'output_filename': 'docs/about.html',
        'title': 'RVJ. Retail Consulting: About Me',
    },
    {
        'input_filename': 'content/contact_content.html',
        'output_filename': 'docs/contact.html',
        'title': 'RVJ. Retail Consulting: Contact Me',
    },
]

#Template Function - pulls in base.html and updates the title
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