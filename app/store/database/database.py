from typing import Optional, TYPE_CHECKING, Any
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.store.database.sqlalchemy_base import db

if TYPE_CHECKING:
    from app.web.app import Application


class Database:
    def __init__(self, app: "Application"):
        self.app = app
        self._engine: Optional[AsyncEngine] = None
        self._db: Optional[declarative_base] = None
        self.session: Optional[sessionmaker[AsyncSession]] = None
        self.url = f"postgresql+asyncpg://{app.config.database.user}:{app.config.database.password}@{app.config.database.host}/{app.config.database.database}"

    async def connect(self, *_: Any, **__: Any) -> None:
        self._db = db
        self._engine = create_async_engine(url=self.url, echo=True)
        self.session = sessionmaker(
            self._engine,
            expire_on_commit=False,
            autoflush=True,
            class_=AsyncSession
        )

    async def disconnect(self, *_: list, **__: dict) -> None:
        try:
            await self._engine.dispose()
        except:
            pass

