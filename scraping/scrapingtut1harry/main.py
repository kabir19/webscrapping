import requests
from bs4 import BeautifulSoup

url ="https://codewithharry.com" 

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content

#print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)
 
# Step 3: HTML Tree traversal 

# Commonly used types of objects:
# print(type(title))          #1. Tag
# print(type(title.string))   #2. NavigableString
# print(type(soup))           #3. BeautifulSoup
                            #4. Comment

#markup = "<p><!-- This is a comment --></p>"
#soup2 = BeautifulSoup(markup)
#print(type(soup2.p.string))



title = soup.title


# Get all the paragraph from the page
paras = soup.find_all('p')
# print(paras)


# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# print(anchors)

# Get all the links in the HTML page
for link in anchors:
    if (link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link) 
        #print(linkText)




# Get first element in the HTML page
#print(soup.find('p')['class'])  


# Get classes of any element in the HTML page
#print(soup.find('p')['class'])  


# find all the element with class lead

# print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())  


navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are availble as a list
# .children - A tag's children are available as a generator

#for elem in navbarSupportedContent.children :
#    print(elem)

#for item in navbarSupportedContent.strings:
#    print(item)

#for item in navbarSupportedContent.stripped_strings:
#    print(item)


# print(navbarSupportedContent.parent)

#for item in navbarSupportedContent.parents:
#    print(item.name)

#print(navbarSupportedContent.next_sibling.next_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('.modal_footer')
print(elem)