# Day: 95(Regular Expressions)

import re

''' Regular Expressions or 'regex' for short are a powerful tool for working with strings and text data
    in python, they allow you to match  and manipulate strings based on patterns, making it easier to 
    peform complex string operations with just feq lines of code'''


pattern=r"Bishop"
content='''Mandell Creighton (1843_1901) was a British historian and clergyman. He studied at the University
of Oxford, then became a don in 1866. He was appointed the first occupant of the Dixie Chair of Ecclesiastical
History at the University of Cambridge in 1884. The following year, he also was engaged as the founding editor
of The English Historical Review, the first English-language academic journal in its field. In these posts, he
helped to establish history as an independent academic discipline in England. Creighton was a parish priest of
the Church of England who rose to be Bishop of London from 1897 and, but for his death, was thought likely
to become Archbishop of Canterbury. His moderation and practicality drew praise from Queen Victoria'''

match=re.search(pattern,content)            # Searches for the first occurence of that word
print(match)

matches=re.finditer(pattern,content)
print(matches)

''' A big vast topic, which has ALOT of meta characters so read its documentation which will help alot in
complex calculation, so look into it. A site for practicing them is RegExr.com so do check it out '''