import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
from pathlib import Path


def serialize_index(index, path="/content/faiss_index.pickle"):
    return faiss.write_index(index, path)


def deserialize_index(path):
    return faiss.read_index(path)


# Loading the model suitable for asymmetric semantic querying.
def build_index(
    model_name="distilbert-base-nli-stsb-mean-tokens",
    path="/data/dataset.csv",
):
    model = SentenceTransformer(model_name)

    df = pd.read_csv(path)

    # Prepare embeddings
    embeddings = model.encode(df.composite.to_list())

    # Change data type
    embeddings = np.array([embedding for embedding in embeddings]).astype("float32")

    # Instantiate the index
    index = faiss.IndexFlatL2(embeddings.shape[1])

    # Pass the index to IndexIDMap
    index = faiss.IndexIDMap(index)

    # Add vectors and their IDs
    index.add_with_ids(embeddings, df.index.to_numpy())

    return index