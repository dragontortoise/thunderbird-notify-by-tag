#!/usr/bin/env python

import unittest

import send_follow_up_email

class TestSendFollwUpEmail(unittest.TestCase):
  def test_grep_emails(self):
    self.assertEqual(send_follow_up_email.grep_emails(
        'How are you? hello@example.com hello \n<worl.d@example.local>'
      ),
      ['hello@example.com', 'worl.d@example.local'])

if __name__ == '__main__':
  unittest.main()
