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
# The r in front of a string makes it a raw string literal, which allows use of
# \ without escaping them unlike regular strings.
if re.match(r'facebook', text):
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

# Explanation of various re below:
# ^regex$ ^ and $ used this way are called anchors. They represent the start
# and end of a string. \b can be used instead for start of a word.
# ? = 0-1. + = 1+. * = 0+.
# \b = word boundary. Other common ones are \d number, \s whitespace, \w word.
# A capital \B means the opposite of \b.
# \. escapes .. Other characters needing escape are \+*?[]^$(){}=!<>|:-.
# () denotes a group. If used, findall will return the contents said group
# instead of the whole match.
# (?:) is used to make it a group non capturing.
# [a-z] specifies all the possible characters accepted.
# [^a-z] specifies all the possible characters rejected.
# {min,max} specifies the min, max number of repetitions of the previous char.
# re.I is known as a flag. re.I=ignore case. re.M=multiline.
# re.S = dotall. (makes . also match newline)
# The | divider is needed to pass multiple flags.
website_names = re.findall(
    r'\bhttps?://\w+\.\w+(?:\.\w+)?(?:/\+?\w+)*/?(?:\.[a-z]{2,4})?', text, re.I | re.M)
# Demonstrates use of negative lookahead to exclude www website names.
# (?!) is called negative lookahead. It looks ahead of itself to ensure that it
# is not behind the text in front of it.
# Replacing ! with = makes it positive. (?=) is positive lookahead.
# (?<=) is lookbehind.
non_www_website_names = re.findall(
    r'\bhttps?://(?!www)(?:\w+)\.\w+(?:\.\w+)?(?:/\+?\w+)*/?(?:\.[a-z]{2,4})?', text, re.I | re.M)
print('websites:')
pprint.pprint(website_names)
print('non-www websites:')
pprint.pprint(non_www_website_names)
print()

text = 'The quick brown fox jumps over the lazy dog.'

# Demonstrates use of [^o ] to excude o and blankspace characters.
words_without_o = re.findall(r'\b[^o ]+\b', text, re.I | re.M)
# Demonstrates use of the or divider |.
words_with_a_or_e = re.findall(r'\b(\w*a\w*|\w*e\w*)\b', text, re.I | re.M)
print('words without o:', words_without_o)
print('words with a or e:', words_with_a_or_e)
print()

# Demonstrates use of groups.
# (?P<name>) is a named group.
pattern = r'The (quick) brown fox (jumps (over)) the (?P<name>lazy) dog\.'
match = re.match(pattern, text)
# 4 groups total.
print(len(match.groups()))
# You can call each group individually using match.group(1).
# 1 can be a name if named groups were used.
for group in match.groups():
    print(group)
# Demonstrates replacement of searched string as well as group indicators
# \1 and \g<name> specifically.
# re.sub replaces all instances of the pattern.
replacement = r'The \g<name> brown fox jumps over the \1 dog.'
altered_text = re.sub(
    pattern, replacement, text)
print(altered_text)
print()
