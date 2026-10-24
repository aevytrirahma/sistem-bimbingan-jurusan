from app import db


class Jurusan(db.Model):
    __tablename__ = "jurusan"

    id = db.Column(db.Integer, primary_key=True)
    nama_jurusan = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.String(255), nullable=False)
    prospek_karier = db.Column(db.String(255), nullable=True)