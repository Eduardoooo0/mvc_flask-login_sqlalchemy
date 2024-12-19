from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import  login_required, current_user
from models import session, Livro,User
bp = Blueprint('book', __name__, url_prefix='/books')


@bp.route('/')
@login_required
def index():
    return render_template('book/index.html', livros=Livro.All())

@bp.route('/cadastro', methods=['POST','GET'])
@login_required
def cadastro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = current_user.usu_id
        book_new = Livro(liv_titulo=titulo, liv_usu_id=autor)
        session.add(book_new)
        session.commit()
        return redirect(url_for('book.index'))
    return render_template('book/cadastro.html')