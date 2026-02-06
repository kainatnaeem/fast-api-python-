#fast api, uvicorn

from fastapi import FastAPI
from models import Product
app = FastAPI()
@app.get("/")
def greet():
    return "Welcome to Fast API"

products = [
    Product(id = 1, name = "phone", description = "abc",price= 99, quantity= 67),
    Product(id = 2, name = "tablet", description = "abc",price= 99, quantity= 67),
    Product(id = 3, name = "laptop", description = "abc",price= 99, quantity= 67),
    Product(id = 4, name = "desktop", description = "abc",price= 99, quantity= 67)
]
@app.get("/products")
def getAllProducts():
    return products


# Get only 1 product
@app.get("/product/{id}")
def getProductbyID(id : int):
    for product in products:
        if product.id == id:
            return products[id]

    return "product not found"

# Post a product
@app.post("/product")
def addProduct(product:Product):
    products.append(product)
    return product

 #Update a product
@app.put("/product")
def updateProduct(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated successfully"
    return "no product found"      

#Delete a product

@app.delete("/product/{id}")
def deleteProduct(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "Product not found"       