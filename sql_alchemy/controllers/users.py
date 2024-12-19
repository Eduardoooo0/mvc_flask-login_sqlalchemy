from flask import Blueprint, render_template, request, redirect,url_for
from models import session, login_manager
from models import User
from sqlalchemy import select
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('user', __name__, url_prefix='/users')


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(user_id)

@auth_bp.route('/')
def index():
    return render_template('user/index.html', users=User.All())

@auth_bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = session.query(User).filter_by(usu_email=email).first()
        if user.usu_email == email and user.usu_senha == senha:
            login_user(user)
            return redirect(url_for('user.index'))
        return redirect(url_for('user.login'))
    return render_template('user/login.html')

@auth_bp.route('/cadastro', methods=['POST','GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        emails = session.execute(select(User.usu_email)).scalars().all()
        if email in emails:
            return redirect(url_for('user.index'))
        user = User(usu_nome=nome, usu_email=email,usu_senha=senha)
        session.add(user)
        session.commit()
        return redirect(url_for('user.index'))
    return render_template('user/cadastro.html')

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.index'))