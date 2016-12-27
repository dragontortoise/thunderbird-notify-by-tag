#!/usr/bin/env python3

# We use json as a mean to pass data from Thunderbird Addon to Python.
import json

# Regular Expression!
import re

# load JSON data from ~/tmp/nbt-data
#   for each JSON
#     send follow up emails

def grep_email(input_string):
  """
  This function greps all email addresses from the input_string and
  returns a list of them.
  """
  
  # I got this regular expression for email from
  # https://docs.python.org/3.1/library/re.html .
  return re.findall('(\w+@\w+(?:\.\w+)+)', input_string)

def run():

  # A dictionary which contains:
  #   key as an email address.
  #   value as a list of email subjects.
  to_notify = {}

  # load JSON data from ~/tmp/nbt-data
  with open('/home/ubuntu/tmp/nbt-data') as nbt_data_file:
    for line in nbt_data_file:
      message = json.loads(line)
      print(message['subject'])
     
if __name__ == '__main__':
  run()
