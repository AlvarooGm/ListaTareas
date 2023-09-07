from flask import (
    Blueprint,render_template,request,url_for,redirect,flash,session, g
    )
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from listar import db

bp = Blueprint('auth',__name__,url_prefix='/auth')


@bp.route('/register', methods=('GET','POST'))
def register():
    
    if request.method == 'POST':
        name = request.form['username']
        passwd= request.form['password']
        
        user = User(name,generate_password_hash(passwd))
        error = None

        user_name = User.query.filter_by(name=name).first()
        
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {name} ya existe'  
        
        flash(error) 
    
    
    return render_template('auth/register.html')

@bp.route('/login',methods =('GET','POST'))
def login():
    
    if request.method == 'POST':
        name = request.form['username']
        passwd= request.form['password']
        
       
        error = None
        #validar datos 
        user_name = User.query.filter_by(name=name).first()
        if user_name == None:
            error = 'Nombre de usuario incorrecto'  
        elif not check_password_hash(user_name.passwd,passwd):
            error = 'Contraseña incorrecta'
        
        #Inicio de sesion
        
        if error is None:
            session.clear()
            session['user_id'] = user_name.id
            return redirect(url_for('lista.index'))
        
        
        flash(error) 
    
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id =session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user=User.query.get_or_404(user_id)    
        

@bp.route('/logout')
def logout() :
    session.clear()
    return redirect(url_for('index'))       


import functools

def loginrequired(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view