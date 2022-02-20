from gensim.models import KeyedVectors
import os
import glob
from tqdm import tqdm
import pandas as pd

MODEL_FOLDER_PATH = 'D:\\word2vec_Ngram_analysis\\Models\\'

keyed_vector_files = glob.glob(MODEL_FOLDER_PATH+'*.bin')

# To store model info
df = pd.DataFrame(columns=['Filename', 'Vocab Size'])

for i in tqdm(range(len(keyed_vector_files))):
    # Load file
    model = KeyedVectors.load_word2vec_format(keyed_vector_files[i], binary=True)
    filename = os.path.basename(keyed_vector_files[i])
    vocab_sz = len(model)
    df = df.append({'Filename': filename,
               'Vocab Size':vocab_sz},
              ignore_index=True)

# Export model info to csv
df.to_csv(MODEL_FOLDER_PATH+'model_info.csv', index=False)