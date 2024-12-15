# sqlalchemy.ext -
from asyncio import current_task

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from ..config import settings


class DBHalper:
    def __init__(self, db_url: str, echo: bool = False):
        # create async engine (connection pool)
        # need to write url to db and additional params
        self.engine = create_async_engine(
            url=db_url,
            echo=echo,
        )
        # create session factory
        # autoflush - prepare session for commit
        # autocommit - commit session
        # expire_on_commit - expire session after commit
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_engine(self):
        with self.engine.begin() as conn:
            return conn

    # scope function provides context for session
    # create scoped session (session in scope(пространство))
    def get_scoped_session(self):
        # scopefunc - function that return current task
        # current_task - return current task
        # sqlalchemy will be used session for specific task(handler)
        """
        Return a scoped session.

        The session is tied to the current task. Each task will have its own session.
        The session is created using `session_factory` and `scopefunc`.

        The session is scoped to the current task. This means that the session will be
        closed when the task is finished.

        :return: A scoped session.
        """
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        """
        Session dependency for FastAPI.

        This method is a dependency for FastAPI.
        It creates a scoped session and yields it.
        After the session is used, it is removed.
        """
        # yield - return session but session is not closed
        # after session is used - it will be closed
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DBHalper(
    db_url=settings.db_url,
    echo=settings.db_echo,
)
