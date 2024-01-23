from sitefake import database, app

from sitefake.models import Usuario,Fotos

with app.app_context():
    database.create_all()