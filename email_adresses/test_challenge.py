import unittest

from challenge import how_many_unique_emails


class TestHowManyUniqueEmails(unittest.TestCase):

    def test_only_one_email(self):
        self.assertEqual(how_many_unique_emails(1, 'daniel.zingaro@gmail.com'), 1)

    def test_two_valid_emails(self):
        self.assertEqual(how_many_unique_emails(2, 'daniel.zingaro@gmail.com', 'guilherme.gouw@gmail.com'), 2)

    def test_two_emails_one_valid_plus_sign(self):
        self.assertEqual(how_many_unique_emails(2, 'daniel.zingaro@gmail.com', 'daniel.zingaro+doesnotcount@gmail.com'), 1)

    def test_two_emails_one_valid_exclude_dots_before_at(self):
        self.assertEqual(how_many_unique_emails(2, 'daniel.zingaro@gmail.com', 'danielzingaro@gmail.com'), 1)
    
    def test_three_emails_one_valid_exclude_dots_before_at_and_plus(self):
        self.assertEqual(how_many_unique_emails(
            3, 
            'daniel.zingaro@gmail.com', 
            'danielzingaro@gmail.com', 
            'daniel.zingaro+doesnotcount@gmail.com'
            ), 1)



if __name__=='__main__':
    unittest.main()
