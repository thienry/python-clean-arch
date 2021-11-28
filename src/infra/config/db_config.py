from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import sessionmaker


class DBConnectionHandler:
    """SqlAlchemy database connection"""

    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self) -> Engine:
        """
        Connection Engine.

        Returns:
            Engine connection to database.
        """

        return create_engine(self.__connection_string)

    def __enter__(self):
        """ """

        session_maker = sessionmaker()
        self.session = session_maker(bind=DBConnectionHandler.get_engine())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ """

        self.session.close()
