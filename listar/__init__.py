from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    
    app = Flask(__name__)
    
    #config proyecto
    app.config.from_mapping(
        
        SECRET_KEY = 'dev',
        DEBUG   = True,
        SQLALCHEMY_DATABASE_URI = "sqlite:///ejerNotas.db"
        
    )
    
    db.init_app(app)
    
    
    #registro blueprint
    from . import lista
    app.register_blueprint(lista.bp)
    
    
    from . import auth
    app.register_blueprint(auth.bp)
    
   
    @app.route('/')
    def index():
        return render_template('index.html')
    
    
    #PARA MIGRAR TODOS LOS MODELOS QUE FALTEN
    with app.app_context():
        db.create_all()

    return app

