from flask_login import LoginManager,UserMixin
from sqlalchemy  import create_engine, ForeignKey
from sqlalchemy.orm import Session,Mapped, mapped_column, relationship,DeclarativeBase

#cria a engine
engine = create_engine('sqlite:///database/database.db')
# cria uma sessão do sqlalchemy
# serve para executar as operações no banco, como: adicionar, selecionar, excluir e etc.
session = Session(bind=engine)

login_manager = LoginManager()


#definição da classe base
class Base(DeclarativeBase):
    pass

class User(Base, UserMixin):
    __tablename__ = 'tb_usuarios'
    usu_id:Mapped[int] = mapped_column(primary_key=True)
    usu_nome:Mapped[str]
    usu_email:Mapped[str] = mapped_column(unique=True)
    usu_senha:Mapped[str]
    # define o relacionamento 1:n entre user e livro. Retorna uma lista.
    livro = relationship('Livro', backref='user')
    def get_id(self):
        return str(self.usu_id)
    def All():
        return session.query(User).all()

class Livro(Base):
    __tablename__ = 'tb_livros'
    liv_id:Mapped[int] = mapped_column(primary_key=True)
    liv_titulo:Mapped[str]
    # define a foreign key
    liv_usu_id:Mapped[int] = mapped_column(ForeignKey('tb_usuarios.usu_id'))
    def All():
        return session.query(Livro).all()