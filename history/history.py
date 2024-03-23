import os
import pandas as pd
from typing import Union, Callable

#    def performOperation(self, operation: Callable, x: Union[int, float], y: Union[int, float]) -> Union[int, float, None]:

class History:
    def __init__(self):
        self.histDf = pd.DataFrame(columns=['x', 'operand', 'y', 'result'], dtype=object)
        self.histFile_ = r'history/history_export.csv'

    def histAppend(self, operand: Callable, x: Union[int, float], y: Union[int, float], result: Union[int, float]) -> None:
        operandName = operand.__name__
        rowAppend = pd.Series([x, operandName, y, result], index=self.histDf.columns)
        self.histDf = pd.concat([self.histDf, rowAppend.to_frame().T], ignore_index=True)
        return None

    def clearHistory(self):
        self.histDf = pd.DataFrame(columns=['x', 'operand', 'y', 'result'], dtype=object)
        return "History cleared"

    def getHistory(self):
      if self.histDf.shape[0] == 0:
        return "No history"
      else:
        return self.histDf

    def exportHistory(self):
       if self.histDf.shape[0] == 0:
          return "No history"
       else:
          self.histDf.to_csv(self.histFile_, index=False)
          return f"History saved to {self.histFile_}"
       
    def importHistory(self):
      
      try:
         self.histDf = pd.read_csv(self.histFile_)
         return "History successfully imported"
      except:
         return "History failed to import"
      
    def deleteHistory(self):

      if os.path.exists(self.histFile_):
         try:
               os.remove(self.histFile_)
               return f"History export file '{self.histFile_}' deleted"
         except Exception as e:
               return f"Failed to delete history export file: {str(e)}"
      else:
         return f"History export file '{self.histFile_}' does not exist"