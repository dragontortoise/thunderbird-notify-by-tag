Project Name: thunderbird-notify-by-tag
Thunderbird Extension Name: notify-by-tag

# Purpose

Send a notification email to each recipient in the To: list of each
email that matches the specified tag in Thunderbird.  We don't send
notification email to people in the CC list of BCC list as it is not
their direct responsibility and if it is so, then they should be added
to the To: list instead.  The email being sent is a new separated email
which does not have reference to the email specified by tag.  This is
in order to prevent unnecessary item in the email conversation view in
case we have to send multiple notification emails more than once.  The
notificaiton email shouldn't be part of the email conversation.  Imagine
if the notification email is part of the email conversation, when we
"Open in Conversation" that email, it will add an extra item to the
converstation tree.  The tree has its limit.  If there are too many
items in the tree, it looks bad.  For example, this is what happens
with my Thunderbird when there are too many items in the tree:

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

At some point, Thunderbird will not indent it anymore as there are not
enough space horizontally.

# Source Code File Structure Explanation

- readme.md : The readme file you are reading right now.

- notify-by-tag@dragon.tortoise/ : This directory is created and named
  according to Thunderbird Extension.  I name the extension as
  "notify-by-tag".  And I have to put my First Name and Last Name in
  this format "project-name@first_name.last_name".

  |- install.rdf : File required by Thunderbird Extension.  It
    is used for the extension installation process.


  |- chrome.manifest : We define GUI namespace here.  GUI in Thunderbird
    is defined in XUL file.  We create reference to each GUI component
    in chrome.manifest file.

    content : is a separated normal GUI component.

    overlay : is a modification/addition to Thunderbird's existing GUI
      components.  E.g. tools_menu.xul is for adding "notify-by-tag"
      menu item to Thunderbird's Tools menu.

  |- chrome/ : This directory contains all the GUI (XUL) files and
    Program Logic (JavaScript) files.

# Install

There are several different ways to install Thunderbird Extension.
I will show you a simple way in Linux.

- git clone git@github.com:dragontortoise/thunderbird-notify-by-tag.git
  or
  git clone https://github.com/dragontortoise/thunderbird-notify-by-tag.git

- Go to your Thunderbird extension directory in your Thunderbird
  Profile.  For example, ~/.thunderbird/sihe8lo0.default/extensions/ .

- Create a text file named notify-by-tag@dragon.tortoise .

- In this text file, you put a path to thunderbird-notify-by-tag source
  code.  For example,

  ~/thunderbird-notify-by-tag/notify-by-tag@dragon.tortoise

- Open Thunderbird and you are ready!  You can open GUI of
  thunderbird-notify-by-tag from Tools menu (Tools -> notify-by-tag).

References

- https://developer.mozilla.org/en-US/Add-ons/Thunderbird/Building_a_Th
  underbird_extension (shorten url: https://goo.gl/46VwA4 )
- https://developer.mozilla.org/en-US/Add-ons/Thunderbird
- https://github.com/protz/thunderbird-stdlib
- https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XUL/Tutorial/XUL_Structure
- https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XUL/XUL_Reference
- http://kb.mozillazine.org/Adding_items_to_menus
- https://dxr.mozilla.org/comm-central/source/
- https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIMsgFolder
- https://developer.mozilla.org/en-US/Add-ons/Thunderbird/HowTos/Folders_and_message_lists#Interacting_With_the_Current_Folder
