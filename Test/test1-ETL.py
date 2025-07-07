import pytest
import pandas as pd
from etl import extract_data; #transform_data; #load_data



def testextract_data():
    df = pd.read_csv("../data/input_data.csv")    
    assert not df.empty
    assert list(df.columns) == ["id","name","age","city","salary"]
    assert df.shape == (5, 7)
    

# def transform_data():
#     assert subtract(5, 3) == 2
#     assert subtract(2, 5) == -3

# def load_data():
#     assert multiply(2, 3) == 6
#     assert multiply(-1, 3) == -3

