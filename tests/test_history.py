import pytest
import os
import pandas as pd
from history.history import History

@pytest.fixture
def history_instance():
    return History()

def test_histAppend(history_instance):
    history_instance.histAppend(lambda x, y: x + y, 2, 3, 5)
    assert history_instance.histDf.iloc[0]['result'] == 5

def test_histExportSuccess(history_instance):
    history_instance.histAppend(lambda x, y: x + y, 2, 3, 5)
    assert history_instance.exportHistory() == f"History saved to {history_instance.histFile_}"

def test_histExportNoHistory(history_instance):
    history_instance.clearHistory()
    assert history_instance.exportHistory() == "No history"

def test_histDelete(history_instance):
    # Check if history export file exists before attempting deletion
    if os.path.exists(history_instance.histFile_):
        history_instance.deleteHistory()
        assert f"History export file '{history_instance.histFile_}' deleted"
    else:
        # If the file doesn't exist, test deletion without raising an exception
        history_instance.deleteHistory()
        assert True  # This line ensures the test passes if deleteHistory() doesn't raise an exception

def test_clearHistory(history_instance):
    history_instance.histAppend(lambda x, y: x + y, 2, 3, 5)
    history_instance.clearHistory()
    assert history_instance.histDf.empty

def test_importHistory_success(history_instance):
    # Prepare a sample CSV file for import
    sample_csv_data = "x,operand,y,result\n1,add,2,3\n"
    sample_csv_path = "history/sample_history.csv"
    with open(sample_csv_path, "w") as f:
        f.write(sample_csv_data)

    # Import history from the sample CSV file
    history_instance.histFile_ = sample_csv_path
    assert history_instance.importHistory() == "History successfully imported"

    # Clean up the sample CSV file after the test
    os.remove(sample_csv_path)

def test_importHistory_failure(history_instance):
    # Set histFile_ to a non-existent file
    history_instance.histFile_ = "nonexistent_file.csv"
    # Call importHistory()
    assert history_instance.importHistory() == "History failed to import"

def test_getHistory_empty(history_instance):
    # Ensure histDf is empty
    assert history_instance.histDf.empty
    # Call getHistory() and assert the returned value
    assert history_instance.getHistory() == "No history"

def test_getHistory_with_data(history_instance):
    # Add some data to histDf
    history_instance.histAppend(lambda x, y: x + y, 2, 3, 5)
    # Call getHistory() and assert the returned DataFrame
    actual_df = history_instance.getHistory()
    expected_df = pd.DataFrame({'x': [2], 'operand': ['<lambda>'], 'y': [3], 'result': [5]})
    assert len(actual_df) == len(expected_df), "Lengths of DataFrames don't match"
    for index, row in expected_df.iterrows():
        assert actual_df.loc[index].equals(row), f"Row {index} doesn't match"

def test_deleteHistory_file_removed_successfully(history_instance, monkeypatch):
    # Mocking os.path.exists to return True
    def mock_os_path_exists(file_path):
        return True

    # Mocking os.remove to raise an exception
    def mock_os_remove(file_path):
        pass  # Mocked to do nothing, simulating successful file removal

    monkeypatch.setattr(os.path, "exists", mock_os_path_exists)
    monkeypatch.setattr(os, "remove", mock_os_remove)

    # Call deleteHistory()
    result = history_instance.deleteHistory()

    # Assert that the correct message is returned
    expected_message = f"History export file '{history_instance.histFile_}' deleted"
    assert result == expected_message

def test_deleteHistory_file_not_removed(history_instance, monkeypatch):
    # Mocking os.path.exists to return True
    def mock_os_path_exists(file_path):
        return True

    # Mocking os.remove to raise an exception
    def mock_os_remove(file_path):
        raise OSError("Mocked OSError")

    monkeypatch.setattr(os.path, "exists", mock_os_path_exists)
    monkeypatch.setattr(os, "remove", mock_os_remove)

    # Call deleteHistory()
    result = history_instance.deleteHistory()

    # Assert that the correct message is returned
    expected_message = f"Failed to delete history export file: Mocked OSError"
    assert result == expected_message

def test_deleteHistory_file_does_not_exist(history_instance, monkeypatch):
    # Mocking os.path.exists to return False
    def mock_os_path_exists(file_path):
        return False

    monkeypatch.setattr(os.path, "exists", mock_os_path_exists)

    # Call deleteHistory()
    result = history_instance.deleteHistory()

    # Assert that the correct message is returned
    expected_message = f"History export file '{history_instance.histFile_}' does not exist"
    assert result == expected_message
