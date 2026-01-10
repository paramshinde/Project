from flask import Flask, render_template, request, redirect, session, url_for
from dotenv import load_dotenv
import os
from contrib_engine import run_contribution


# LOAD ENV VARIABLES
load_dotenv()

app = Flask(__name__)

# CONFIG
app.secret_key = os.getenv("SECRET_KEY")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

# DEBUG (remove later)
print("Loaded ADMIN_PASSWORD:", ADMIN_PASSWORD)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entered_password = request.form.get("password")

        if entered_password == ADMIN_PASSWORD:
            session["auth"] = True
            return redirect(url_for("dashboard"))
        else:
            return render_template(
                "login.html",
                error="❌ Incorrect password"
            )

    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if not session.get("auth"):
        return redirect(url_for("login"))

    message = None

    if request.method == "POST":
        level = request.form.get("level")

        commits = run_contribution(
            level=level,
            repo_path=os.getenv("REPO_PATH")
        )

        message = f"✅ {commits} commits pushed ({level.capitalize()})"

    return render_template("dashboard.html", message=message)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
