#!/usr/bin/env python

import unittest

import send_follow_up_email

class TestSendFollwUpEmail(unittest.TestCase):
  def test_grep_email(self):
    self.assertEqual(send_follow_up_email.grep_email(
        'How are you? hello@example.com \n<world@example.local>'
      ),
      ['hello@example.com', 'world@example.local'])

if __name__ == '__main__':
  unittest.main()
