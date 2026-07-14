from flask import Flask, redirect, render_template, url_for


app = Flask(__name__, template_folder="templates", static_folder="static")


@app.get("/")
def index():
    return redirect(url_for("smart_factory_dashboard"))


@app.get("/smart-factory/dashboard")
def smart_factory_dashboard():
    return render_template("smart_factory/dashboard.html", active_page="dashboard")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
