#!/usr/bin/env python3
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    return redirect("/index.html")

@app.get("/index.html")
def index_html():
    return render_template("index.html")

@app.get("/credits.html")
def credits():
    return render_template("credits.html")

@app.get("/maze.html")
def maze():
    return render_template("maze.html")
