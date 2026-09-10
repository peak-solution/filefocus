"""
ExternalFileData class to read data from an external file using pandas.
"""

import logging
from typing import override

import pandas as pd
from ods_exd_api_box.simple.file_simple_interface import FileSimpleInterface


class ExternalFileData(FileSimpleInterface):
    """
    Concrete implementation for reading CSV files.

    """

    def __init__(self, file_path: str, parameters: dict):
        """
        Initialize the ExternalFileData class.
        :param file_path: Path to the external file.
        :param parameters: Parameters for reading the file (e.g., delimiter, header). Check pd.read_csv for details.
        """
        self.file_path: str = file_path
        self.parameters: dict = parameters
        self.df: pd.DataFrame | None = None
        self.log = logging.getLogger(__name__)

    @override
    def not_my_file(self) -> bool:
        """
        Check if the file should be read with this plugin.
        :return: True if the file should not be read with this plugin, False otherwise.
        """
        with open(self.file_path, "r", encoding="utf-8-sig") as file:
            return not file.readline().startswith("Point,")

    @override
    def data(self) -> pd.DataFrame:
        """
        Read the data from the file and return it as a pandas DataFrame.
        :return: DataFrame containing the data from the file.
        """
        if self.df is None:
            self.log.info("Reading file: %s", self.file_path)
            try:
                with open(self.file_path, "r", encoding="utf-8-sig") as file:
                    names = [
                        item.strip().strip('"') for item in file.readline().split(",")
                    ]
                    self._units = [
                        item.strip().strip('"') for item in file.readline().split(",")
                    ]

                # Read the data from the file - skip the header (already read)
                self.df = pd.read_csv(
                    self.file_path, sep=",", decimal=".", header=None, skiprows=3
                )
                self.df.columns = names

            except pd.errors.ParserError as e:
                self.log.info(
                    "Not My File: Error reading file %s: %s", self.file_path, e
                )
                self.df = pd.DataFrame()
        if self.df is None:
            self.df = pd.DataFrame()
        return self.df

    @override
    def column_units(self) -> list[str]:
        """
        Get the units of the columns in the file.
        :return: List of column units.
        """
        return self._units

    @classmethod
    @override
    def create(cls, file_path: str, parameters: dict) -> FileSimpleInterface:
        """Factory method to create a file handler instance."""
        return cls(file_path, parameters)

    @override
    def close(self) -> None:
        """
        Close the file and release resources.
        """
        if self.df is not None:
            self.log.info("Closing file: %s", self.file_path)
            del self.df
            self.df = None


if __name__ == "__main__":
    from ods_exd_api_box.simple import serve_plugin_simple

    serve_plugin_simple(
        file_type_name="CUSTOM_CSV",
        file_type_factory=ExternalFileData.create,
        file_type_file_patterns=["*.dat"],
    )
