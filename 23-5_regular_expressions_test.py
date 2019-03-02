# Demonstrates use of the regular expression module.
# Due to the importance of this topic I gave it its own file.
import re
import pprint

text = '''
<header>
<div class="container">
<div class="row">
<div class="col-md-4">
<a class="bc_logo" href="https://www.bleepingcomputer.com/"><img src="https://www.bleepstatic.com/images/site/logo.png" width="287" height="24" alt="logo"></a>
</div>
<div class="col-md-8">
<ul class="bc_social_icons">
<li><a href="https://www.facebook.com/BleepingComputer"><span class="fa fa-facebook"></span></a></li>
<li><a href="https://twitter.com/BleepinComputer"><span class="fa fa-twitter"></span></a></li>
<li><a href="https://plus.google.com/+bleepingcomputer/posts/cat/dog/squirrel"><span class="fa fa-google-plus"></span></a></li>
<li><a href="https://www.youtube.com/user/BleepingComputer/"><span class="fa fa-youtube"></span></a></li>
</ul>
'''

# Matches beginnings of string.
if re.match('facebook', text):
    print('facebook present from beginning of string')
else:
    print('facebook absent from beginning of string')

# Matches first instance anywhere in string.
search = re.search('facebook', text)
if search:
    print(search.group())
    # Returns start position of match. Note that the first position is 0.
    print(search.start())
    print(search.end())
    print(search.span())
else:
    print('facebook absent')
print()

# Returns a list of strings of all matches. Explanation of re used below:
# ? = 0-1. + = 1+. * = 0+.
# \w means all letters. For other such shorthand use a re cheatsheet.
# \. the . and some special characters must be escaped.
# () denotes a capturing group. If used, findall will only return the contents
# of said group. (?:) is used to make it non capturing.
website_names = re.findall(
    r'https?://\w+\.\w+(?:\.\w+)?(?:/\+?\w+)*/?(?:\.\w+)?', text)
pprint.pprint(website_names)

# Demonstrates replacement searched string.
altered_text = re.sub('facebook', 'tastebook', text)
print(altered_text)
print()

# Possible to use /w* instead of [a-z]* here if you don't mind words with
# capitalized improperly.
# .group() is necessary here as search does not return a string.
# In this case, (o) was used to deliberately put o in group 1.
# There is no practical reason to do this in this case, but you can retrieve
# group 1 by using .group(1)
# word_containing_o = re.search(r'\b\w?[a-z]*(o)[a-z]*', text).group()
# words_containing_o = re.findall(r'\b\w?[a-z]*o[a-z]*', text)
# print(word_containing_o)
# print(words_containing_o)
# print()
