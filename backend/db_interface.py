from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from models import Base, ProductModel
from sqlalchemy.pool import StaticPool

class DBInterface:
  def __init__(self):
    self.engine = create_engine(
      "sqlite:///:memory:", 
      echo=False,
      connect_args={"check_same_thread": False},
      poolclass=StaticPool)
    Base.metadata.create_all(self.engine)
    self.Session = sessionmaker(bind=self.engine)

  def Seed(self):
    
    with self.Session() as session:
      p1 = ProductModel(
        name="product1",
        price=55.5,
        stock=20,
        description="this is a description"
      )
      p2 = ProductModel(
        name="product2",
        price=155.5,
        stock=25,
        description="this is a description"
      )
      p3 = ProductModel(
        name="product3",
        price=5.5,
        stock=10,
        description="this is a description"
      )
      session.add_all([p1, p2, p3])
      session.commit()

  def Create(self, product: ProductModel) -> dict:
    with self.Session() as session:
      session.add(product)
      try:
        session.commit()
        return product.to_dict()
      except IntegrityError as e:
        print("Commit failed:", e)
        session.rollback() 
    return None
    
  
  def Read(self):
    resuslts = []
    with self.Session() as session:
      resuslts_test = session.query(ProductModel).all()
      for r in resuslts_test:
        resuslts.append(r.to_dict())
    return resuslts
  
  def Read_ID(self, id: int):
    resuslt = None
    with self.Session() as session:
      resuslt = session.get(ProductModel, id)
      if resuslt:
        resuslt = resuslt.to_dict()
    return resuslt

    
  def Update(self, product: ProductModel) -> dict:
    with self.Session() as session:
      p = session.get(ProductModel, product.id)
      if p is None:
        return None
      p.name = product.name
      p.price = product.price
      p.stock = product.stock
      p.description = product.description
      try:
        session.commit()
        return product.to_dict()
      except IntegrityError as e:
        print("Commit failed:", e)
        session.rollback() 
    return None
      
  def Delete(self, id: int) -> bool:
    with self.Session() as session:
      p = session.get(ProductModel, id)
      if p is None:
        return False
      session.delete(p)
      try:
        session.commit()
        return True
      except SQLAlchemyError as e:
        print("Commit failed:", e)
        session.rollback() 
        return False
