import pandas as pd

class History:
    def __init__(self):
        self.histDf = pd.DataFrame(columns=['x', 'operand', 'y', 'result'], dtype=object)

    def histAppend(self, operand, x, y, result):
        operandName = operand.__name__
        rowAppend = pd.Series([x, operandName, y, result], index=self.histDf.columns)
        self.histDf = pd.concat([self.histDf, rowAppend.to_frame().T], ignore_index=True)

    def clearHistory(self):
        self.histDf = pd.DataFrame(columns=['x', 'operand', 'y', 'result'], dtype=object)

    def getHistory(self):
      if self.histDf.shape[0] == 0:
        return "No history"
      else:
        return self.histDf
