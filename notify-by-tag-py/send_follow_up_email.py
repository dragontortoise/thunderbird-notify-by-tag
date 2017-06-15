#!/usr/bin/env python3

# We use json as a mean to pass data from Thunderbird Addon to Python.
import json

# Regular Expression!
import re

# load JSON data from ~/tmp/nbt-data
#   for each JSON
#     send follow up emails

def grep_emails(input_string):
  """
  This function greps all email addresses from the input_string and
  returns a list of them.
  """
  
  # http://stackoverflow.com/questions/17681670/extract-email-sub-strin
  # gs-from-large-document
  return re.findall(r'[\w\.-]+@[\w\.-]+', input_string)

def run():
  """
  myself = ['a@example.com', 'b@example.org']

  # A dictionary which contains:
  #   key as an email address.
  #   value as a list of email subjects.
  to_notify = {}

  # Load JSON data from ~/tmp/nbt-data .
  # File format of nbt-data is:
  # 
  #   {"subject": "<a_subject>", "author":"<an_author">,
  #    "recipients":"<a_list_of_recipients>"}
  #
  # For example (without newline characters):
  #
  #   {"subject":"Hello World","author":"dragontortoise
  #   <dragontortoise@example.org>","recipients":"turtle
  #   <turtle@example.com>, duck <duck@example.com>"}
  # 
  with open('/home/ubuntu/tmp/nbt-data') as nbt_data_file:
    for line in nbt_data_file:
      message = json.loads(line)

      all_email_list = grep_emails(message['author']) + \
        grep_emails(message['recipients'])
      subject = message['subject']

      for email in all_email_list:
        if email not in myself:
          if email not in to_notify.keys():
            to_notify.get[email] = [subject]

  print(to_notify)
  """
     
if __name__ == '__main__':
  run()
