Title: 2nd Meetup: May 2014
Date: 2014-05-31 13:00
Category: Blog
Tags: 2014, meetup, talks, pythonbrew, portia, accounting, decorators, ipython
Author: Hussain
Summary: Feedback on the second meetup event.

Our second meetup was held on 17 May at the House4Hack.

We were expecting an attendance of 5 confirmed pythonistas, with any others that aren't that familiar with our group yet, to come through as well.

Unfortunately 2 members couldn't make it, so we were 3 pythonistas, with Gert being the *wildcard attendee (this proved to be an insightful activity, as Gert shared some interesting knowledge with us, but more on that later).

###We had 3 presentations (+ informal discussion) conducted on the day. These were:

###Frank - Presenting his accounting package:

I learnt a lot from Franks software presentation. Although the presentation was broken in 2, with being shown a demo initially (with some discussion about the software) and being given a more detailed overview at the end of the meetup.

Frank demonstrated how his accounting package went from a desktop application using a GUI, to a web-based application that is unlike any other you've seen.

Although it may at first seem like the application is relatively simple, we quickly learnt that what is "under the hood" in the software is some very powerful stuff.

Frank demonstrated how he had basically written every part of the software ("vanilla" style), which means that a lot of what you might expect from a web-framework, was written by Frank himself.

(I stand to be corrected on this) The software works through multiple threads, so if it crashes on 1 client, it will continue to work on others. We also learnt that the application works similar to an SPA (Single Page Application), with a variety of menu windows popping up per-request (and not through being hard-coded).

The software also had some other parts that I haven't quite wrapped my mind around yet, so it was a great way to discover that even with an application that would seem as simple as CRUD, that a lot of work is going on in the back.

I also suggested that Frank consider separating the concerns of the application from what is happening "underneath", so that he could fine-tune the framework-esque part to be more generic and let the accounting software run on top of it. We will see what Frank has to say about that at a future meetup.

Lastly, as a word of encouragement, I would like to tell Frank that his application is definitely well beyond "vaporware" and the extensive work he has put in to build the application will bear fruits soon.


###Nelis - Presenting [Decorators](http://tooblippe.github.io/insightstack-blog/2014/05/05/decorators/) within iPython:

Although I cannot give much detail into the technical part of using decorators (as I am still trying to understand them and their application), the talk by Nelis was very enlightening and informative.

(I stand to be corrected) Decorators are used for pre- and post-processing.

Nelis explained to us the use-case of decorators in his situation, where data needs to be flattened and then reshaped 10-12 times. The use of a decorator eliminates redundancy and maintenance, as you will not need to maintain 10-12 pieces of the same code.

The talk itself was also very well presented by Nelis (he lectures part-time, so we got to experience a thorough explanation of what is happening).

We also got to experience all this using iPython, which is proving to be a very popular and useful tool among data scientists.

Although I haven't yet tested it out for myself, you can expect to see a simple attendance graph being drawn with one of the graph libraries iPython provides :P

###Hussain - [Pythonbrew](https://github.com/utahta/pythonbrew) and [Portia](https://github.com/scrapinghub/portia):

My presentation was split into 2, with the first part being a "install at home" for Pythonbrew(http://gautengpug.github.io/how-to-install-pythonbrew.html) and then doing some visual web-scraping with Portia.

I have spoken at length about the merits of pythonbrew, but unfortunately the package has been deprecated for about a year now, and the Python Foundation has backed Pyenv as the option for virtual python environments in Python3 (Frank showed me the documentation that speaks about this).

I demonstrated using Portia by firstly explaining how to install it within a virtual environment (that was created within pythonbrew). Although I didn't get much time to test out Portia myself(I had a nightmare laptop issue 2 days before the presentation), I did manage to demo the basic steps involved in using the visual web-scraping tool.

This tool is pretty useful for any number of activities and simplifies web-scraping for most people. I would think it is especially useful for data scientists trying to extract data from a website that doesn't have an API (eg. government data that is accessuble to the public).

###Gert - Scaling, massive datasets, SSDs, Go-lang (and some Ruby):

Although Gert was attending primarily to help open/close H4H for us, we did have a great informal discussion with him about a variety of topics.

Gert explained to us how his team does tests at the H4H on an SSD-run PC/server. Their datasets are so huge that it takes 6+ hours to process.

We also discovered how most CRUD-based webapps have bottlenecks that aren't the CPU. I/O (Input/Output) being one of those bottlenecks, Gert explained how they approach this issue with a single-threaded, event-driven model.

There was also some mention of the C10K problem and how a Clojure server experimentally tested 1 million concurrent connections (we will need a reference on that one Gert!).

###Future Meetups and other matters:

Although the attendance shrunk a bit this time (in percentage terms, we're talking double-digits!), this was partly due to poor marketing (some may also refer to this as "Growth Hacking") of the event after the first meetup.

Luckily, Tobie has stepped in with a meetup.com group (http://www.meetup.com/Gauteng-Python-Users-Group/) and we have seen interest grow from a handle of users to almost 30 now!

Also, due to the info provided on the meetup group, we may also see the event being moved to our city neighbours (Joburg), as most of the members are based there (we still <3 you H4H).

Most of the event planning will now happen within the G-Group and the meetup site (sadly, this also signals the end of our experiment with static meetup attendance using github).

The next scheduled meetup will likely be held on: 21 June 2014.
Location/Venue and time will be decided (with location most likely shifting to Johannesburg) soon, so keep in touch via the G-Group or the meetup.com-Group.


Lastly, if you'd like to contribute to the site by writing on something interesting, all you need to do is to do your write-up in Markdown and email it to me (I will then publish it for you).

If you'd like to see how Markdown is written for this blog, see here:

https://github.com/gautengpug/site_generate/blob/master/content/Blog%20Post%201.md

Click on "Raw" on the right side of the screen to see the actual Markdown text.
