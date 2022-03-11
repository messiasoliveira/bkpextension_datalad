import unittest
import pandas as pd
from datalad_helloworld.writers.dataframe import Dataframe
from datalad_helloworld.utils.folder import Folder
class TestDataframe(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        self.path = f"{Folder().getcurrent()}/datalad_helloworld/tests/resources/test_"
        self.settings_csv = {"file":{"format":"csv","separator":";","names":[],"header":0,"path":self.path+"w_names.csv"}}
        self.settings_parquet = {"file":{"format":"parquet","path":self.path+"exists.parquet"}}
        self.settings_none = {"file":{"format":"","path":self.path+"exists.parquet"}}
        self.dataframe = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
    def test_read_none(self):
        res = Dataframe().read(self.settings_none)
        self.assertTrue(res == None)
    def test_read_parquet(self):
        res = Dataframe().read(self.settings_parquet)
        self.assertTrue(isinstance(res,pd.DataFrame))
    def test_read_csv(self):
        res = Dataframe().read(self.settings_csv)
        self.assertTrue(isinstance(res,pd.DataFrame))
    def test_write_none(self):
        res = Dataframe().write(None,self.settings_none)
        self.assertTrue(res == None)
    def test_write_parquet(self):
        df = pd.DataFrame(self.dataframe)
        res = Dataframe().write(df,self.settings_parquet)
        self.assertTrue(res == None)
    def test_write_csv(self):
        df = pd.DataFrame(self.dataframe)
        res = Dataframe().write(df,self.settings_csv)
        self.assertTrue(res == None)