import unittest
import pandas as pd
from datalad_helloworld.runner.actions import Actions
from datalad_helloworld.utils.folder import Folder
from datalad_helloworld.utils.dataframe import Dataframe
class TestActions(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        self.df = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18],"DateBorn":["2020-01-02","2020-04-02","2021-01-02","2022-01-02"]}  
        self.operations = {"upper": "true"}
        self.filepath = f"{Folder().getcurrent()}/datalad_helloworld/tests/resources/settings_base.json"
        self.settings = Folder(self.filepath).read()
    def test_tokenization(self):
        dfa = pd.DataFrame(self.df)
        path = f"{Folder().getcurrent()}/datalad_helloworld/tests/resources/test_tokenization.parquet"
        self.settings["file"]["path"] = path
        act = Actions("Name",self.settings,dfa,self.filepath)
        act.tokenization()
        res = act.dataframe
        self.assertTrue(isinstance(res,pd.DataFrame))
    def test_ofuscation(self):
        dfa = pd.DataFrame(self.df)
        path = f"{Folder().getcurrent()}/datalad_helloworld/tests/resources/test_ofuscation.parquet"
        self.settings["file"]["path"] = path
        act = Actions("DateBorn",self.settings,dfa,self.filepath)
        act.ofuscation()
        res = act.dataframe
        self.assertTrue(isinstance(res,pd.DataFrame))
    def test_anonymation(self):
        dfa = pd.DataFrame(self.df)
        path = f"{Folder().getcurrent()}/datalad_helloworld/tests/resources/test_anonymation.parquet"
        self.settings["file"]["path"] = path
        act = Actions("Age",self.settings,dfa,self.filepath)
        act.anonymation()
        res = act.dataframe
        self.assertTrue(isinstance(res,pd.DataFrame))