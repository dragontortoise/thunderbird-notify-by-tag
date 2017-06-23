vim: syntax=markdown

Project Name: thunderbird-send-follow-up-emails

Thunderbird Extension Name: send-follow-up-emails

# Purpose

I need a simple way to send folllow up emails to my colleagues at work.

Here is the situation.  I send emails to my colleagues which I expect
them to reply me.  I tag (using Thunderbird's tag function) each sent
email with my custom 'Expecting Reply' tag.  I wait long enough until I
feel it is time to follow up.  I then decide to send each of them a
follow up email.  I do not want to send follow up email to them by
replying to the existing sent email as that will link my follow up email
to the existing email.  Linking them results in too many unnecessary
items in the conversation tree view in Thunderbird as you can see from
the following ascii picture:

~~~
Some Email
|- Re: Some Email
    |- Re: Some Email
        |- Re: Some Email
            |- Re: Some Email
                |- Re: Some Email
                    |- Re: Some Email
                        |- Re: Some Email
                        ...
                        ...
                        ...
                               |- Re: Some Email
                               |- Re: Some Email
                               |- Re: Some Email
                               |- Re: Some Email
~~~

For each sent email I expect to be replied, I manually tag them with a
custom tag I created, 'Expecting Reply'.  I then have a Saved Search
Folder I created with the same name as the tag, 'Expecting Reply', which
show all emails with 'Expecting Reply' tag.  (The tag and Saved Search
Folder can be easily created manually from the GUI of Thunderbird.)

Each day I go through each email in the 'Expecting Reply' Saved Search
Folder to find which email I need to send a follow up.  I use vi to
write down something that looks like this:

~~~  
john@example.com
  - Re: [pythoner] When will you push your code?
  - Will you come to my birthday dinner?

smith@example.com
  - Re: Send invoices to 3 clients
  - Purchase 3 books from Amazon
  - Re: Purchase 2 x Raspbery Pi
~~~

After going through all emails in this 'Expecting Reply' Saved Search
Folder, I get a complete list of what I am going to follow up in vi.  I
then send the email subject list to each person with each new separated
email.  For example:

~~~
To: john@example.com
Subject: Follow Up
Email Content:
  List of email subjects
  - Re: [pythoner] When will you push your code?
  - Will you come to my birthday dinner?

---

To: smith@example.com
Subject: Follow Up
Email Content:
  List of email subjects
  - Re: Send invoices to 3 clients
  - Purchase 3 books from Amazon
  - Re: Purchase 2 x Raspbery Pi
~~~

Each of the recipients who receives my follow up email will search from
the email subject I provide and sort the result by date in descending
order.  The newest one is the supposed email they should give me a
reply.  (Or they might use other way as this depends on how they use
their email, e.g. they might tag these emails and they should search
from the tagged emails instead.)

This project, *thunderbird-send-follow-up-emails*, is to save your time
on the following steps:

- Writing down what you want to follow up in vi.
- Sending email with email subject list from vi to each person.

With *thunderbird-send-follow-up-emails*, when you go through each email
in the 'Expecting Reply' Saved Search Folder, you just press the key,
'alt+t, n' ('alt+t', release all keys, 'n'), and the program will save
each email subject together with email addresses of the persons whom you
want to send the follow up email to into a data file.  Once you are done
with selecting emails, you then execute a Python script provided by this
project which will send follow up emails based on the data in the
generated data file.

Flow of data:

~~~
Thunderbird -> ~/tmp/sfue-data -> Python Script
~~~

# History

Initially when I started this project, I wanted to developed a
Thunderbird Add-On which would send follow up emails for each email
which has the specified tag if is left unanswered for at least the
specified number of days.  It was a pain for me to find out how to
develop add-on in Thunderbird with JavaScript.  I am new to JavaScript
and the whole JavaScript environments.  I found it was very difficult to
find documentations and howtos to develop such things I wanted with
Thunderbird.  It was more like trial-and-error instead of the preferred
way which were to read proper textbooks and start coding.  At the end, I
was able to use Gloda to search all emails matchiing the specified tag.
But, unfortunately, there were some errors i.e. some emails which did
not have that tag also came up in the search result.  I then decided to
give up.  And here comes my new approach which does not have coding
related to the tag.  I just use minimal JavaScript code to export data
from Thunderbird into file and then use external Python script for the
rest of the works.

# Source Code File Structure Explanation

- readme.md : The readme file you are reading right now.

- send-follow-up-emails&#64;dragon.tortoise/ : This directory is created
  and named according to Thunderbird Extension.  I name the extension as
  "send-follow-up-emails".  And I have to put my First Name and Last
  Name in this format "project-name@first\_name.last\_name".

  - install.rdf : File required by Thunderbird Extension.  It is used
    for the extension installation process.

  - chrome.manifest : We define GUI namespace here.  GUI in Thunderbird
    is defined in XUL file.  We create reference to each GUI component
    in chrome.manifest file.

    content : is a separated normal GUI component or JavaScript file.

    overlay : is a modification/addition to Thunderbird's existing GUI
      components.  E.g. tools_menu.xul is for adding
      "send-follow-up-emails" menu item to Thunderbird's Tools menu.

  - chrome/ : This directory contains all the GUI (XUL) files and
    Program Logic (JavaScript) files.

    - content/send-follow-up-emails.js : Our JavaScript main JavaScript
      code is here.
    - content/tools\_menu.xul : GUI definition for the
      'send-follow-up-emails' menu item under Tools menu.

# Install

There are several different ways to install Thunderbird Extension.
I will show you a simple way in Linux.

~~~
% cd
% mkdir project
% cd project
% git clone \
  git@github.com:dragontortoise/thunderbird-send-follow-up-emails.git
~~~

Assuming your Thunderbird Profile directory is:

  `~/.thunderbird/sihe8lo0.default`

~~~
% pushd ~/.thunderbird/sihe8lo0.default/extensions/
% cat > send-follow-up-emails@dragon.tortoise
~/project/thunderbird-send-follow-up-emails/send-follow-up-emails@dragon.tortoise
% echo -n "~/project/thunderbird-send-follow-up-emails" \
  >> send-follow-up-emails@dragon.tortoise
% echo -n "/send-follow-up-emails@dragon.tortoise" \
  >> send-follow-up-emails@dragon.tortoise
~~~

Open Thunderbird and you are ready!  You should notice
thunderbird-send-follow-up-emails from Tools menu (Tools ->
send-follow-up-emails).

# Environment I test my software with

- Debian 9.0
- Thunderbird 45.8.0
- Python 3.4.2

# Other Follow Up solutions

- https://addons.mozilla.org/en-US/thunderbird/addon/follow-up/

# References

- https://developer.mozilla.org/en-US/Add-ons/Thunderbird/Building_a_Thunderbird_extension
- https://developer.mozilla.org/en-US/Add-ons/Thunderbird
- https://github.com/protz/thunderbird-stdlib
- https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XUL/Tutorial/XUL_Structure
- https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XUL/XUL_Reference
- http://kb.mozillazine.org/Adding_items_to_menus
- https://dxr.mozilla.org/comm-central/source/
- https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIMsgFolder
- https://developer.mozilla.org/en-US/Add-ons/Thunderbird/HowTos/Folders_and_message_lists#Interacting_With_the_Current_Folder
