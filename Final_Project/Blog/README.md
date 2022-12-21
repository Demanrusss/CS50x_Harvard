CS50 2022 Final Project "Blog"
=====================================

The tree of a project [here](https://github.com/Demanrusss/CS50x_Harvard/tree/main/Final_Project/Blog)

What is my Final Project about?
---------------------

## [Quoting From Wikipedia](https://en.wikipedia.org/wiki/Blog):
A blog (a truncation of "weblog") is a discussion or informational [website](https://en.wikipedia.org/wiki/Website) published on the [World Wide We](https://en.wikipedia.org/wiki/World_Wide_Web)
consisting of discrete, often informal diary-style text entries (posts). Posts are typically displayed in [reverse 
chronological order](https://en.wikipedia.org/wiki/Reverse_chronology) so that the most recent post appears first, at the top of the [web page](https://en.wikipedia.org/wiki/Web_page). Until 2009, blogs 
were usually the work of a single individual, occasionally of a small group, and often covered a single subject 
or topic. In the 2010s, "multi-author blogs" (MABs) emerged, featuring the writing of multiple authors and sometimes 
professionally [edited](https://en.wikipedia.org/wiki/Editing). MABs from [newspapers](https://en.wikipedia.org/wiki/Newspaper), other [media outlets](https://en.wikipedia.org/wiki/News_media), universities, [think tanks](https://en.wikipedia.org/wiki/Think_tank), [advocacy groups](https://en.wikipedia.org/wiki/Advocacy_group), 
and similar institutions account for an increasing quantity of blog [traffic](https://en.wikipedia.org/wiki/Web_traffic). The rise of [Twitter](https://en.wikipedia.org/wiki/Twitter) and other "[microblogging](https://en.wikipedia.org/wiki/Microblogging)" 
systems helps integrate MABs and single-author blogs into the news media.

There is nothing more to say except the fact that  it took a lot of time.

Maybe, further information about Blog will be added a little bit later. It depends on new features that might be 
developed and implemented to the project.

License
-------

Blog is released under the terms of my own free license. Thus you can share it without any payment or punishment

Development Process
-------------------

The `master` branch has been built and tested, but it is not guaranteed to be
completely stable. The main problem is under configuration file and .env-file that you have to create by yourself.
More information about installing please see below.

As you could see from the tree and some specific files in main folder, this whole project was developed by Microsoft
Visual Studio, in particularly version 2022. 
The stack of technologies are follows:
Python with libraries: Jinja2, WTForms, SQLAlchemy, Flask, Babel, Elasticearch, etc.
SQLite
HTML
CSS
JavaScript
Full addons you can find in the file "[requirements.txt](https://github.com/Demanrusss/CS50x_Harvard/blob/main/Final_Project/Blog/requirements.txt)"

## !!!Attention!!! Problem almost solved
This IDE has its prons and cons. The only frustration was that when you start the application in order to test it every
library in virtual environment became as disconnected from the solution.
Here are some tips:
 * Close current solution.
 * Open another solution (it will be better if the path is completely different
 * Close that solution
 * Open the IDE and click on your solution to open.
 * Doesn't work? Repeat from the first step.
There is no answer through the InterNet on that bag.

# The pattern of the whole project is like MVC.
There are:
 * Models in just one file (actually we can easily divide it when really need) [models.py](https://github.com/Demanrusss/CS50x_Harvard/blob/main/Final_Project/Blog/app/models.py)
 * Views. Plenty of them in [templates](https://github.com/Demanrusss/CS50x_Harvard/tree/main/Final_Project/Blog/app/templates) folder
 * Controlers again in just one file [routes.py](https://github.com/Demanrusss/CS50x_Harvard/blob/main/Final_Project/Blog/app/routes.py)

# Also there are additional logic:
 * Sends email to change password in [email.py](https://github.com/Demanrusss/CS50x_Harvard/blob/main/Final_Project/Blog/app/email.py)
 * Error handlers in [errors.py](https://github.com/Demanrusss/CS50x_Harvard/blob/main/Final_Project/Blog/app/errors.py)
 * Search and indices in [search.py](https://github.com/Demanrusss/CS50x_Harvard/blob/main/Final_Project/Blog/app/search.py)
 * Translation of posts in [translate.py](https://github.com/Demanrusss/CS50x_Harvard/blob/main/Final_Project/Blog/app/translate.py)
 * Web application autoTranslation in beforehand prepared files in folder "[translations](https://github.com/Demanrusss/CS50x_Harvard/tree/main/Final_Project/Blog/app/translations)"

Icons or avatars were used from special web-site: https://www.gravatar.com
If you have been registered to that site, you can easily use your own avatar.

Testing
-------

Testing and code review is the bottleneck for development. But I did my best to write some unit-tests.
Honestly, it is quite tedious. And the most effective method for that project was starting the server!
Perhaps I will cover all the basic logic with tests, but not now.

### Automated Testing

Developers are strongly encouraged to write [unit tests](src/test/README.md) for new code, and to
submit new unit tests for old code. Unit tests can be compiled and run
(assuming they weren't disabled in configure) with: `make check`.

These [tests](https://github.com/Demanrusss/CS50x_Harvard/blob/main/Final_Project/Blog/tests.py) can be run

### Manual Quality Assurance (QA) Testing

Changes should be tested by somebody other than the developer who wrote the
code. This is especially important for large or high-risk changes. It is useful
to add a test plan to the pull request description if testing the changes is
not straightforward. Maybe, later I will do it.

Translations
------------

Changes to translations as well as new translations can be submitted to me by messages or email.
Please, follow me and see my [bio](https://github.com/Demanrusss)

Translations will be periodically pulled from [Deepl.com](https://www.deepl.com) and merged into the git repository. Now I have 
only three: Spanish, English, French
