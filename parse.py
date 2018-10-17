"""
Code to parse AIMA file of links, such as `old-links.txt`.
"""

import collections
import re

Link   = collections.namedtuple('Link', 'title, star, url, topics, genre, comment')
REGEX  = re.compile(r"([^*]+?)([*]?)\s+((http|mailto|ftp):[^\s]+)\s+([a-z,]+)[.]([a-z,]+)\s*(.*)$")
TOPICS = {'agents', 'intro', 'java', 'learning', 'lisp', 'logic', 'nlp', 'phil', 'planning',
          'prolog', 'python', 'robotics', 'search', 'uncertainty'}
GENRES = {'com', 'edu', 'humor', 'jour', 'list', 'news', 'org', 'people', 'ref', 'soft'}

def parse_link(line):
    "Parse a line of text into a `Link` structure."
    m = REGEX.match(line)
    assert m, 'Line does not match: ' + line
    title, star, url, _, topics, genre, comment = m.groups()
    topics = set(topics.split(','))
    assert genre in GENRES, 'Unknown genre: ' + genre
    assert not (topics - TOPICS), 'Unknown topics: ' + str(topics - TOPICS)
    return Link(title, star == '*', url, topics, genre, comment)

def parse_file(filename='old-links.txt'):
    "Parse a file into a list of Links."
    return [parse_link(line) for line in open(filename)]
