import kaggle
import os
import shutil
import pandas as pd
from typing import List
from sqlalchemy.engine.base import Engine

DEFAULT_TARGET_PATH = './data'


class KaggleConnector:
    """Kaggle Connector

    This class allows us to interact with Kaggle's API.
    """
    def __init__(self, dataset_name: str) -> None:
        """Class' Constructor

        Parameters
        ----------
        dataset_name : str
            Kaggle dataset name to search.
        """
        self.dataset = kaggle.api.dataset_list(search=dataset_name)[0]

    def dataset_download(
        self,
        target_path: str = DEFAULT_TARGET_PATH
    ) -> None:
        """Dataset Download Method

        This method is responsible for downloading a specific dataset
        and storing it in a folder.

        Parameters
        ----------
        target_path : str, optional
            The directory path where files will be downloaded,
            by default DEFAULT_TARGET_PATH
        """
        self._clean_directory(target_path)

        kaggle.api.dataset_download_files(
            self.dataset.ref, path=target_path, unzip=True
        )

    def load_dataset_into_table(
                        self,
                        engine: Engine,
                        target_path: str = DEFAULT_TARGET_PATH
                    ) -> None:
        """Load Dataset into Table

        This method inserts the data downloaded in the target_path
        into the table informed by the connection parameter.

        Parameters
        ----------
        engine : Engine
            Engine connector from sqlalchemy.create_engine.
        target_path : str, optional
            The directory path where files were downloaded,
            by default DEFAULT_TARGET_PATH
        """
        dataset_list = self._get_files_path(target_path)

        for dataset in dataset_list:
            file_name = os.path.basename(dataset).split('.')[0]

            df = pd.read_csv(dataset, delimiter=",")
            df.to_sql(
                file_name,
                con=engine,
                schema='bronze',
                if_exists='replace',
                index=False
            )

    def _clean_directory(
                    self,
                    target_path: str = DEFAULT_TARGET_PATH
                ) -> None:
        """Clean Directory

        This method cleans the target path directory.

        Parameters
        ----------
        target_path : str, optional
            The directory path where files were downloaded,
            by default DEFAULT_TARGET_PATH
        """
        if os.path.exists(target_path):
            shutil.rmtree(target_path)

    def _get_files_path(
                    self,
                    target_path: str = DEFAULT_TARGET_PATH
                ) -> List[str]:
        """Get Files Path

        This method returns a list of files' paths
        in the target_path directory.

        Parameters
        ----------
        target_path : str, optional
            The directory path where files were downloaded,
            by default DEFAULT_TARGET_PATH

        Returns
        -------
        List[str]
            List of files' paths.
        """
        dataset_list = []

        for path in os.listdir(target_path):
            if os.path.isfile(os.path.join(target_path, path)):
                dataset_list.append(os.path.join(target_path, path))

        return dataset_list
