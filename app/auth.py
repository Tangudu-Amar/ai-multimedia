from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import re
from .database import get_db_connection  # Note the relative import

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        if conn is None:
            flash("⚠ Cannot connect to the database. Try again later.")
            return redirect(url_for('auth_bp.login'))

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            conn.close()

            if user and check_password_hash(user['password'], password):
                session['username'] = username
                return redirect(url_for('analysis_bp.index'))  # Redirect to the main app page
            elif not user:
                flash("User doesn't exist. Please sign up.")
                return redirect(url_for('auth_bp.signup'))
            else:
                flash("Incorrect password.")
                return redirect(url_for('auth_bp.login'))

        except Exception as e:
            print("❌ Login DB error:", e)
            flash("⚠ Something went wrong during login.")
            return redirect(url_for('auth_bp.login'))

    return render_template('login.html')


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        raw_password = request.form["password"]

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'
        if not re.match(pattern, raw_password):
            flash("❌ Password must be 8–16 characters, include 1 number, 1 uppercase, 1 lowercase, and 1 special symbol.")
            return redirect(url_for("auth_bp.signup"))

        password = generate_password_hash(raw_password)

        conn = get_db_connection()
        if conn is None:
            flash("⚠ Cannot connect to the database. Try again later.")
            return redirect(url_for('auth_bp.signup'))

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash("⚠ Username already exists.")
                return redirect(url_for("auth_bp.signup"))

            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            conn.close()

            flash("✅ Signup successful. You can now log in.")
            return redirect(url_for("auth_bp.login"))

        except Exception as e:
            print("❌ Signup DB error:", e)
            flash("⚠ An error occurred during signup.")
            return redirect(url_for("auth_bp.signup"))

    return render_template("signup.html")

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    flash("✅ Logged out successfully.")
    return redirect(url_for('auth_bp.login'))