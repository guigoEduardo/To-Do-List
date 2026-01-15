
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# App e Configurações

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models

class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    tasks = db.relationship(
        'Todo',
        backref='category_rel',
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Category {self.name}>"


class Todo(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='Pendente')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"<Todo {self.content[:20]}>"

# Rotas Principais

@app.route('/', methods=['GET'])
def index():
    sort_by = request.args.get('sort', 'date_created')
    filter_cat = request.args.get('filter')

    query = Todo.query

    # Filtro por categoria
    if filter_cat and filter_cat != 'Todas':
        query = query.join(Category).filter(Category.name == filter_cat)

    # Ordenação
    if sort_by == 'content':
        tasks = query.order_by(Todo.content.asc()).all()
    else:
        tasks = query.order_by(Todo.date_created.desc()).all()

    categories = Category.query.all()

    return render_template('index.html', tasks=tasks, categories=categories)

# CRUD de Tarefas

@app.route('/add_task', methods=['POST'])
def add_task():
    content = request.form.get('content')
    category_id = request.form.get('category_id')

    if not content or not category_id:
        return redirect(url_for('index'))

    new_task = Todo(content=content, category_id=category_id)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/complete/<int:id>')
def complete(id):
    task = Todo.query.get_or_404(id)
    task.status = 'Concluído' if task.status == 'Pendente' else 'Pendente'
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    task = Todo.query.get_or_404(id)
    new_content = request.form.get('content')

    if new_content:
        task.content = new_content
        db.session.commit()

    return redirect(url_for('index'))

# CRUD de Categoria

@app.route('/add_category', methods=['POST'])
def add_category():
    name = request.form.get('cat_name')

    if name and not Category.query.filter_by(name=name).first():
        db.session.add(Category(name=name))
        db.session.commit()

    return redirect(url_for('index'))

# Inicialização

def create_default_categories():
    default = ['Estudo', 'Trabalho', 'Pessoal']
    existing = {cat.name for cat in Category.query.all()}

    for cat in default:
        if cat not in existing:
            db.session.add(Category(name=cat))

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_default_categories()

    app.run(debug=True)
