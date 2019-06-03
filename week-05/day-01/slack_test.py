import unittest
import slack

class test_slack(unittest.TestCase):
    def test_number_of_id(self):
        self.assertEqual(len(slack.users), 83)
    
    def test_number_of_messages(self):
        self.assertEqual(len(slack.messages), 758)

    def test_number_of_reactions(self):
        self.assertEqual(len(slack.reactions), 563)

    def test_number_of_mentions(self):
        self.assertEqual(len(slack.mentions), 758)
        
if __name__ == "__main__":
    unittest.main()
