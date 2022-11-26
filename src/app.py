from flask import Flask
from config import config
from routes import Medic, Patient

app = Flask(__name__)

def page_not_found(e):
    return "<h1>Page not found</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(Medic.medic_bp, url_prefix='/api/medic')
    app.register_blueprint(Patient.patient_bp, url_prefix='/api/patient')

    #Error handlers
    app.register_error_handler(404, page_not_found)

    app.run()