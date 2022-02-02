from app.routes.register_routes import bp as bp_register
from app.routes.get_routes import bp as bp_get
from app.routes.get_with_id_routes import bp as bp_get_id

def init_app(app):
    app.register_blueprint(bp_register)
    app.register_blueprint(bp_get)
    app.register_blueprint(bp_get_id)