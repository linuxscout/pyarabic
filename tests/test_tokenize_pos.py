import re
import unittest
import pyarabic.araby as araby 

# ~ TOKEN_PATTERN_SPLIT = re.compile(u"([\w\u064b-\u0652']+)", re.UNICODE)


# ~ def tokenize_with_location(text: str) -> list:
    # ~ """
    # ~ Tokenize text into words with their positions.

    # ~ Example:
        # ~ >>> text = "حدثنا ابن أبي عامر، قال: رايت مناما"
        # ~ >>> tokens = araby.tokenize_with_position(text)
        # ~ >>> print u"\\n".join(tokens)
         # ~ [{'token': 'حدثنا', 'start': 0,  'end': 5},
          # ~ {'token': 'ابن',   'start': 6,  'end': 9}, 
          # ~ {'token': 'أبي',   'start': 10, 'end': 13}, 
          # ~ {'token': 'عامر',  'start': 14, 'end': 18}, 
          # ~ {'token': 'قال',   'start': 20, 'end': 23}, 
          # ~ {'token': 'رايت',  'start': 25, 'end': 29},
           # ~ {'token': 'مناما','start': 30, 'end': 35}
           # ~ ]
        
   
    # ~ @param text: the input text.
    # ~ @type text: unicode.
    # ~ @return: list of dict of (tokens, starts, ends).
    # ~ @rtype: list of dict.
    # ~ """    
    # ~ tokens = []
    # ~ for match in TOKEN_PATTERN_SPLIT.finditer(text):
        # ~ tokens.append({
            # ~ "token": text[match.start(): match.end()],
            # ~ "start": match.start(),
            # ~ "end": match.end()
        # ~ })

    # ~ return tokens


class TestStringMethods(unittest.TestCase):

    def test_empty_word(self):
        text = ""
        self.assertEqual(araby.tokenize_with_location(text), [])

    def test_with_one_word(self):
        text = "قال"
        text_with_tashkeel = "قَالَ"

        result_tokenize_text = araby.tokenize_with_location(text)
        result_tokenize_text_with_tashkeel = araby.tokenize_with_location(text_with_tashkeel)

        self.assertEqual(result_tokenize_text[0]['token'], text)
        self.assertEqual(result_tokenize_text[0]['start'], 0)
        self.assertEqual(result_tokenize_text[0]['end'], 3)

        self.assertEqual(result_tokenize_text_with_tashkeel[0]['token'], text_with_tashkeel)
        self.assertEqual(result_tokenize_text_with_tashkeel[0]['start'], 0)
        self.assertEqual(result_tokenize_text_with_tashkeel[0]['end'], len(text_with_tashkeel))

    def test_with_two_words(self):
        text = "حذف الحركة"

        result_tokenize_text = araby.tokenize_with_location(text)
        toke = result_tokenize_text[0]['token']
        start = result_tokenize_text[0]['start']
        end = result_tokenize_text[0]['end']

        self.assertEqual(toke, text[start:end])

        toke = result_tokenize_text[1]['token']
        start = result_tokenize_text[1]['start']
        end = result_tokenize_text[1]['end']

        self.assertEqual(toke, text[start:end])

    def test_with_two_tashkeel_words(self):
        text = "حَذَفَ الْحَرَكَةُ"

        result_tokenize_text = araby.tokenize_with_location(text)
        toke = result_tokenize_text[0]['token']
        start = result_tokenize_text[0]['start']
        end = result_tokenize_text[0]['end']

        self.assertEqual(toke, text[start:end])

        toke = result_tokenize_text[1]['token']
        start = result_tokenize_text[1]['start']
        end = result_tokenize_text[1]['end']

        self.assertEqual(toke, text[start:end])

    def test_with_multi_words(self):
        text = "حذف الحركة الأخيرة فقط: قد تكون هي الحركة الإعرابية، لكن ليس في كل الحالات، مثلا يضربه، حركة الإعراب على الباء وليس على الهاء"

        result_tokenize_text = araby.tokenize_with_location(text)

        for token_dict in result_tokenize_text:
            token = token_dict['token']
            start = token_dict['start']
            end = token_dict['end']

            self.assertEqual(token, text[start:end])

    def test_with_space_first(self):
        text = "  حذف الحركة الأخيرة"

        result_tokenize_text = araby.tokenize_with_location(text)

        for token_dict in result_tokenize_text:
            token = token_dict['token']
            start = token_dict['start']
            end = token_dict['end']

            self.assertEqual(token, text[start:end])

        # assert length of array is 3
        self.assertEqual(len(result_tokenize_text), 3)

    def test_with_space_last(self):
        text = "حذف الحركة الأخيرة  "

        result_tokenize_text = araby.tokenize_with_location(text)

        for token_dict in result_tokenize_text:
            token = token_dict['token']
            start = token_dict['start']
            end = token_dict['end']

            self.assertEqual(token, text[start:end])

        # assert length of array is 3
        self.assertEqual(len(result_tokenize_text), 3)


    def test_with_space_first_last(self):
        text = "  حذف الحركة الأخيرة  "

        result_tokenize_text = araby.tokenize_with_location(text)

        for token_dict in result_tokenize_text:
            token = token_dict['token']
            start = token_dict['start']
            end = token_dict['end']

            self.assertEqual(token, text[start:end])

        # assert length of array is 3
        self.assertEqual(len(result_tokenize_text), 3)


    def test_last_word(self):
        text = "  حذف الحركة الأخيرة  "

        result_tokenize_text = araby.tokenize_with_location(text)

        last_word = result_tokenize_text[-1]['token']

        self.assertEqual(last_word, "الأخيرة")

    def test_first_word(self):
        text = "  حذف الحركة الأخيرة  "

        result_tokenize_text = araby.tokenize_with_location(text)

        last_word = result_tokenize_text[0]['token']

        self.assertEqual(last_word, "حذف")
        
    def test_alef_small_word(self):
        """ Test it Alef supscript is supported"""
        
        text = "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"

        result_tokenize_text = araby.tokenize(text)
        print(result_tokenize_text)
        print(" ".join(result_tokenize_text[1:]))

        self.assertEqual(len(result_tokenize_text),4)


if __name__ == '__main__':
    unittest.main()
