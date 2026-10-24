from app import db


class JurusanMinat(db.Model):
    __tablename__ = "jurusan_minat"

    id = db.Column(db.Integer, primary_key=True)

    jurusan_id = db.Column(
        db.Integer,
        db.ForeignKey("jurusan.id"),
        nullable=False
    )

    bidang_minat_id = db.Column(
        db.Integer,
        db.ForeignKey("bidang_minat.id"),
        nullable=False
    )