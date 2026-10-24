
from flask import Blueprint, request, jsonify
from app import db
from app.models.bidang_minat import BidangMinat

bidang_minat_bp = Blueprint("bidang_minat", __name__)


@bidang_minat_bp.route("/bidang-minat", methods=["GET"])
def get_bidang_minat():
    data = BidangMinat.query.all()
    return jsonify([
        {
            "id": b.id,
            "nama_bidang": b.nama_bidang,
            "deskripsi": b.deskripsi
        }
        for b in data
    ]), 200


@bidang_minat_bp.route("/bidang-minat", methods=["POST"])
def tambah_bidang_minat():
    data = request.get_json(silent=True)

    if not data or not data.get("nama_bidang"):
        return jsonify({
            "error": "nama_bidang wajib diisi"
        }), 400

    bidang = BidangMinat(
        nama_bidang=data["nama_bidang"],
        deskripsi=data.get("deskripsi")
    )

    db.session.add(bidang)
    db.session.commit()

    return jsonify({
        "message": "Data bidang minat berhasil ditambahkan",
        "id": bidang.id
    }), 201


@bidang_minat_bp.route("/bidang-minat/<int:id>", methods=["PUT"])
def ubah_bidang_minat(id):
    bidang = db.session.get(BidangMinat, id)

    if bidang is None:
        return jsonify({"error": "Bidang minat tidak ditemukan"}), 404

    data = request.get_json(silent=True)

    if not data or not data.get("nama_bidang"):
        return jsonify({"error": "nama_bidang wajib diisi"}), 400

    bidang.nama_bidang = data["nama_bidang"]
    bidang.deskripsi = data.get("deskripsi")

    db.session.commit()

    return jsonify({
        "message": "Data bidang minat berhasil diubah"
    }), 200


@bidang_minat_bp.route("/bidang-minat/<int:id>", methods=["DELETE"])
def hapus_bidang_minat(id):
    bidang = db.session.get(BidangMinat, id)

    if bidang is None:
        return jsonify({"error": "Bidang minat tidak ditemukan"}), 404

    db.session.delete(bidang)
    db.session.commit()

    return jsonify({
        "message": "Data bidang minat berhasil dihapus"
    }), 200
