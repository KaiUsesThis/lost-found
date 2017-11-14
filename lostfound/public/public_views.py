from flask import Blueprint, render_template, abort, session, redirect, url_for
from jinja2 import TemplateNotFound

mod = Blueprint('public_views', __name__)

@mod.route('/')
def show():
	if 'email' in session: 
		return redirect(url_for("item_views.dashboard"))
	return render_template('public/index.html')

@mod.route('/about')
def about():
	return render_template('public/about.html')

@mod.route('/contact')
def contact():
	return render_template('public/contact.html')

