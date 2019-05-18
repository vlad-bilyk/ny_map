from whitenoise import WhiteNoise

from render import app

application = WhiteNoise(app)
application.add_files('static/', prefix='static/')
