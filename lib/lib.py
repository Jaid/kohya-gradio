import torch
import gc

def freeMemory():
    torch.cuda.empty_cache()
    gc.collect()

def isColab():
    try:
        import google.colab
        return True
    except:
        return False
