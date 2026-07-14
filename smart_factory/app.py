from flask import Flask, redirect, render_template, url_for


app = Flask(__name__, template_folder="templates", static_folder="static")


@app.get("/")
def index():
    return redirect(url_for("smart_factory_dashboard"))


@app.get("/smart-factory/dashboard")
def smart_factory_dashboard():
    return render_template("smart_factory/dashboard.html", active_page="dashboard")


@app.get("/smart-factory/quality")
def smart_factory_quality():
    return render_template("smart_factory/quality.html", active_page="quality")


@app.get("/smart-factory/equipment")
def smart_factory_equipment():
    return render_template("smart_factory/equipment.html", active_page="equipment")


@app.get("/smart-factory/reports")
def smart_factory_reports():
    return render_template("smart_factory/reports.html", active_page="reports")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
