import pandas as pd
import numpy as np

def prepareData(sklearnDataSet):
    
    bunch = sklearnDataSet()
    X, y = bunch["data"], bunch["target"]
    data  = np.hstack([X,y.reshape(-1,1)])
    cols_name_lst = bunch["feature_names"].tolist() + ["target"]
    return pd.DataFrame(data, columns = cols_name_lst), bunch["DESCR"]