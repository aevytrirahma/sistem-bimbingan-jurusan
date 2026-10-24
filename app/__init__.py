
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///bimbingan_jurusan.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        from app.models.siswa import Siswa
        from app.models.jurusan import Jurusan
        from app.models.bidang_minat import BidangMinat
        from app.models.siswa_minat import SiswaMinat
        from app.models.jurusan_minat import JurusanMinat

        db.create_all()

    from app.routes.siswa_routes import siswa_bp
    from app.routes.jurusan_routes import jurusan_bp
    from app.routes.bidang_minat_routes import bidang_minat_bp
    from app.routes.siswa_minat_routes import siswa_minat_bp
    from app.routes.jurusan_minat_routes import jurusan_minat_bp
    app.register_blueprint(siswa_bp)
    app.register_blueprint(jurusan_bp)
    app.register_blueprint(bidang_minat_bp)
    app.register_blueprint(siswa_minat_bp)
    app.register_blueprint(jurusan_minat_bp)

    @app.route("/")
    def home():
        return jsonify({
            "status": "success",
            "message": "API Bimbingan Jurusan berhasil dijalankan!"
        })

    return app
