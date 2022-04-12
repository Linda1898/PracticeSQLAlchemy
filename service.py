# Heroes and Teams are classes made by Martina saved in models in applications folder
from application.models.branch import Branch
from application.models.books import Books
from application import db

def get_all_books():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return Books.query.all()


def get_book_by_id(book_id):
    if book_id > 0:
        return Books.query.get(book_id)
    else:
        return None


def get_branch_by_id(branch_id):
    if branch_id < 100:
        return Branch.query.get(branch_id)
    else:
        return None
