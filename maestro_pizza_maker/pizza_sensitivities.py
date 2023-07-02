# The maestro pizza maker wants to fully understand of the properties of his pizza menu.
# Therefore he defines the follwing variables in the pizza industry known as "pizza sensitivities":
# 1. menu_sensitivity_protein - represents the rate of change between the price of the pizza and the amount of protein in the pizza
# 2. menu_sensitivity_carbs - represents the rate of change between the price of the pizza and the amount of carbohydrates in the pizza
# 3. menu_sensitivity_fat - represents the rate of change between the price of the pizza and the amount of average_fat in the pizza

# TODO: implement above mentioned sensitivities
# hint: simple linear regression might be helpful

from maestro_pizza_maker.pizza_menu import PizzaMenu
from sklearn import linear_model
import numpy as np


def menu_sensitivity_protein(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    reg = linear_model.LinearRegression()
    X = np.array([pizza.protein for pizza in menu.pizzas]).reshape(-1,1)
    y = np.array([pizza.price for pizza in menu.pizzas])
    reg.fit(X, y)
    return reg.coef_[0]


def menu_sensitivity_carbs(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    reg = linear_model.LinearRegression()
    X = np.array([pizza.carbohydrates for pizza in menu.pizzas]).reshape(-1,1)
    y = np.array([pizza.price for pizza in menu.pizzas])
    reg.fit(X, y)
    return reg.coef_[0]


def menu_sensitivity_fat(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    reg = linear_model.LinearRegression()
    X = np.array([pizza.average_fat for pizza in menu.pizzas]).reshape(-1,1)
    y = np.array([pizza.price for pizza in menu.pizzas])
    reg.fit(X, y)
    return reg.coef_[0]


# In case you expected to see a method which makes certain that we will be able to rebuild the world after a doomsday :-)
# you would calc the estimators for the parameters from minimization of the objective function ( least squares )
# F( \beta_0, \beta_1) = sum_n ( y_i - \beta_0 - beta_1 x_i)**2
# with minimization equation in \beta_0, and \beta_1 leading to
# beta_0 = \overline( y ) - \beta_1 \overline(x)
# beta_1 = \frac{\sum_i (y_i - \overlay(y))( x_i -\overly(x))}{  (x_i-\overlay(x))²}

def menu_sensitivity_rate( menu: PizzaMenu, sensitivity_var:str ) -> float:
    
    # Get the variables from the menu
    y = np.array([ getattr( pizza, 'price' ) for pizza in menu.pizzas ])
    x = np.array([ getattr( pizza,  sensitivity_var ) for pizza in menu.pizzas ]).reshape(-1, 1)
    
    T1 = np.sum((y-np.mean(y)).reshape(-1,1)*(x-np.mean(x)))
    T2 = np.sum((x-np.mean(x))**2)
    return T1/T2


def menu_sensitivity( menu: PizzaMenu , vars:list ) -> float:
    #TODO: Nice2have all 3 in one function with possibility to regress 
    # on each separately or combinations of the input regressors
    pass

