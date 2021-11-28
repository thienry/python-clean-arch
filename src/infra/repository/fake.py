from src.infra.entities import Users
from src.infra.config import DBConnectionHandler


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert_use(cls):
        """Something"""

        with DBConnectionHandler() as db_conn:
            try:
                new_user = Users(name="Software Engineer", passwd="qwerty")
                db_conn.session.add(new_user)
                db_conn.session.commit()
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()
