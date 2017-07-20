import re

#Reading file content and extract it 
file = open("urlsemail.txt", "r")
content = file.read()

#Code to extract the urls from content
urlPattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
urls = re.findall(urlPattern, content)
print(urls)
print("First URL: " , urls[0])

#Code to extract the email address from content
emailPattern = r'\b[\w.-]+?@\w+?\.\w+?\b'
emails = re.findall(emailPattern, content)
print(emails)
print("First Email: " + emails[0])

#By using search and group function
match = re.search(urlPattern, content)
print(match.group())

file.close()
