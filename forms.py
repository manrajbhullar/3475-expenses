"""
This module defines blueprints and validation rules for any HTML forms needed in our Expense application
"""


from wtforms import Form, StringField, SelectField, FloatField, DateField, validators
from models import Expense, Category


class ExpenseForm(Form):
    name = StringField('name', [validators.Length(min=3, max=64)])
    category_id = SelectField('category_id', [validators.Length(min=24, max=24)], validate_choice=False)
    amount = FloatField('amount', [validators.NumberRange(min=0.01)])
    date = DateField('date')
    # used when editing a expense to find it from the database, ignored when making new expense
    expense_id = StringField('expense_id')


class CategoryForm(Form):
    name = StringField('name', [validators.Length(min=3, max=64)])
    # used when editing a category to find it from the database, ignored when making new category
    category_id = StringField('category_id')
