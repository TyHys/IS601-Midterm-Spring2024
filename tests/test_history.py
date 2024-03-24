# pylint: disable=redefined-outer-name

"""
Tests to validate the history module
"""
import os
import pytest
import pandas as pd
from history.history import History

@pytest.fixture
def history_instance():
    """
    Fixture to return an instance of the History class
    """
    return History()

def test_hist_append(history_instance):
    """
    Test the hist_append method of the History class
    """
    history_instance.hist_append(lambda x, y: x + y, 2, 3, 5)
    assert history_instance.hist_df.iloc[0]['result'] == 5

def test_hist_export_success(history_instance):
    """
    Test the export_history method of the History class
    """
    history_instance.hist_append(lambda x, y: x + y, 2, 3, 5)
    assert history_instance.export_history() == f"History saved to {history_instance.hist_file}"

def test_hist_export_no_history(history_instance):
    """
    Test the export_history method of the History class with no history    
    """
    history_instance.clear_history()
    assert history_instance.export_history() == "No history"

def test_hist_delete(history_instance):
    """
    Test the delete_history method of the History class
    """
    # Check if history export file exists before attempting deletion
    if os.path.exists(history_instance.hist_file):
        history_instance.delete_history()
        assert f"History export file '{history_instance.hist_file}' deleted"


def test_clear_history(history_instance):
    """
    Test the clear_history method of the History class
    """
    history_instance.hist_append(lambda x, y: x + y, 2, 3, 5)
    history_instance.clear_history()
    assert history_instance.hist_df.empty

def test_import_history_success(history_instance):
    """
    Test the import_history method of the History class
    """
    # Prepare a sample CSV file for import
    sample_csv_data = "x,operand,y,result\n1,add,2,3\n"
    sample_csv_path = "history/sample_history.csv"
    with open(sample_csv_path, "w", encoding="utf-8") as f:
        f.write(sample_csv_data)


    # Import history from the sample CSV file
    history_instance.hist_file = sample_csv_path
    assert history_instance.import_history() == "History successfully imported"

    # Clean up the sample CSV file after the test
    os.remove(sample_csv_path)

def test_import_history_failure(history_instance):
    """
    Test the import_history method of the History class with a non-existent file
    """
    # Set hist_file to a non-existent file
    history_instance.hist_file = "nonexistent_file.csv"
    # Call import_history()
    ex_msg = "History file not found: nonexistent_file.csv"

    assert history_instance.import_history() == ex_msg


def test_get_history_empty(history_instance):
    """
    Test the get_history method of the History class with no history
    """
    # Ensure hist_df is empty
    assert history_instance.hist_df.empty
    # Call get_history() and assert the returned value
    assert history_instance.get_history() == "No history"

def test_get_history_with_data(history_instance):
    """
    Test the get_history method of the History class with some data
    """
    # Add some data to hist_df
    history_instance.hist_append(lambda x, y: x + y, 2, 3, 5)
    # Call get_history() and assert the returned DataFrame
    actual_df = history_instance.get_history()
    expected_df = pd.DataFrame({'x': [2], 'operand': ['<lambda>'], 'y': [3], 'result': [5]})
    assert len(actual_df) == len(expected_df), "Lengths of DataFrames don't match"
    for index, row in expected_df.iterrows():
        assert actual_df.loc[index].equals(row), f"Row {index} doesn't match"

def test_delete_history_file_removed_successfully(history_instance, monkeypatch):
    """
    Test the delete_history method of the History class with successful file removal
    """
    # Mocking os.path.exists to return True
    def mock_os_path_exists(_file_path):
        return True

    # Mocking os.remove to raise an exception
    def mock_os_remove(_file_path):
        pass  # Mocked to do nothing, simulating successful file removal

    monkeypatch.setattr(os.path, "exists", mock_os_path_exists)
    monkeypatch.setattr(os, "remove", mock_os_remove)

    # Call delete_history()
    result = history_instance.delete_history()

    # Assert that the correct message is returned
    expected_message = f"History export file '{history_instance.hist_file}' deleted"
    assert result == expected_message

def test_delete_history_file_not_removed(history_instance, monkeypatch):
    """
    Test the delete_history method of the History class with failed file removal
    """
    # Mocking os.path.exists to return True
    def mock_os_path_exists(_file_path):
        return True

    # Mocking os.remove to raise a different exception
    def mock_os_remove(_file_path):
        raise FileNotFoundError("Mocked FileNotFoundError")

    monkeypatch.setattr(os.path, "exists", mock_os_path_exists)
    monkeypatch.setattr(os, "remove", mock_os_remove)

    # Call delete_history()
    result = history_instance.delete_history()

    # Assert that the correct message is returned
    expected_message = "File not found: Mocked FileNotFoundError"
    assert result == expected_message




def test_delete_history_file_does_not_exist(history_instance, monkeypatch):
    """
    Test the delete_history method of the History class when the file doesn't exist
    """
    # Mocking os.path.exists to return False
    def mock_os_path_exists(_file_path):
        return False

    monkeypatch.setattr(os.path, "exists", mock_os_path_exists)

    # Call delete_history()
    result = history_instance.delete_history()

    # Assert that the correct message is returned
    expected_message = f"History export file '{history_instance.hist_file}' does not exist"
    assert result == expected_message

def test_import_history_empty_file(history_instance):
    """
    Test the import_history method of the History class with an empty file
    """
    # Create an empty CSV file
    with open(history_instance.hist_file, "w", encoding="utf-8"):
        pass

    expected_msg = "History file is empty: No columns to parse from file"
    assert history_instance.import_history() == expected_msg
