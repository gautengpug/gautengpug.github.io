Title: How to install Pythonbrew
Date: 2014-05-16 02:00
Tags: 2014, talks, pythonbrew
Author: Hussain
Summary: A quick guide to installing pythonbrew on your system.

Here is a quick guide to installing pythonbrew. It is taken from:

https://github.com/utahta/pythonbrew

Although I understand that the project is deprecated, I'm sure it will be very useful to all of you, especially if you are doing multiple things on different python versions.

This installation is leaning towards the *nix users in our group. This installation guide should work with most linux flavours (with a couple of shell-command changes if required) and possibly with OSX too (Apple guys).

Go ahead and open a terminal/shell-command and type this:

	curl -kL http://xrl.us/pythonbrewinstall | bash

You will find a .pythonbrew folder (most likely in your $USER).

Within the same directory .pythonbrew is, look for a .bashrc file. Open this file and at the end of the file, type this:

	[[ -s $HOME/.pythonbrew/etc/bashrc ]] && source $HOME/.pythonbrew/etc/bashrc

This command worked for me (on an old install). You could also try changing HOME to the name of the USER.

So for example, if your username on your system is "Jonny", the line above will look like this:

	[[ -s $Jonny/.pythonbrew/etc/bashrc ]] && source $Jonny/.pythonbrew/etc/bashrc

Let's add the latest Python 2.7 to the list of Pythons...

Go to this file: pythonbrew/etc/config.cfg

Open this file and go to line 170-175. You should see 2.7.5 as the last 2.7 version. Add this code and this is how it will look:

	[Python-2.7.5]
	url = http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tgz

	[Python-2.7.6]
	url = http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz
	latest = True

Start a fresh terminal/shell.

Now it's time to install pythonbrew with pip included. Just run this command:

	pythonbrew install --configure="--with-zlib" 2.7.6

This will take a while (unless you're using a 10MB/s or faster connection) so you can chill as it fetches 2.7.6 and installs it.

If the install is a success, you can close the current terminal and open a fresh one. Then type this:

	pythonbrew switch 2.7.6

This will keep 2.7.6 as the persistent python on your system. You can test it out by typing "python" in the terminal and it should tell you the version number.

Phewww!!! We're almost there!

Let's now create a virtual environment...

Type this in the terminal:

	pythonbrew venv init
	pythonbrew venv create gpug

You can then go ahead and install anything you like in this virtual environment. If you'd like to try out our site-blog, you can do this:

	pythonbrew venv use gpug
	pip install pelican
	pip install markdown

Clone our [site_generate](https://github.com/gautengpug/site_generate) and [gautengpug.github.io](https://github.com/gautengpug/gautengpug.github.io) and you'll have your dev environment setup.

If you're having problems installing pythonbrew, contact me via email and we can chat on Skype. I will help with whatever issues you're having.

Also, I recommend you install this at home(before the meetup) as Python is around 16MB and if too many people try installing it on the day, it will take a long while to download.
