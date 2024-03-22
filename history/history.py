import pandas as pd
from typing import Union, Callable

#    def performOperation(self, operation: Callable, x: Union[int, float], y: Union[int, float]) -> Union[int, float, None]:

class History:
    def __init__(self):
        self.histDf = pd.DataFrame(columns=['x', 'operand', 'y', 'result'], dtype=object)

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
          exportLocation = r'history/history_export.csv'
          self.histDf.to_csv(exportLocation, index=False)
          return f"History saved to {exportLocation}"
       
    def importHistory(self):
      importLocation = r'history/history_export.csv'
      try:
         self.histDf = pd.read_csv(importLocation)
         return "History successfully imported"
      except:
         return "History failed to import"
      
    def deleteHistoryRow(self):
       indexIn = input("Enter a row number to delete:")
       
       try:
          indexIn = int(indexIn)
       except:
          return "Invalid input"


       try:
          self.histDf = self.histDf.drop(indexIn, axis=0)
          return f"Row {indexIn} deleted from history"
       except:
          return "Row does not exist"