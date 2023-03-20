# BACKEND

## Create a proyect

@mkdir orders
@cd orders

## Create a Django Proyect with restframework

:ctrl+alt+t
:ctrl+alt+shift+t
> name: back

@python -m venv orders-env
@source orders-env/source/activate
@pip install --upgrade pip
@pip install django djangorestframework
@django-admin startproject back
@cd back
@python manage.py startapp orders

## Prepare nvim 

:ctrl+alt+t
:ctrl+alt+shift+t
> name: nvim

nvim


## Register App

Edit -> orders/back/back/settings.py

'''
INSTALLED_APPS = [
    #...
    #new_apps
    'orders',
    'rest_framework',
]
'''

## Create models in orders

Edit -> orders/back/orders/models.py

-add

from django.contrib.auth.models import User

Create class follow:

* class Color(modelos.Model):
* class Carriage(models.Model):
* class Category(models.Model):
* class Product(models.Model):
* class Client(models.Model):
* class Price_list(models.Model):
* class Line_price_list(models.Model):
* class Order(models.Model):
* class Line_order(models.Model):

## Inser the common fields:


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_customer')
    charge_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)

in the line 1- related_name is "user" + class name.

## Make Migrations and create super user


@python manage.py makemigrations
@python manage.py migrate
@mpoython manage.py createsuperuser

## Implemented JWT

create folder -> orders/back/orders/api
in api create files:
* __init__.py
* views.py
* serializers.py
* urls.py

@pip install djangorestframework-simplejwt

in -> ordes/back/back/setting add:

'''
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
'''

import:

'''

from datetime import timedelta
'''

then:

in INSTALLED_APPS add :

'''
'rest_framework_simplejwt.token_blacklist'
'''



'''
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
'''
in -> orders/back/orders/api/view.py

'''
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


'''

in -> orders/back/orders/api/urls.py

'''

from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
        path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        ]
'''

@python manage.py migrate
@python manage.py runserver

## Configure CORS

pip install django-cors-headers

in -> orders/back/back/settings.py

'''
INSTALLED_APPS = [
...
   'corsheaders',
...
]
'''


'''
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

'''

and add in settings.py

'''
CORS_ALLOW_ALL_ORIGINS = True

'''

Finish backend.

# FRONTEND


## Create a react proyect

:ctrl+alt+t
:ctrl+alt+shift+t
> name: front

@npm create vite@latest front
>React
>Javascript
@cd front
@npm install
@npm run dev

output:

'''
> front@0.0.0 dev
> vite


  VITE v4.1.4  ready in 722 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
'''


## Clean Proyect... empty

only files:

App.css
App.jsx
main.jsx

and create on sources the follow dirs:

context
pages
components
utils

then, on pages create: HomePage.jsx and LoginPage.jsx

with rafce snipped create booth class


npm install react-router-dom

in main.jsx


import {BrowserRouter} from 'react-router-dom'
...


<React.StrictMode>
   <BrowserRouter>
     <App />
   </BrowserRouter>
</React.StrictMode>,


Create file in folder "components" Header.jsx:

import React from 'react'
import { Link } from 'react-router-dom'
const Header = () => {
  return (
    <div>
      <Link to="/">Home</Link>
      <span> | </span>
      <Link to="/login">Login</Link>
    </div>
  )
}

export default Header


Create file in -> utils

PrivateRouter.jsx

import { Navigate, Outlet } from 'react-router-dom'
import React from 'react'

const PrivateRouter = ({children, ...rest}) => {
  const authenticated = false
  return authenticated ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRouter



in App.jsx 


import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import './App.css'
import HomePage from './pages/HomePage.jsx'
import LoginPage from './pages/LoginPage'
import Header from './components/Header.jsx'
import PrivateRouter from './utils/PrivateRouter.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
     <Header />
     <Routes>
          <Route exact path="/" element={<PrivateRouter />}>
            <Route element={<HomePage />} path="/" exact />
          </Route>
          <Route element={<LoginPage />} path="/login" />
      </Routes>
    </div>
  )
}


export default App
