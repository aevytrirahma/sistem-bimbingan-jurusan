from app import db


class SiswaMinat(db.Model):
    __tablename__ = "siswa_minat"

    id = db.Column(db.Integer, primary_key=True)

    siswa_id = db.Column(
        db.Integer,
        db.ForeignKey("siswa.id"),
        nullable=False
    )

    bidang_minat_id = db.Column(
        db.Integer,
        db.ForeignKey("bidang_minat.id"),
        nullable=False
    )