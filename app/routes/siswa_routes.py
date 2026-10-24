
from flask import Blueprint, request, jsonify
from app import db
from app.models.siswa import Siswa

siswa_bp = Blueprint("siswa", __name__)


@siswa_bp.route("/siswa", methods=["GET"])
def get_siswa():
    data = Siswa.query.all()

    return jsonify([
        {
            "id": siswa.id,
            "nama": siswa.nama,
            "kelas": siswa.kelas,
            "asal_sekolah": siswa.asal_sekolah
        }
        for siswa in data
    ]), 200


@siswa_bp.route("/siswa", methods=["POST"])
def tambah_siswa():
    data = request.get_json(silent=True)

    if not data or not all(
        data.get(k) for k in ["nama", "kelas", "asal_sekolah"]
    ):
        return jsonify({
            "error": "nama, kelas, dan asal_sekolah wajib diisi"
        }), 400

    siswa = Siswa(
        nama=data["nama"],
        kelas=data["kelas"],
        asal_sekolah=data["asal_sekolah"]
    )

    db.session.add(siswa)
    db.session.commit()

    return jsonify({
        "message": "Data siswa berhasil ditambahkan",
        "id": siswa.id
    }), 201


@siswa_bp.route("/siswa/<int:id>", methods=["PUT"])
def ubah_siswa(id):
    siswa = db.session.get(Siswa, id)

    if siswa is None:
        return jsonify({"error": "Siswa tidak ditemukan"}), 404

    data = request.get_json(silent=True)

    if not data or not all(
        data.get(k) for k in ["nama", "kelas", "asal_sekolah"]
    ):
        return jsonify({
            "error": "nama, kelas, dan asal_sekolah wajib diisi"
        }), 400

    siswa.nama = data["nama"]
    siswa.kelas = data["kelas"]
    siswa.asal_sekolah = data["asal_sekolah"]

    db.session.commit()

    return jsonify({"message": "Data siswa berhasil diubah"}), 200


@siswa_bp.route("/siswa/<int:id>", methods=["DELETE"])
def hapus_siswa(id):
    siswa = db.session.get(Siswa, id)

    if siswa is None:
        return jsonify({"error": "Siswa tidak ditemukan"}), 404

    db.session.delete(siswa)
    db.session.commit()

    return jsonify({"message": "Data siswa berhasil dihapus"}), 200
