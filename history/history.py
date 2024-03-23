"""
A history module, used within the calculator to track all operations
that have been passed into it. Also includes methods for exporting
the history, printing it, importing it, or deleting the export file.
"""
import os
from typing import Union, Callable
import pandas as pd

class History:
    """
    This class represents a history of operations.
    """

    def __init__(self):
        """
        Initialize the History object.
        """
        self.hist_df = pd.DataFrame(columns=['x', 'operand', 'y', 'result'], dtype=object)
        self.hist_file = r'history/history_export.csv'

    def hist_append(self, operand: Callable, x: Union[int, float], y: Union[int, float],
                     result: Union[int, float]) -> None:
        """
        Append an operation to the history.

        Args:
            operand (Callable): The operation performed.
            x (Union[int, float]): The first operand.
            y (Union[int, float]): The second operand.
            result (Union[int, float]): The result of the operation.

        Returns:
            None
        """
        operand_name = operand.__name__
        row_append = pd.Series([x, operand_name, y, result], index=self.hist_df.columns)
        self.hist_df = pd.concat([self.hist_df, row_append.to_frame().T], ignore_index=True)

    def clear_history(self):
        """
        Clear the history.

        Returns:
            str: A message indicating that the history has been cleared.
        """
        self.hist_df = pd.DataFrame(columns=['x', 'operand', 'y', 'result'], dtype=object)
        return "History cleared"

    def get_history(self):
        """
        Get the history.

        Returns:
            Union[pd.DataFrame, str]: The history DataFrame if available, 
               otherwise a message indicating no history.
        """
        if self.hist_df.shape[0] == 0:
            return "No history"
        return self.hist_df

    def export_history(self):
        """
        Export the history to a CSV file.

        Returns:
            str: A message indicating whether the history was exported successfully.
        """
        if self.hist_df.shape[0] == 0:
            return "No history"
        self.hist_df.to_csv(self.hist_file, index=False)
        return f"History saved to {self.hist_file}"

    def import_history(self):
        """
        Import the history from a CSV file.

        Returns:
            str: A message indicating whether the history was imported successfully.
        """
        try:
            self.hist_df = pd.read_csv(self.hist_file)
            return "History successfully imported"
        except FileNotFoundError as e:
            return f"History file not found: {str(e)}"
        except pd.errors.EmptyDataError as e:
            return f"History file is empty: {str(e)}"
        except Exception as e:
            return f"History failed to import: {str(e)}"

    def delete_history(self):
        """
        Delete the history file.

        Returns:
            str: A message indicating whether the history file was deleted successfully or not.
        """
        if os.path.exists(self.hist_file):
            try:
                os.remove(self.hist_file)
                return f"History export file '{self.hist_file}' deleted"
            except Exception as e:
                return f"Failed to delete history export file: {str(e)}"
        return f"History export file '{self.hist_file}' does not exist"
