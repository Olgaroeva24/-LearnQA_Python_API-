class Test_1:
    def test_check_len(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Phrase should be less than 15 characters, you phrase has {len(phrase)} characters"
