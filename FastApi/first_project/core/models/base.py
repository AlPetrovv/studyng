from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    """
    Base class for models (like class Model in Django)
    Class is abstract (__abstract__ = True), no declared in db
    attributes:
        id: Mapped - annotation that id is column in db
            mapped_column - create column in db with params(like primary_key=True)
        __tablename__ - name of table
    """

    __abstract__ = True
    # id - Mapped[int] - annotation that show to
    id: Mapped[int] = mapped_column(primary_key=True)

    # declared_attr - declared some attr as property in model
    # use for relationship or property (directive)
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"shop_app__{cls.__name__.lower()}s"
