# AI Links

The file [links.txt](links.txt) is a list of web links that we recommended, back in the early 2000s. We are no longer maintaining this list, but have put it here for anyone to use as they see fit.  

# Format

Each line in [links.txt](links.txt) has the format: *Title*`*` *url* *topics*.*genre* *comment*  &nbsp; For example,

    Agents Web (UMBC)*  http://agents.umbc.edu intro,agents.edu Great site for agent news and software.
     
is a line whose fields are as follows:

     title   = 'Agents Web (UMBC)'
     star    = True
     url     = 'http://agents.umbc.edu'
     topics  = {'intro', 'agents'}
     genre   = 'edu'
     comment = 'Great site for agent news and software.'

The `*` character at the end of the title is optional; if present it means that the link is *highly recommended*. The `title` ends where the `url` begins; a url starts with `http:`, `https:`, `ftp:`, or `mailto:` (so those strings can't occur in a title). The `url` ends with whitespace, then we have one or more comma-separated topics followed by a `.` and exactly one `genre`. Everything after that is the `comment`. We supply [code](parse.py) to parse this format. The topics and genres are as follows:

|TOPIC|Description| |GENRE|Description|
|-----|-----------|-|-----|-----------|
intro	| Overview of AI||ref|reference
agents| Intelligent Agents||list    | Lists of Links
search| Search and Game Playing||jour	| Journals
logic	| Logic and Knowledge Representation||people	| People
planning	| Planning||com	| Companies
uncertainty	| Reasoning with Uncertainty||news	| News &amp; Mail lists
learning	| Machine Learning||soft| Software
nlp	| Natural Language Processing||edu	| University Research Groups
robotics	| Perception and Robotics||org	| Nonprofit Organizations
phil	| Philosophy and the Future||humor	| Humor
lisp	| AI Programming (Lisp)
python| AI Programming (Python)
prolog| AI Programming (Prolog)
java	| AI Programming (Java, etc.)



