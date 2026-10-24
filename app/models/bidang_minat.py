from app import db


class BidangMinat(db.Model):
    __tablename__ = "bidang_minat"

    id = db.Column(db.Integer, primary_key=True)
    nama_bidang = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.String(255))