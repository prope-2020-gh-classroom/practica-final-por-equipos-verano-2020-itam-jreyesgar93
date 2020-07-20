import numpy as np
import pandas as pd

def label(x, groups=None):
    if groups is None:
        return "Other_label"
    else:
        for key, val in groups.items():
            if x in val:
                return key
        return "Other_label"