import os

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')


# Original df column names
INPUT_ORIGINAL_TEXT = 'Subject'
INPUT_LANGUAGE_COLUMN = 'Country'

# Optout df columns names
OUT_ORIGINAL_TEXT = 'text'
OUT_LANGUAGE_COLUMN = 'language'
OUT_TRANSLATED_COLUMN = 'translated_text'

# Language mapper for AWS translator languages  more info https://docs.aws.amazon.com/translate/latest/dg/what-is.html
language_dict_map = {'ee': 'et'}