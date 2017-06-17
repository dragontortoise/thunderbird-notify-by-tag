#!/usr/bin/env python

import unittest

import send_follow_up_email

class TestSendFollwUpEmail(unittest.TestCase):

  def get_sample_raw_nbtdata_str(self) -> str:
    """returns sample raw string in nbt-data file
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
      '"author":"Boy Sawd <boy@example.org>",' + \
      '"recipients":"Rui Nag <rui.nag@example.com>"}'

    return raw

  def test_grep_emails(self):
    self.assertEqual(send_follow_up_email.grep_emails(
        'How are you? hello@example.com hello \n<worl.d@example.local>'
      ),
      ['hello@example.com', 'worl.d@example.local'])

  def test_can_parse_nbtdata(self):
    """parse each line of nbt_data into a python data structure
    """

    nbtdata_lines = self.get_sample_raw_nbtdata_str().split('\n')

    nbtdata = send_follow_up_email.parsenbtdata(nbtdata_lines[0])

    self.assertEqual(nbtdata['subject'], 'server under maintenance')
    self.assertEqual(nbtdata['author'],
      'Sample Name <sample@example.com>')
    self.assertEqual(nbtdata['recipients'],
      'Chalo Huan <chalohuan@example.com>, Cart <cart@example.com>')

    nbtdata = send_follow_up_email.parsenbtdata(nbtdata_lines[1])

    self.assertEqual(nbtdata['subject'], 'status report - 20170614')
    self.assertEqual(nbtdata['author'],  'Nada <nada@example.com>')
    self.assertEqual(nbtdata['recipients'],
      'status-report@example.com, Kwanjai A <kwanjai@example.com>, ' + \
      '"Chalo D." <chalod@example.com>')

    nbtdata = send_follow_up_email.parsenbtdata(nbtdata_lines[2])

    self.assertEqual(nbtdata['subject'], 'Aug 4 - Aug 7, 30 people')
    self.assertEqual(nbtdata['author'],  'Boy Sawd <boy@example.org>')
    self.assertEqual(nbtdata['recipients'],
      'Rui Nag <rui.nag@example.com>')

if __name__ == '__main__':
  unittest.main()
