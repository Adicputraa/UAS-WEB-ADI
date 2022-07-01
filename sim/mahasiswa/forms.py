import email
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sim.models import Tmahasiswa
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed



class mahasiswa_F(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired()])
    npm = StringField('NPM', validators=[
                      DataRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    kelas = StringField('Kelas', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    kon_pass = PasswordField('Konfirmasi Password', validators=[
                             DataRequired(), EqualTo('password')])
    alamat = TextAreaField('Alamat', validators=[DataRequired()])
    submit = SubmitField('Registrasi')

    #cek npm
    def validate_npm(self, npm):
        ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
        if ceknpm:
            raise ValidationError('NPM Sudah Terdaftar, Gunaka NPM Yang Lain!')

    #cek email
    def validate_email(self, email):
        cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError('Email Sudah Terdaftar, Gunaka Email Yang Lain')


class loginmahasiswa_F(FlaskForm):
    npm = StringField('NPM', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class editmahasiswa_F(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired()])
    npm = StringField('NPM', validators=[
                      DataRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    kelas = StringField('Kelas', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    kon_pass = PasswordField('Konfirmasi Password', validators=[
                             DataRequired(), EqualTo('password')])
    alamat = TextAreaField('Alamat', validators=[DataRequired()])
    foto= FileField('Ubah Foto Profil', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Ubah Data')

    #cek npm
    def validate_npm(self, npm):
        if npm.data != current_user.npm:
            ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
            if ceknpm:
                raise ValidationError('NPM Sudah Terdaftar, Gunaka NPM Yang Lain!')

    #cek email
    def validate_email(self, email):
        if email.data != current_user.email:
            cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
            if cekemail:
                raise ValidationError('Email Sudah Terdaftar, Gunaka Email Yang Lain')

class pengaduan_F(FlaskForm):
    subjek = StringField('Subjek', validators=[DataRequired()])
    kategori = SelectField(u'Kategori Pengaduan', choices=[('administrasi','Pelayanan Administrasi'), ('fasilitas','Fasilitas'), ('dosen','Dosen')],  validators=[DataRequired()])
    detail_pengaduan = TextAreaField('Pengaduan', validators=[DataRequired()])
    submit = SubmitField('Kirim')
    

class editpengaduan_F(FlaskForm):
    subjek = StringField('Subjek', validators=[DataRequired()])
    kategori = SelectField(u'Kategori Pengaduan', choices=[('administrasi','Pelayanan Administrasi'), ('fasilitas','Fasilitas'), ('dosen','Dosen')],  validators=[DataRequired()])
    detail_pengaduan = TextAreaField('Pengaduan', validators=[DataRequired()])
    submit = SubmitField('Ubah')
#surat
class surat_F(FlaskForm):
    nomor_surat = StringField('Nomor Surat', validators=[DataRequired()])
    jenis_surat = SelectField(u'Jenis Surat', choices=[('surat masuk','Surat Masuk'), ('surat keluar','Surat Keluar')],  validators=[DataRequired()])
    perihal = TextAreaField('Perihal', validators=[DataRequired()])
    sifat_surat = SelectField('Sifat Surat', choices=[('surat resmi','Surat Resmi'), ('surat tidak resmi','Surat Tidak Resmi')],  validators=[DataRequired()])
    nama_instansi = StringField('Nama Instansi', validators=[DataRequired()])
    submit = SubmitField('Kirim')

class editsurat_F(FlaskForm):
    nomor_surat = StringField('Nomor Surat', validators=[DataRequired()])
    jenis_surat = SelectField(u'Jenis Surat', choices=[('surat masuk','Surat Masuk'), ('surat keluar','Surat Keluar')],  validators=[DataRequired()])
    perihal = TextAreaField('Perihal', validators=[DataRequired()])
    sifat_surat = SelectField('Sifat Surat', choices=[('surat resmi','Surat Resmi'), ('surat tidak resmi','Surat Tidak Resmi')],  validators=[DataRequired()])
    nama_instansi = StringField('Nama Instansu', validators=[DataRequired()])
    submit = SubmitField('Ubah')