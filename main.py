import pandas as pd
import os
from datetime import datetime
from __init__  import DATA_FOLDER
from translator_extensions import clean_df, AWS_Translator

df = pd.read_csv(os.path.join(DATA_FOLDER, 'complaints.csv'))
cleaned_df = clean_df(df)

translator = AWS_Translator()
out = translator.translate_batch(cleaned_df)
out.to_csv(os.path.join(DATA_FOLDER, f"translated_text_{datetime.now().strftime('%Y-%m%d_%H:%m')}.csv"), index=False)
print('Code finished!')
