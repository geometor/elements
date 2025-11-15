we are making great progress - but I want to take a step back and refine our process - lets create a cli in the pyproject to just run the transformation from the root of the project instead of @generate_rsts.py

I also want to go back to the full xml files for each book 

@resources/xml/books 

I want to walk the hierarchy of the xml and create our rst files as we go

each book gets a folder and an index.rst

there is a clear hierarchy: div2 > div3 > div4

div2 represents a grouping of entry types like propositions - these do not get a file or folder

div3 represents an entry in the book - this gets a folder with an index.rst

div4 is handled in the content - but may contain ids - like porisms

each entry will get an :order: field representing the order in the book and a :number: field representing the count of this item across all 13 books

I also want to get consistent in how we reference items - returning to Heath's roman numeral and sub numbers 

so the first book title is `I` and is also the folder name - the title of an entry in a book and a reference tag follows: `I.47` `V.def.1` but the folder for the entry is just the subnumber: `47` `def.1` - this will create a concise url that is easy to predict `I/47` `V/def.1`
