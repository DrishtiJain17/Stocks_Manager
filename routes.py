from flask import Blueprint, request, render_template, redirect, url_for, flash,session
from models import Stock, User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user

stock_routes = Blueprint('stock_routes', __name__)
user_routes = Blueprint('user_routes', __name__)

@stock_routes.route('/')
def index():
    return render_template('index.html')

@stock_routes.route('/aboutstockify')
def aboutstockify():
    return render_template('aboutstockify.html')


@stock_routes.route('/add_stock', methods=['GET','POST'])
@login_required
def add_stock():
    if request.method == "POST":
        data = request.form
        if data['name']=='' or data['ticker_symbol']=='' or data['price']=='':
                message="Please fill all details of the book"
                flash(message,"info")
                return redirect(url_for('add_stock'))
        new_stock = Stock(
            name=data['name'],
            ticker_symbol=data['ticker_symbol'],
            price=float(data['price'])
        )
        db.session.add(new_stock)
        db.session.commit()
        message = "Stock Added successfully"
        flash(message,"info")
        return redirect(url_for('stock_routes.home', message=message))
    return render_template("add_stock.html")

@stock_routes.route('/editstock/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_stock(id):
    stockinfo = Stock.query.get_or_404(id)
    if request.method == 'POST':
        stockinfo.name = request.form['name']
        stockinfo.price = float(request.form['price'])
        db.session.commit()
        message = "Stock Updated successfully"
        flash(message,"info")
        return redirect(url_for('stock_routes.home', ))
    return render_template("edit_stock.html",stockinfo=stockinfo)

@stock_routes.route('/stocks/<int:id>/delete', methods=['GET','POST'])
@login_required
def delete_stock(id):
    if request.method == 'POST':
        stock = Stock.query.get_or_404(id)
        if stock: 
            db.session.delete(stock)
            db.session.commit()
            message = "Stock Deleted successfully"
            flash(message,"info")
            return redirect(url_for('stock_routes.home', message=message))
    message = "Stock was not found"
    flash(message,"info")
    return redirect(url_for('stock_routes.home', message=message))

@user_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        # name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash('Email is already registered.', 'danger')
            return redirect(url_for('user_routes.register'))

        # Create a new user and hash the password
        new_user = User(name="user1", email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('user_routes.login'))

    return render_template('register.html')


@user_routes.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        
        # Query for the user
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            # Log the user in and store their ID in the session
            login_user(user)
            return redirect(url_for('stock_routes.home'))
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('user_routes.login'))
    return render_template('login.html')    

@stock_routes.route('/dashboard')
@login_required
def home():
    stocks = Stock.query.all()
    page = request.args.get('page', 1, type=int)
    per_page = 5  # Number of stocks per page
    pagination = Stock.query.paginate(page=page, per_page=per_page, error_out=False)
    stocks = pagination.items
    return render_template('userdashboard.html', stocks=stocks, pagination=pagination)

@user_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('user_routes.login'))
