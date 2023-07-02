# class representing a pizza

from dataclasses import dataclass
from typing import List, Literal, Optional

from maestro_pizza_maker.ingredients import PizzaIngredients
import numpy as np

from itertools import chain

weights_vector = {'dough':0.05, 'sauce':0.2, 'cheese':0.3, 'fruit':0.1, 'meat':0.3, 'vegetable':0.05 }

@dataclass
class Pizza:
    dough: Literal[
        PizzaIngredients.CLASSIC_DOUGH,
        PizzaIngredients.THIN_DOUGH,
        PizzaIngredients.WHOLEMEAL_DOUGH,
    ]
    sauce: Literal[PizzaIngredients.TOMATO_SAUCE, PizzaIngredients.CREAM_SAUCE]
    cheese: Optional[
        List[
            Literal[
                PizzaIngredients.MOZZARELA,
                PizzaIngredients.CHEDDAR,
                PizzaIngredients.PARMESAN,
            ]
        ]
    ] = None
    fruits: Optional[
        List[Literal[PizzaIngredients.PINEAPPLE, PizzaIngredients.APPLE]]
    ] = None
    meat: Optional[
        List[
            Literal[
                PizzaIngredients.HAM, PizzaIngredients.BACON, PizzaIngredients.SAUSAGE
            ]
        ]
    ] = None
    vegetables: Optional[
        List[
            Literal[
                PizzaIngredients.MUSHROOMS,
                PizzaIngredients.ONIONS,
                PizzaIngredients.PEPPER,
            ]
        ]
    ] = None

    def __post_init__(self) -> None:
        if self.cheese is None:
            self.cheese = []
        if self.fruits is None:
            self.fruits = []
        if self.meat is None:
            self.meat = []
        if self.vegetables is None:
            self.vegetables = []
        self.ingredients = [
            self.dough,
            self.sauce,
            *self.cheese,
            *self.fruits,
            *self.meat,
            *self.vegetables,
        ]

    @property
    def price(self) -> float:
        return sum(ingredient.value.price for ingredient in self.ingredients)

    @property
    def protein(self) -> float:
        return sum(ingredient.value.protein for ingredient in self.ingredients)

    @property
    def fat(self) -> np.array:
        return sum(ingredient.value.fat for ingredient in self.ingredients)

    @property
    def average_fat(self) -> float:
        # TODO: implement average fat calculation
        # HINT: check the `PizzaIngredients` class properly, you will find a `fat` property there which is a numpy array representing the drawings from the fat distribution
        # since fat is a random variable, we will calculate the average fat of the pizza by averaging the fat vectors of the ingredients
        fat_all_ingridients = sum(ingredient.value.fat for ingredient in self.ingredients)
        return np.mean( fat_all_ingridients )


    @property
    def carbohydrates(self) -> float:
        return sum(ingredient.value.carbohydrates for ingredient in self.ingredients)

    @property
    def calories(self) -> float:
        return sum(ingredient.value.calories for ingredient in self.ingredients)

    @property
    def name(self) -> str:
               
        pizza_name = [x.name for x in self.ingredients]
        pizza_name.sort()
        pizza_name = '_'.join(pizza_name)
        
        # TODO: implement name generation, it is purely up to you how you want to do it
        # (you can use random, you can use some kind of algorithm) - just make sure that
        # the name is unique.
        return pizza_name

    @property
    def taste(self) -> np.array:       
        
        # TODO: implement taste function
        # The famous fact that taste is subjective is not true in this case. We believe that fat is the most important factor, since fat carries the most flavor.
        # So we will use the fat vector to calculate the taste of the pizza with the following formula:
        # taste = 0.05 * fat_dough + 0.2 * fat_sauce + 0.3 * fat_cheese + 0.1 * fat_fruits + 0.3 * fat_meat + 0.05 * fat_vegetables       
          
        taste = sum(weights_vector[ingredient.value.type.value] * ingredient.value.fat for ingredient in self.ingredients)    
        return taste
