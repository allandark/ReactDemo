from dataclasses import dataclass

@dataclass
class Product:
  id: int
  name: str
  price: float
  stock: int
  description: str


class DBInterface:
  def __init__(self):
    self.products: list[Product] = []
    self.id_counter = 0


  def Seed(self):

    self.products = [      
      Product(
        id=0,
        name="Product0",
        price=5.5,
        stock=5,
        description="this is a description"
      ),
      Product(
        id=1,
        name="Product1",
        price=15.5,
        stock=50,
        description="this is a description"
      ),
      Product(
        id=2,
        name="Product2",
        price=25.5,
        stock=25,
        description="this is a description"
      )
    ]
    self.id_counter = 3

  def Create(self, 
             name:str, 
             price: float, 
             stock: int, 
             description: str) -> Product:
    p = Product(
      id=self.id_counter, 
      name=name,
      price=price,
      stock=stock,
      description=description)
    self.id_counter += 1
    self.products.append(p)
    return p
  
  def Read(self):
    return self.products
  
  def Read_ID(self, id: int):
    for p in self.products:
      if p.id == id:
        return p
    return None
    
  def Update(self, product: Product):
    for p in self.products:
      if p.id == product.id:
        p = product
        return p
      
  def Delete(self, id: int):
    for p in self.products:
      if p.id == id:
        self.products.remove(p)
        return True
    return False
