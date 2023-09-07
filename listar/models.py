from listar import db


#MODELO DE USUARIO
class User(db.Model):
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True,nullable=False)
    passwd = db.Column(db.Text,nullable=False)
    
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

    def __repr__(self):
        
        return f'<User: {self.name} > <Password: {self.passwd} >'
    
    #MODELO LISTA DE TAREAS to do CON LA FOREIGN KEY CREATED_By LA ENLAZAMOS A LA TABLA USUARIO POR EL ID
class Todo(db.Model):
    
    id = db.Column(db.Integer,primary_key=True)
    created_by = db.Column(db.Integer,db.ForeignKey('user.id'))
    titulo = db.Column(db.Text,nullable=False)
    desc= db.Column(db.Text)
    estado = db.Column(db.Boolean,default=False)
    
    def __init__(self,created_by,titulo,desc,estado=False):
        self.created_by = created_by
        self.titulo= titulo
        self.desc = desc
        self.estado = estado

    def __repr__(self):
        
        return f'<Hacer : {self.titulo} >'