import pandas as pd
import boto3
import os
from __init__  import DATA_FOLDER


df = pd.read_csv(os.path.join(DATA_FOLDER, 'complaints.csv'))


'''
class AWS_Translator():
    def __init__(self):
        self.translator = boto3.client(service_name='translate', use_ssl=True)
    def translate_batch(self,
                        df: pd.DataFrame,
                        text_lang_column: str = LANGUAGE_COL,
                        text_column: str = TEXT_COL,
                        output_language: str = 'en',
                        output_translated_column: str = TRANSLATED_COL) -> pd.DataFrame:
        messages_diff_lang = df[df[text_lang_column] != output_language][[text_column, text_lang_column]]
        for idx, row in messages_diff_lang.iterrows():
            result = self.translator.translate_text(Text=row[text_column], SourceLanguageCode=row[text_lang_column],
                                      TargetLanguageCode=output_language)
            messages_diff_lang.loc[idx, TEXT_COL] = result.get('TranslatedText', 'failed_translation')
        df[output_translated_column] = df[text_column].copy()
        df.loc[messages_diff_lang.index, output_translated_column] = messages_diff_lang[TEXT_COL]
        return df
'''
