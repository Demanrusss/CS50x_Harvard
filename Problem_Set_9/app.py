import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        user_transactions = db.execute(
            "SELECT symbol, name, SUM(shares) as Shares, price, SUM(sum) as Sum FROM transactions WHERE user_id = ? GROUP BY symbol", session["user_id"])
        user_cash_list = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        user_cash = user_cash_list[0]["cash"]
        total_list = db.execute("SELECT SUM(sum) as Total FROM transactions WHERE user_id = ?", session["user_id"])
        if total_list[0]["Total"] == None:
            total_list[0]["Total"] = 0
        user_total = total_list[0]["Total"] + user_cash
        for row in user_transactions:
            row["price"] = round(row["price"], 2)
            row["Sum"] = round(row["Sum"], 2)
        return render_template("index.html", transactions_list=user_transactions, user_cash=usd(user_cash), user_total=usd(user_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares_from_form = request.form.get("shares")
        if not shares_from_form.isdigit():
            return apology("No value in Shares", 400)
        shares = int(shares_from_form)
        if not symbol or symbol == " ":
            return apology("No value in Symbol", 403)
        stocks_symbol = lookup(symbol.upper())
        if stocks_symbol == None:
            return apology("Cannot find such Symbol", 400)
        if not shares or shares < 0 or shares == 0:
            return apology("Not available number in Quantity of shares", 400)
        transaction_sum = shares * stocks_symbol["price"]
        cash_list = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash_available = cash_list[0]["cash"]
        if transaction_sum > cash_available:
            return apology("Not enough cash", 403)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_available - transaction_sum, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, sum, date, name) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   session["user_id"], stocks_symbol["symbol"], shares, stocks_symbol["price"],
                   shares * stocks_symbol["price"], datetime.datetime.now(), stocks_symbol["name"])
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        user_transactions = db.execute(
            "SELECT symbol, name, shares, price, sum, date FROM transactions WHERE user_id = ?", session["user_id"])
        return render_template("history.html", transactions_list=user_transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol or symbol == " ":
            return apology("No value in symbol", 400)
        stocks_symbol = lookup(symbol.upper())
        if stocks_symbol == None:
            return apology("Cannot find such symbol", 400)
        stocks_symbol_price = usd(stocks_symbol["price"])
        return render_template("quoted.html", stocks_symbol=stocks_symbol, price=stocks_symbol_price)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        user = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not user or user == " ":
            return apology("No value in username", 400)
        if not password or password == " ":
            return apology("No value in password", 400)
        if confirmation != password:
            return apology("Password does not confirmed properly", 400)
        password_hash = generate_password_hash(password)
        try:
            user_session = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", user, password_hash)
        except:
            return apology("Such username already exists", 400)
        session["user_id"] = user_session
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_symbols_available = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING shares > 0", session["user_id"])
        return render_template("sell.html", symbols=user_symbols_available)
    else:
        symbol = request.form.get("symbol")
        if not symbol or symbol == "Choose symbol":
            return apology("No value in Choose symbol", 403)
        shares_from_form = request.form.get("shares")
        if not shares_from_form:
            return apology("No value is shares", 400)
        shares = int(shares_from_form)
        shares_control_list = db.execute(
            "SELECT SUM(shares) as Shares FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        if not shares or shares < 0 or shares == 0 or shares > shares_control_list[0]["Shares"]:
            return apology("Not available number in Quantity of shares", 400)
        stocks_symbol = lookup(symbol)
        transaction_sum = shares * stocks_symbol["price"]
        cash_list = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash_available = cash_list[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_available + transaction_sum, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, sum, date, name) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol, shares * -1, stocks_symbol["price"], shares * stocks_symbol["price"] * -1,
                   datetime.datetime.now(), stocks_symbol["name"])
        return redirect("/")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change Password"""
    if request.method == "GET":
        return render_template("change_password.html")
    else:
        old_password = request.form.get("old_password")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not old_password or old_password == " ":
            return apology("No value in Old password", 403)
        if not password or password == " ":
            return apology("No value in Password", 403)
        if confirmation != password:
            return apology("Password does not confirmed properly", 403)
        old_password_hash = generate_password_hash(old_password)
        print(old_password_hash)
        old_password_hash_from_db = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
        print(old_password_hash_from_db)
        if not check_password_hash(old_password_hash_from_db[0]["hash"], old_password):
            return apology("Old password is incorrect", 403)
        password_hash = generate_password_hash(password)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", password_hash, session["user_id"])
        return redirect("/")
