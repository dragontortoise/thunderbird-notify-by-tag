#!/usr/bin/env python

import unittest

import send_follow_up_emails

class TestSendFollwUpEmails(unittest.TestCase):

  def get_sample_raw_sfuedata_str(self) -> str:
    """returns sample raw string in sfue-data file
    """

    raw = '{"subject":"server under maintenance",' + \
      '"author":"Sample Name <sample@example.com>",' + \
      '"recipients":"Chalo Huan <chalohuan@example.com>, ' + \
      'Cart <cart@example.com>"}\n' + \
      '{"subject":"status report - 20170614",' + \
      '"author":"Nada <nada@example.com>",' + \
      '"recipients":"status-report@example.com, ' + \
      'Kwanjai A <kwanjai@example.com>, ' + \
      '\\"Chalo D.\\" <chalod@example.com>"}\n' + \
      '{"subject":"Aug 4 - Aug 7, 30 people",' + \
      '"author":"Yes <sample@example.com>",' + \
      '"recipients":"Rui Nag <rui.nag@example.com>"}'

    return raw

  def test_grep_emails(self):
    self.assertEqual(send_follow_up_emails.grep_emails(
        'How are you? hello@example.com hello \n<worl.d@example.local>'
      ),
      ['hello@example.com', 'worl.d@example.local'])

  def test_can_parse_sfuedata(self):
    """parse each line of sfue_data into a python dictionary with keys:
    'subject', 'author' and 'recipeints'
    """

    sfuedata_lines = self.get_sample_raw_sfuedata_str().split('\n')

    sfuedata = send_follow_up_emails.parsesfuedata(sfuedata_lines[0])

    self.assertEqual(sfuedata['subject'], 'server under maintenance')
    self.assertEqual(sfuedata['author'],
      'Sample Name <sample@example.com>')
    self.assertEqual(sfuedata['recipients'],
      'Chalo Huan <chalohuan@example.com>, Cart <cart@example.com>')

    sfuedata = send_follow_up_emails.parsesfuedata(sfuedata_lines[1])

    self.assertEqual(sfuedata['subject'], 'status report - 20170614')
    self.assertEqual(sfuedata['author'],  'Nada <nada@example.com>')
    self.assertEqual(sfuedata['recipients'],
      'status-report@example.com, Kwanjai A <kwanjai@example.com>, ' + \
      '"Chalo D." <chalod@example.com>')

    sfuedata = send_follow_up_emails.parsesfuedata(sfuedata_lines[2])

    self.assertEqual(sfuedata['subject'], 'Aug 4 - Aug 7, 30 people')
    self.assertEqual(sfuedata['author'],  'Yes <sample@example.com>')
    self.assertEqual(sfuedata['recipients'],
      'Rui Nag <rui.nag@example.com>')

  def test_can_generate_message_dict(self):
    raw_sfuedata = self.get_sample_raw_sfuedata_str()
    msg_dict = send_follow_up_emails.generate_message_dict(raw_sfuedata,
      'sample@example.com')

    self.assertEqual(msg_dict['chalohuan@example.com'],
      '- server under maintenance\n- Aug 4 - Aug 7, 30 people')
    self.assertEqual(msg_dict['cart@example.com'],
      '- server under maintenance')
    self.assertEqual(msg_dict['nada@example.com'],
      '- status report - 20170614')
    self.assertEqual(msg_dict['status-report@example.com'],
      '- status report - 20170614')
    self.assertEqual(msg_dict['kwanjai@example.com'],
      '- status report - 20170614')
    self.assertEqual(msg_dict['chalod@example.com'],
      '- status report - 20170614')
    self.assertEqual(msg_dict['rui.nag@example.com'],
      '- Aug 4 - Aug 7, 30 people')

if __name__ == '__main__':
  unittest.main()
