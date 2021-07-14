# Python-May-2021

This program pulls data from a compilation of emails related to my Graduate thesis project.  This Python parses a text file comprising emails between myself and collaborators over the course of a year and a half.  The emails are separated into email chains, which may or may not span multiple dates with multiple recipients. The emails span between Fall 2011- May 2013, and are tagged with keywords to be parsed for behavioral tracking through email communication patterns.  

Features included:
1) Regex use to parse email chain numbers, dates, and collaborator emails.
2) A dictionary of representative data in the form of tuples.
3) Pandas used to create a database from dicctionary, and for data manipulation.

Details on running this project:
* MY code uses import sys, because the text file is stored locally.  I uploaded my original text file to github, but I think it's possible to apply some of this program to other text files that include similar data patterns, as well.
* You've got to download pandas and regular expressions to run this program. a command line pip-install is the way to go. 

Features of this project incude:

* Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
* Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code
* Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program


This is a personal passion project, and an attempt to revisit an auto-ethnographic study of my communication patterns, to improve my approaches to commuicating with collaborators. 

Areas for future improvement:
*integrating regex within panda expressions to reduce code blocks.
*create a dictionary of actual values from the full text file, rather than a dictionary constructed of repreenattive data.

