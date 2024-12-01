from app.data_access.product_supabase import *
from app.models.product import Product
import json

# get list of products from data
def getAllProducts() :
    products = dataGetProducts()
    return products

def getProduct(id) :
    return dataGetProduct(id)

# add new todo using data access
def newProduct(input: Product) :
    # add product (via dataaccess)
    new_product = dataAddProduct(input)

    # return new product
    return new_product

# add new todo using data access
def updateProduct(input: Product) :
    # update product
    product = dataUpdateProduct(input)

    # return updated product
    return product


def deleteProduct(id : int) :
    result = dataDeleteProduct(id)

def getProductByCat(id: int) :
    return dataGetProductByCat(id)