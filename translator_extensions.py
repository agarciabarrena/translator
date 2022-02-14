import pandas as pd
import boto3
from __init__ import INPUT_LANGUAGE_COLUMN, INPUT_ORIGINAL_TEXT, OUT_TRANSLATED_COLUMN, OUT_ORIGINAL_TEXT
from __init__ import OUT_LANGUAGE_COLUMN, language_dict_map

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    original_number_rows = df.shape[0]
    reduced_df = df[[INPUT_ORIGINAL_TEXT, INPUT_LANGUAGE_COLUMN]].copy()

    reduced_df.drop_duplicates(inplace=True)
    reduced_df.dropna(subset=[INPUT_ORIGINAL_TEXT], inplace=True)
    reduced_df = reduced_df[~reduced_df[INPUT_ORIGINAL_TEXT].str.match('^\d+$')]  # clean message consisting just in numbers

    for c in reduced_df.columns:
        reduced_df[c] = reduced_df[c].str.lower()
    reduced_df[INPUT_LANGUAGE_COLUMN] = reduced_df[INPUT_LANGUAGE_COLUMN].map(language_dict_map)

    print(f'df cleaned ({original_number_rows - reduced_df.shape[0]} rows cleaned, cleaned_df size {reduced_df.shape})')
    reduced_df.rename(columns={INPUT_ORIGINAL_TEXT: OUT_ORIGINAL_TEXT, INPUT_LANGUAGE_COLUMN: OUT_LANGUAGE_COLUMN}, inplace=True)
    reduced_df.reset_index(inplace=True, drop=True)
    return reduced_df


class AWS_Translator:
    def __init__(self):
        self.translator = boto3.client(service_name='translate', use_ssl=True)

    def translate_batch(self,
                        df: pd.DataFrame,
                        text_lang_column: str = OUT_LANGUAGE_COLUMN,
                        text_column: str = OUT_ORIGINAL_TEXT,
                        output_language: str = 'en',
                        output_translated_column: str = OUT_TRANSLATED_COLUMN) -> pd.DataFrame:
        print('Translating...')
        for idx, row in df.iterrows():
            if row[text_lang_column] != output_language:  # Translate
                result = self.translator.translate_text(Text=row[text_column],
                                                        SourceLanguageCode=row[text_lang_column],
                                                        TargetLanguageCode=output_language)
                df.loc[idx, output_translated_column] = result.get('TranslatedText', 'failed_translation')
            else:
                df.loc[idx, output_translated_column] = 'original_english_text'
        return df