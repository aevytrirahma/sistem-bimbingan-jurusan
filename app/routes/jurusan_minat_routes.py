
from flask import Blueprint, request, jsonify
from app import db
from app.models.jurusan_minat import JurusanMinat
from app.models.jurusan import Jurusan
from app.models.bidang_minat import BidangMinat

jurusan_minat_bp = Blueprint("jurusan_minat", __name__)


@jurusan_minat_bp.route("/jurusan-minat", methods=["GET"])
def get_jurusan_minat():
    data = JurusanMinat.query.all()
    return jsonify([
        {
            "id": item.id,
            "jurusan_id": item.jurusan_id,
            "bidang_minat_id": item.bidang_minat_id
        }
        for item in data
    ]), 200


@jurusan_minat_bp.route("/jurusan-minat", methods=["POST"])
def tambah_jurusan_minat():
    data = request.get_json(silent=True)

    if not data or not data.get("jurusan_id") or not data.get("bidang_minat_id"):
        return jsonify({
            "error": "jurusan_id dan bidang_minat_id wajib diisi"
        }), 400

    jurusan = db.session.get(Jurusan, data["jurusan_id"])
    bidang = db.session.get(BidangMinat, data["bidang_minat_id"])

    if jurusan is None:
        return jsonify({"error": "Jurusan tidak ditemukan"}), 404

    if bidang is None:
        return jsonify({"error": "Bidang minat tidak ditemukan"}), 404

    item = JurusanMinat(
        jurusan_id=jurusan.id,
        bidang_minat_id=bidang.id
    )

    db.session.add(item)
    db.session.commit()

    return jsonify({
        "message": "Hubungan jurusan dan bidang minat berhasil ditambahkan",
        "id": item.id
    }), 201

# Mengubah hubungan jurusan dengan bidang minat
@jurusan_minat_bp.route("/jurusan-minat/<int:id>", methods=["PUT"])
def ubah_jurusan_minat(id):
    item = db.session.get(JurusanMinat, id)

    if item is None:
        return jsonify({"error": "Data jurusan-minat tidak ditemukan"}), 404

    data = request.get_json(silent=True)

    if not data or not data.get("jurusan_id") or not data.get("bidang_minat_id"):
        return jsonify({
            "error": "jurusan_id dan bidang_minat_id wajib diisi"
        }), 400

    jurusan = db.session.get(Jurusan, data["jurusan_id"])
    bidang = db.session.get(BidangMinat, data["bidang_minat_id"])

    if jurusan is None or bidang is None:
        return jsonify({"error": "Jurusan atau bidang minat tidak ditemukan"}), 404

    item.jurusan_id = jurusan.id
    item.bidang_minat_id = bidang.id
    db.session.commit()

    return jsonify({"message": "Data jurusan-minat berhasil diubah"}), 200


# Menghapus hubungan jurusan dengan bidang minat
@jurusan_minat_bp.route("/jurusan-minat/<int:id>", methods=["DELETE"])
def hapus_jurusan_minat(id):
    item = db.session.get(JurusanMinat, id)

    if item is None:
        return jsonify({"error": "Data jurusan-minat tidak ditemukan"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Data jurusan-minat berhasil dihapus"}), 200
