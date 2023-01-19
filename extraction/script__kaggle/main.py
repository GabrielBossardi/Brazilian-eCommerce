from kaggle_connector import KaggleConnector
from sqlalchemy import create_engine
from decouple import config


def main():
    DB_USER = config("DB_ROOT_USER")
    DB_PASS = config("DB_ROOT_PASSWORD")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT", default=5432)

    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}')

    kg = KaggleConnector("olistbr/brazilian-ecommerce")
    kg.dataset_download()
    kg.load_dataset_into_table(engine)

    engine.dispose()


if __name__ == "__main__":
    main()
