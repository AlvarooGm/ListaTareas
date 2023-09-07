from flask import Blueprint,render_template,request,redirect,url_for,g
from listar.auth import loginrequired
from .models import Todo,User
from listar import db


bp = Blueprint('lista',__name__,url_prefix='/lista')


@bp.route('/list')
@loginrequired
def index():
    
    todos=Todo.query.all()
    
    return render_template('lista/index.html',todos=todos)



@bp.route('/create')
@bp.route('/create', methods=('GET','POST'))
@loginrequired
def create():
    
    if request.method == 'POST':
        titu = request.form['titulo']
        desc= request.form['desc']
        
        nota = Todo(g.user.id,titu,desc)
        error = None

       
        
        
        db.session.add(nota)
        db.session.commit()
        return redirect(url_for('lista.index'))
       
        
       

    return render_template('lista/create.html')

def get_nota(id):
    nota = Todo.query.get_or_404(id)
    return nota



@bp.route('/update/<int:id>', methods=('GET','POST'))
@loginrequired
def update(id):
    nota = get_nota(id)
    if request.method == 'POST':
        nota.titulo = request.form['titulo']
        nota.desc= request.form['desc']
        nota.estado = True if request.form.get('estado') == 'on' else False
        
       
        db.session.commit()
        return redirect(url_for('lista.index'))
       
        
       

    return render_template('lista/update.html',nota=nota)


@bp.route('/delete/<int:id>', methods=('GET','POST'))
@loginrequired
def delete(id):
    
    nota = get_nota(id)
    db.session.delete(nota)
    db.session.commit()
    return redirect(url_for('lista.index'))
       
        
       

    

