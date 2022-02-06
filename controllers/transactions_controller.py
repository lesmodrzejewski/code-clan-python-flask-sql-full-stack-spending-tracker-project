from flask import Flask, render_template, Blueprint, request, redirect

from models.merchant import Merchant
from models.transaction import Transaction
from models.tag import Tag

from repositories import merchant_repository
from repositories import tag_repository
from repositories import transaction_repository

transactions_blueprint = Blueprint('transactions', __name__)

@transactions_blueprint.route('/transactions')
def transactions():
    transactions = transaction_repository.select_all()
    return render_template('transactions/index.html', transactions = transactions)
