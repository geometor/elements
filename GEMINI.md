# Background

This project has been through a number of iterations over the years. Beginning
with the xml content, we produced all 13 books as Grav markdown files for each
element. And books 1 & 2 are fairly clean and well structured. But a lot of this work was done with macros in vim. 

Many scripts were written to do this parsing along the way - the code is
scattered around the repo. It was done piecemeal with little documentation. And we have found that the xml tags used in each book is slightly different.

Hovever, we want to get the whole thing into RST with our Sphinx customization.
This platform will provide tremendous capabilities for cross-linking refs,
glossaries, etc.


# Goals

The project will focus on the following:

- **Formalization**: Translating the text of Euclid's Elements into a more structured and machine-readable format. Semantically and symbolically consistent throughout.
- **Dependency Mapping**: Identifying the dependency chain between definitions, postulates, and propositions.
- **Content Transformation**: Converting the xml content from the `resources` folder into reStructuredText (RST) within a new `docsrc/elements2` directory. This will involve:
    -   Retitling propositions for clarity.
    -   Establishing a consistent categorization and linking system.
    -   Integrating with Sphinx for documentation generation.
- **Canonical Consistency** - links and labelling - predicable urls

I want to start over, from the xml element files, reparsing the xml directly
into what we need for RST. The books have been cleanly split into xml files for
each element. We can examine these and develop new translations scripts to
create the RST structure we are looking for.

But before we begin we need to document the process and design the system for
organization. In `docsrc/elements` I experimented with departing from numbered
indexes to phrases - which would be the key for refs and the url path. This is
tedious, however a reference like "Book3 prop11" or worse "III.11" is useless semantically.

# Current Status and Next Steps

The design for the new RST structure and XML parsing process is documented in :doc:`elements2/design`.
The next step is to develop the XML parsing script based on this design.
