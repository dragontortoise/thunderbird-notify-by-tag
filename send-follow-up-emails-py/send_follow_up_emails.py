#!/usr/bin/env python3

"""
send-follow-up-emails thunderbird addon generates data to sfue-data
file.  Each line in it is in JSON format: 

  {"subject":"the subject", "author":"email address of the author",
  "recipients":"email addresses in the 'to' field"}

  (without new line charactor)

Each line is the extracted data from each email that you want to send a
follow up email to related people.

This script reads it, and generates a Python dict which its keys are
each email address found in 'author' or 'recipients' except an email
address which is your email address (you wouldn't send the follow up
email to yourself, would you?).  And its values are list of email
subjects to be followed up.

Then, it iterates through the dict and send follow up email to each
person.
"""

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

def parsesfuedata(sfuedata_line) -> dict:
  """Returns dict with the following keys:
    - subject : email subject
    - author : the author of that email
    - recipients : the recipients in the 'to' field of that email
  """

  sfuedata = json.loads(sfuedata_line)

  return sfuedata

def generate_message_dict(raw_sfuedata, my_email):
  """Generate message dict from raw sfue-data.  This message dict will
  be used in a loop to send out notification emails to each recipients.
  """

  d = {'chalohuan@example.com' : '- server under maintenance\n' + \
    '- Aug 4 - Aug 7, 30 people'}

  return d

def run():
  """
  myself = ['a@example.com', 'b@example.org']

  # A dictionary which contains:
  #   key as an email address.
  #   value as a list of email subjects.
  to_notify = {}

  # Load JSON data from ~/tmp/sfue-data .
  # File format of sfue-data is:
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
