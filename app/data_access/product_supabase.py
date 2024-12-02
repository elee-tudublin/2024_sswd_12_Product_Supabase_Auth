# import the model class
from app.models.product import Product
from starlette.config import Config
from supabase import create_client, Client

import json


# Load environment variables from .env
config = Config(".env")

db_url: str = config("SUPABASE_URL")
db_key: str = config("SUPABASE_KEY")

supabase: Client = create_client(db_url, db_key)


# get all products
def dataGetProducts():
    response = (supabase.table("product")
                .select("*, category(name)")
                .order("title", desc=False)
                .execute()
    )
    return response.data


def dataGetProductByCat(id: int) :
    response = (supabase.table("product")
                .select("*, category(name)")
                .eq("category_id", id)
                .order("title", desc=False)
                .execute()
    )
    return response.data
    

# get product by id
def dataGetProduct(id):
    # select * from product where id = id 
    response = (
        supabase.table("product")
        .select("*, category(name)")
        .eq("id", id)
        .execute()
    )
    return response.data[0]

# update product
def dataUpdateProduct(product: Product) :
    # pass params individually
    #response = supabase.table("product").upsert({"id": product.id, "category_id": product.category_id, "title": product.title, "thumbnail": product.thumbnail, "stock": product.stock, "price": product.price}).execute()
    response = (
        supabase.table("product")
        .upsert(product.model_dump()) # convert product object to dict - required by Supabase
        .execute()
    )
    # result is 1st item in the list
    return response.data[0]

# add product, accepts product object
def dataAddProduct(product: Product, accessToken, refreshToken) :

    supabase.auth.set_session(accessToken, refreshToken)

    response = (
        supabase
        .table("product")
        .insert(product.model_dump()) # convert product object to dict - required by Supabase
        .execute()
    )

    if (response.data) :
        return dataGetProduct(response.data[0]['id'])

    return False

# get all categories
def dataGetCategories():
    response = (supabase.table("category")
                .select("*")
                .order("name", desc=False)
                .execute()
    )

    return response.data


# delete product by id
def dataDeleteProduct(id):
    # select * from product where id = id 
    response = (
        supabase.table("product")
        .delete()
        .eq('id', id)
        .execute()
    )
    return response.data


# Supabase Auth for Python https://supabase.com/docs/reference/python/auth-api

# register new user
def dataUserRegister(user):
    response = supabase.auth.sign_up(user.model_dump())
    return response

# Login
def dataUserLogin(user):
    response = supabase.auth.sign_in_with_password(user.model_dump())
    return response

#Logout
def dataLogout():
    response = supabase.auth.sign_out()
    return "success"

# Get Session
def dataGetUserSession():
    response = supabase.auth.get_session()
    return response
