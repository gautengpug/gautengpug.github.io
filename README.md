site_generate
=============

Contains all the python files to generate the static(HTML, CSS, etc.) files.


This repo contains all the necessary files needed to generate the static output files.

You need to have Pelican (as well as Markdown) installed on your system to make this work. Best current way to do this is using venv (some *nix libraries required in python installation too).

Link to setup Pelican found here: 

    http://chdoig.github.io/create-pelican-blog.html

OR  here:

    https://gist.github.com/josefjezek/6053301


#how to create the site
Clone both this repo and the static web repo - gautengpug.github.io.

Edit/Add files in the content directory of this repo... Have a look at what is there to get an idea of the format. It is markdown...

Ok then run 

    make publish

To test your output run 

    make serve
    
This will give you a local server to check the whole site out locally. Go to

    localhost:8000
    
When you are ready to upload check the 'output' directory in the source folder. I just copy the whole directory from the output to the static site repo. When asked I only copy the changed files (mac). [wee need to make this easier]
When output is generated, make sure that you copy it from "output" folder into the gautengpug.github.io folder/repo. Only output must exist in that repo.

Remember to commit and push both the source and output back to their respective repos.

