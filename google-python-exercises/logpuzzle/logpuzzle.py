#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import requests

# Use for testing file in atom.
# Comment out if running from cmd.
# print(os.getcwd())
os.chdir(os.getcwd() + r'\google-python-exercises\logpuzzle')

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    underscore_index = filename.find('_')
    hostname = filename[underscore_index + 1:]
    with open(filename, 'r') as f:
        content = f.read()
    urls = re.findall(
        r'GET (\S+/puzzle\S+(?:\-\w+)+\.jpg)', content)
    urls = set(urls)

    def puzzle_key(url):
        match = re.search(r'puzzle(\S+(?:\-\w+)+)\.jpg', url)
        key = match.group(1)
        return key
    urls = sorted(urls, key=puzzle_key)
    full_urls = ['http://' + hostname + url for url in urls]
    return full_urls


print(read_urls('animal_code.google.com'))


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    index_path = os.path.join(dest_dir, 'index.html')
    with open(index_path, 'w') as f:
        f.write(r'<html><body>\n')
        i = 0
        for url in img_urls:
            r = requests.get(url, stream=True)
            file_path = os.path.join(dest_dir, 'img' + i + '.jpg')
            with open(file_path, 'wb') as f2:
                for chunk in r:
                    f2.write(chunk)
            i += 1
        f.write(r'</body></html>')


download_images('https://raw.githubusercontent.com/persocom01/TestPython/master/Innocence.jpg',
                os.path.join(os.getcwd() + r'\google-python-exercises\logpuzzle'))


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
