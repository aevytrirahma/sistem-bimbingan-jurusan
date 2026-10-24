import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Konfigurasi database
    database_url = os.environ.get(
        "DATABASE_URL",
        "sqlite:///bimbingan_jurusan.db"
    )

    # Menyesuaikan format URL PostgreSQL untuk psycopg
    if database_url.startswith("postgres://"):
        database_url = database_url.replace(
            "postgres://",
            "postgresql+psycopg://",
            1
        )
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace(
            "postgresql://",
            "postgresql+psycopg://",
            1
        )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Memuat model dan membuat tabel jika belum ada
    with app.app_context():
        from app.models.siswa import Siswa
        from app.models.jurusan import Jurusan
        from app.models.bidang_minat import BidangMinat
        from app.models.siswa_minat import SiswaMinat
        from app.models.jurusan_minat import JurusanMinat

        db.create_all()

    # Mendaftarkan route API
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
