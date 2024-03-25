import pytest

from restaurant.repository.memrepo import MemRepo
from restaurant.domain.dish import Dish

@pytest.fixture
def dish_dicts():
    return [
        {
            "position":1,
            "name":'pierogi',
            "description":'Ulubione Polskie danie ;)',
            "price":20,
        },
        {
            "position":2,
            "name":'schabowy z ziemniaczkami',
            "description":'Krolewska uczta!',
            "price":30,
        },
        {
            "position":3,
            "name":'nalesniki',
            "description":'Something sweet',
            "price":7.99,
        },
        {
            "position":4,
            "name":'pizza',
            "description":'pizza pepperoni',
            "price":5,
        },
    ]

def test_repository_list_without_parameters(dish_dicts):
    repo = MemRepo(dish_dicts)

    dishes = [Dish.from_dict(i) for i in dish_dicts]

    assert repo.list() == dishes