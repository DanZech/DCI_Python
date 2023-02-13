'''
Task 1
Define a global variable named settings as a dictionary with a key title that contains a string of your choice, then create a function named change_site_title that takes one argument of type String and assigns it to the key title in the global variable settings.

Use this test case:

print(settings)
change_site_title("A new fancy title")
print(settings)

Your result should look like this:
'''

settings = {'title':'rio de janeiro'}
#book_dict['title'] = 'livro1'
#print(book_dict)

#book_dict['title'] = 'livro2'
#print(book_dict)

#{'title': 'My original title'}
#{'title': 'A new fancy title'}

#print(list(book_dict.values()))


def change_site_title(new_title):
  settings['title'] = new_title
  return settings

print(change_site_title("A new fancy title"))
print(change_site_title("A new fancy title2"))
print(change_site_title("A new fancy title3"))

def change_dict(new_field, new_value):
  settings[new_field] = new_value
  return settings

print(change_dict('endereco', 'Copacabana'))
print(change_dict('idade', '30'))

'''
Task 2
Keep the previous code and define now a global variable named default_settings as a dictionary with a key title, then create a function named get_title that takes one argument as a dictionary that defaults to default_settings and returns the content of the key title in the given dictionary.

Use this test case:

print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())

Your result should look like this:

My original title
My original title
A new fancy title
My original title
'''

default_settings = {'title': 'Rio de Janeiro'}

def get_title(settings):
  return settings['title']

print( get_title(default_settings) )


'''
Task 3: Default and non default arguments combined

Add a key pages to your previous settings and default_settings dictionaries.

Now, define two functions named get_pages and add_page. They will both have a parameter settings that will default to default_settings.

The function get_pages will simply return the list stored in the key pages of the given settings dictionary.

The function add_page will have an additional positional argument that will be the page as a dictionary. The function will append this argument to the pages key of the given settings dictionary.

Use this test case:

home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))

Your result should look like this:

[{'title': 'Home', 'path': '/'}]
[]
[{'title': 'Home', 'path': '/'}]
[{'title': 'About', 'path': '/about/'}]
'''

default_settings['page'] = 10

def add_page(settings, page_numer):
  settings['page'] = page_numer
  return settings

def get_page(settings):
  return settings['page']

print(default_settings)
add_page(default_settings, 20)
print(get_page(default_settings))