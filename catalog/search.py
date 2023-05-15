import numpy as np

def vector_search(query, model, index, num_results=10):
    """Tranforms query to vector using a pretrained, DistilBERT model 
    and finds similar vectors using FAISS.
    """
    vector = model.encode(list(query))
    D, I = index.search(np.array(vector).astype("float32"), k=num_results)
    return D, I

def id2details(df, I, column):
    """Returns the paper titles based on the paper index."""
    return [list(df[df.index == idx][column]) for idx in I[0]]