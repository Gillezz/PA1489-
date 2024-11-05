"""
Tests
"""


import unittest
from unittest.mock import patch, MagicMock
from config import create_database_if_not_exists

class TestCreateDatabaseIfNotExists(unittest.TestCase):
    @patch('config.MySQLdb.connect')
    def test_create_database_connection(self, mock_connect):
        """
        Simulating the database connection  validating if the correct parameters is sent into the method
        """
        create_database_if_not_exists()
        mock_connect.assert_called_once_with(
            host="db",
            user="root",
            passwd="password",
            port=3306
        )

    @patch('config.MySQLdb.connect')
    def test_create_database_query_execution(self, mock_connect):
        """
        Verifying that the correct commands runs

        """
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        create_database_if_not_exists()

        mock_cursor.execute.assert_called_once_with("CREATE DATABASE IF NOT EXISTS burger")
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()
