print("Yep, it's working")

#assign variables for the templates
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

#assign content to variable, combine and put in new file
content = open('content/index_content.html').read()

index_html = top_template + content + bottom_template
open('docs/index.html', 'w+').write(index_html)

