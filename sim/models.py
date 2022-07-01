from datetime import datetime
from sim import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(mahasiswa_id):
    return Tmahasiswa.query.get(int(mahasiswa_id))


class Tmahasiswa(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    npm = db.Column(db.String(15), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    kelas = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(30), nullable=False, default='default.jpg')
    pengaduans = db.relationship('Tpengaduan', backref='mahasiswa')
    pendataans = db.relationship('Tpendataansurat', backref='pmahasiswa')

    def __repr__(self):
        return f"Tmahasiswa('{self.npm}','{self.nama}','{self.email}','{self.password}','{self.kelas}','{self.alamat}','{self.foto}')"


class Tpengaduan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subjek = db.Column(db.String(100), nullable=False)
    kategori = db.Column(db.String(50), nullable=False)
    detail_pengaduan = db.Column(db.String(300), nullable=False)
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mahasiswa_id = db.Column(db.Integer, db.ForeignKey('tmahasiswa.id'))

    def __repr__(self):
        return f"Tpengaduan('{self.subjek}','{self.kategori}','{self.detail_pengaduan}','{self.tgl_post}')"


#Tpendataansurat
class Tpendataansurat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomor_surat = db.Column(db.String(100), nullable=False)
    jenis_surat = db.Column(db.String(50), nullable=False)
    perihal = db.Column(db.String(100), nullable=False)
    sifat_surat= db.Column(db.String(20), nullable=False)
    nama_instansi = db.Column(db.String(20), nullable=False)
    tgl_surat = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mahasiswaid = db.Column(db.Integer, db.ForeignKey('tmahasiswa.id'))

    def __repr__(self):
        return f"Tpendataansurat('{self.nomor_surat}',('{self.nomor_surat}','{self.perihal}','{self.sifat_surat}','{self.nama_instansi}','{self.tgl_surat}')"