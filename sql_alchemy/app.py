from flask import Flask, render_template
from models import Base, Livro
from models import login_manager,engine
from controllers.users import auth_bp
from controllers.books import bp
app = Flask(__name__)

app.config['SECRET_KEY'] = 'VASCÃO'

# iniciar flask login
login_manager.init_app(app)

#cria o banco de dados
Base.metadata.create_all(bind=engine)

app.register_blueprint(auth_bp)
app.register_blueprint(bp)

@app.route('/')
def index():
    return render_template('index.html')
