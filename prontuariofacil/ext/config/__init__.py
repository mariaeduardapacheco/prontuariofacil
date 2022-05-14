from distutils.log import debug


def init_app(app):
    #app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///prontfacil.db'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://pnkqqlinhcjgdc:2d9af553c2bffbd05454883c9e902b1f9303cb099fc89724c1d85692329d1c82@ec2-107-22-238-112.compute-1.amazonaws.com:5432/d2fb59euiennat'
    app.config["SECRET_KEY"] = '123'
    app.config['FLASK_ENV'] = 'development'