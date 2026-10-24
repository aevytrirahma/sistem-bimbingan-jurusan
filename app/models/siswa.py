from app import db


class Siswa(db.Model):
    __tablename__ = "siswa"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kelas = db.Column(db.String(20), nullable=False)
    asal_sekolah = db.Column(db.String(100), nullable=False)