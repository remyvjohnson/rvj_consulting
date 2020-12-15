print("Yep, it's working")

#assign variables for the templates
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

#assign content to variable, combine and put in new file
content = open('content/index_content.html').read()

index_html = top_template + content + bottom_template
open('docs/index.html', 'w+').write(index_html)

# Repeat for Services file
content = open('content/services_content.html').read()

services_html = top_template + content + bottom_template
open('docs/services.html', 'w+').write(services_html)

# Repeat for About file
content = open('content/about_content.html').read()

about_html = top_template + content + bottom_template
open('docs/about.html', 'w+').write(about_html)

# Repeat for Contact file
content = open('content/contact_content.html').read()

contact_html = top_template + content + bottom_template
open('docs/contact.html', 'w+').write(contact_html)