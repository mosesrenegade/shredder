from application import db

class Base(db.Model):
    __tablename__ = 'main'
    __table_args__ = { 'extend_existing': True }

    id = db.Column(db.Integer, primary_key=True)
    shell_url = db.Column(db.String())
    shell_type = db.Column(db.String())

    def __init__(self, shell_url, shell_type):
        self.shell_url = shell_url
        self.shell_type = shell_type

class Commands(db.Model):
    __tablename__ = 'commands'
    __table_args__ = {'extend_existing': True}


    id = db.Column(db.Integer, primary_key=True)
    shell_id = db.Column(db.Integer, db.ForeignKey('main.id'))
    shell_history = db.Column(db.String())

    def __init__(self, shell_id, shell_history):
        self.shell_id = shell_id
        self.shell_history = shell_history

class ShellInfo(db.Model):
    __tablename__ = 'shellinfo'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    shell_id = db.Column(db.Integer, db.ForeignKey('main.id'))
    shell_os = db.Column(db.String())
    shell_webserver_type = db.Column(db.String())
    shell_users = db.Column(db.String())
    shell_passwords = db.Column(db.String())

    def __init__(self, shell_id, shell_os, shell_webserver_type, shell_users, shell_passwords):
        self.shell_id = shell_id
        self.shell_os = shell_os
        self.shell_webserver_type = shell_webserver_type
        self.shell_users = shell_users
        self.shell_passwords = shell_passwords
