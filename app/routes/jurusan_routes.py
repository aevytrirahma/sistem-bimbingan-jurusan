
from flask import Blueprint, request, jsonify
from app import db
from app.models.jurusan import Jurusan

jurusan_bp = Blueprint("jurusan", __name__)


# Menampilkan semua data jurusan
@jurusan_bp.route("/jurusan", methods=["GET"])
def get_jurusan():
    data = Jurusan.query.all()
    return jsonify([
        {
            "id": j.id,
            "nama_jurusan": j.nama_jurusan,
            "deskripsi": j.deskripsi,
            "prospek_karier": j.prospek_karier
        }
        for j in data
    ]), 200


# Menambahkan data jurusan
@jurusan_bp.route("/jurusan", methods=["POST"])
def tambah_jurusan():
    data = request.get_json(silent=True)

    if not data or not data.get("nama_jurusan") or not data.get("deskripsi"):
        return jsonify({
            "error": "nama_jurusan dan deskripsi wajib diisi"
        }), 400

    jurusan = Jurusan(
        nama_jurusan=data["nama_jurusan"],
        deskripsi=data["deskripsi"],
        prospek_karier=data.get("prospek_karier")
    )

    db.session.add(jurusan)
    db.session.commit()

    return jsonify({
        "message": "Data jurusan berhasil ditambahkan",
        "id": jurusan.id
    }), 201


# Mengubah data jurusan
@jurusan_bp.route("/jurusan/<int:id>", methods=["PUT"])
def ubah_jurusan(id):
    jurusan = db.session.get(Jurusan, id)

    if jurusan is None:
        return jsonify({"error": "Jurusan tidak ditemukan"}), 404

    data = request.get_json(silent=True)

    if not data or not data.get("nama_jurusan") or not data.get("deskripsi"):
        return jsonify({
            "error": "nama_jurusan dan deskripsi wajib diisi"
        }), 400

    jurusan.nama_jurusan = data["nama_jurusan"]
    jurusan.deskripsi = data["deskripsi"]
    jurusan.prospek_karier = data.get("prospek_karier")

    db.session.commit()

    return jsonify({"message": "Data jurusan berhasil diubah"}), 200


# Menghapus data jurusan
@jurusan_bp.route("/jurusan/<int:id>", methods=["DELETE"])
def hapus_jurusan(id):
    jurusan = db.session.get(Jurusan, id)

    if jurusan is None:
        return jsonify({"error": "Jurusan tidak ditemukan"}), 404

    db.session.delete(jurusan)
    db.session.commit()

    return jsonify({"message": "Data jurusan berhasil dihapus"}), 200
