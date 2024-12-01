# import the model class
from app.models.product import Product
from starlette.config import Config
import httpx, json


# Load environment variables from .env
config = Config(".env")

# A list for products
products_data = []

# initialise with data from dummyjson
def dataInitDB() :

    # use global var
    global products_data

    # data already exists
    if (products_data) :
        return True

    # Get data
    response = httpx.get(config("PRODUCT_DATA_URL"))
    data = response.json()
    products_data = data['products']

    return True

# get all products
def dataGetProducts():
    global products_data
    # force init if first time
    check_data: bool = dataInitDB()
    return products_data

# get product by id
def dataGetProduct(id: int):
    for index, product in enumerate(products_data) :
        if product['id'] == id :
            return product

    return False

def dataAddProduct(new_product):
    
    new_product.id = len(products_data) + 1
    products_data.append(new_product.dict())
    return new_product

# https://stackoverflow.com/questions/65622045/pydantic-convert-to-jsonable-dict-not-full-json-string
def dataUpdateProduct(update_product):
    for index, product in enumerate(products_data) :
        if product['id'] == update_product.id :
            products_data[index] = update_product.dict()
            return update_product

def dataDeleteProduct(id : int) :
    result : bool = False

    # find the product if it exists then delete
    for index, product in enumerate(products_data) :
        if (product['id'] == id) :
            del products_data[index]
            result = True
    
    return result