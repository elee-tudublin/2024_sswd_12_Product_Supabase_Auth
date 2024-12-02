from app.data_access.product_supabase import *
from app.models.user import User
import json

# register a new user
def userRegister(user: User) :
    response = dataUserRegister(user)
    return response

# Login a user
def userLogin(user: User) :
    response = dataUserLogin(user)
    return response

# Logout
def logout() :
    return dataLogout()

# Get session
def getSession() :
    return dataGetUserSession()