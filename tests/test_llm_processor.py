import unittest
from unittest.mock import patch
from src.llm_processor import extract_email, extract_credit_card, find_similar_comments

class TestLLMProcessor(unittest.TestCase):
    @patch("src.llm_processor.openai.ChatCompletion.create")
    def test_extract_email(self, mock_openai):
        mock_openai.return_value = {"choices": [{"message": {"content": "test@example.com"}}]}
        result = extract_email("Email: test@example.com")
        self.assertEqual(result, "test@example.com")

    @patch("src.llm_processor.openai.ChatCompletion.create")
    def test_extract_credit_card(self, mock_openai):
        mock_openai.return_value = {"choices": [{"message": {"content": "4111-1111-1111-1111"}}]}
        result = extract_credit_card("image_path.png")
        self.assertEqual(result, "4111-1111-1111-1111")

    @patch("src.llm_processor.openai.Embedding.create")
    def test_find_similar_comments(self, mock_openai):
        mock_openai.return_value = {"data": [{"embedding": [0.1, 0.2]}, {"embedding": [0.2, 0.3]}]}
        comments = ["Comment 1", "Comment 2"]
        result = find_similar_comments(comments)
        self.assertEqual(result[0], "Comment 1")  # Assuming sorted order

if __name__ == "__main__":
    unittest.main()
