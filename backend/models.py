# from typing import List
# from typing import Optional
# from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
  pass

class ProductModel(Base):
  __tablename__ = "products"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(64))
  price: Mapped[float]
  stock: Mapped[int]
  description: Mapped[str] = mapped_column(String(64))

  def __repr__(self) -> str:
    return f"Product(id={self.id!r}, name={self.name!r}, price={self.price!r}, stock={self.stock!r}, description={self.description!r})"
  
  def to_dict(self):
      """Return this model as a serializable Python dict."""
      return {
          "id": self.id,
          "name": self.name,
          "price": self.price,
          "stock": self.stock,
          "description": self.description,
      }
