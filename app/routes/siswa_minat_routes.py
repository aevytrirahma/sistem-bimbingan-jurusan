
from flask import Blueprint, request, jsonify
from app import db
from app.models.siswa_minat import SiswaMinat
from app.models.siswa import Siswa
from app.models.bidang_minat import BidangMinat

siswa_minat_bp = Blueprint("siswa_minat", __name__)


@siswa_minat_bp.route("/siswa-minat", methods=["GET"])
def get_siswa_minat():
    data = SiswaMinat.query.all()
    return jsonify([
        {
            "id": item.id,
            "siswa_id": item.siswa_id,
            "bidang_minat_id": item.bidang_minat_id
        }
        for item in data
    ]), 200


@siswa_minat_bp.route("/siswa-minat", methods=["POST"])
def tambah_siswa_minat():
    data = request.get_json(silent=True)

    if not data or not data.get("siswa_id") or not data.get("bidang_minat_id"):
        return jsonify({
            "error": "siswa_id dan bidang_minat_id wajib diisi"
        }), 400

    siswa = db.session.get(Siswa, data["siswa_id"])
    bidang = db.session.get(BidangMinat, data["bidang_minat_id"])

    if siswa is None:
        return jsonify({"error": "Siswa tidak ditemukan"}), 404

    if bidang is None:
        return jsonify({"error": "Bidang minat tidak ditemukan"}), 404

    item = SiswaMinat(
        siswa_id=siswa.id,
        bidang_minat_id=bidang.id
    )

    db.session.add(item)
    db.session.commit()

    return jsonify({
        "message": "Minat siswa berhasil ditambahkan",
        "id": item.id
    }), 201

# Mengubah hubungan siswa dengan bidang minat
@siswa_minat_bp.route("/siswa-minat/<int:id>", methods=["PUT"])
def ubah_siswa_minat(id):
    item = db.session.get(SiswaMinat, id)

    if item is None:
        return jsonify({"error": "Data minat siswa tidak ditemukan"}), 404

    data = request.get_json(silent=True)

    if not data or not data.get("siswa_id") or not data.get("bidang_minat_id"):
        return jsonify({
            "error": "siswa_id dan bidang_minat_id wajib diisi"
        }), 400

    siswa = db.session.get(Siswa, data["siswa_id"])
    bidang = db.session.get(BidangMinat, data["bidang_minat_id"])

    if siswa is None or bidang is None:
        return jsonify({"error": "Siswa atau bidang minat tidak ditemukan"}), 404

    item.siswa_id = siswa.id
    item.bidang_minat_id = bidang.id
    db.session.commit()

    return jsonify({"message": "Data minat siswa berhasil diubah"}), 200


# Menghapus hubungan siswa dengan bidang minat
@siswa_minat_bp.route("/siswa-minat/<int:id>", methods=["DELETE"])
def hapus_siswa_minat(id):
    item = db.session.get(SiswaMinat, id)

    if item is None:
        return jsonify({"error": "Data minat siswa tidak ditemukan"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Data minat siswa berhasil dihapus"}), 200
