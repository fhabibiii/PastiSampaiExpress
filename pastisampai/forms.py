from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,SelectField,PasswordField,IntegerField
from wtforms.validators import Length,DataRequired,ValidationError,Email
from pastisampai.models import get_city,search_user,search_noresi

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = search_user(username_to_check.data)
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    def validate_email(self,email_to_check):
        user = search_user(email_to_check.data)
        if user:
            raise ValidationError('Email already exists! Please try a different Email')
    fullname = StringField(label='full name',validators=[Length(min=2, max=30), DataRequired()])
    username = StringField(label = 'username',validators=[Length(min=2,max=30),DataRequired()])
    email = StringField(label = "email",validators=[Email(),DataRequired()])
    password = PasswordField(label = 'Password',validators = [Length(min=2,max=30),DataRequired()])
    submit = SubmitField(label="register")

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class addNewOrder(FlaskForm):
    def validate_kota_asal(self,kota_asal_to_check):
        if kota_asal_to_check.data == 'default':
            raise ValidationError('Kota asal harus diisi!')
    def validate_kota_tujuan(self,kota_tujuan_to_check):
        if kota_tujuan_to_check.data == 'default':
            raise ValidationError('Kota tujuan harus diisi!')
    sender_n = StringField(label = 'Nama Pengirim',validators=[DataRequired(),Length(max=30)])
    receiver_n = StringField(label = 'Nama Penerima',validators=[DataRequired(),Length(max=30)])
    origin_n = StringField(label = 'Alamat Asal',validators=[DataRequired(),Length(max=30)])
    type_of_packet = StringField(label = 'Tipe Paket',validators=[DataRequired(),Length(max=30)])
    type_of_service = SelectField(choices=['Jenis Layanan','Reguler','Ekonomi','Kargo'])
    sender_pn = IntegerField(validators=[DataRequired()])
    receiver_pn = IntegerField(validators=[DataRequired()])
    destination_n = StringField(label = 'Alamat Penerima',validators=[DataRequired(),Length(max=30)])
    weight_packet = StringField(validators=[DataRequired()])
    kota_asal = SelectField(label='Kota Asal',choices = get_city())
    kota_tujuan = SelectField(label='Kota Asal',choices = get_city())
    submit = SubmitField()

class addUsername(FlaskForm):
    def validate_username_r(self,username_r_to_check):
        username = search_user(username_r_to_check.data)
        if not username:
            raise ValidationError('Username of receiver doesnt exists!')
    def validate_username_d(self,username_d_to_check):
        username = search_user(username_d_to_check.data)
        if not username:
            raise ValidationError('Username of deliver doesnt exists!')
    username_r = StringField(label = 'Nama Penerima',validators=[DataRequired(),Length(max=30)])
    username_d = StringField(label = 'Nama Pengirim',validators=[DataRequired(),Length(max=30)])
    no_resi = IntegerField()
    submit = SubmitField()

class updateResiForm(FlaskForm):
    def validate_noresi(self,noresi_to_check):
        noresi = search_noresi(noresi_to_check.data)
        if not noresi:
            raise ValidationError('No resi yang anda masukkan salah!')
    noresi = IntegerField(label='No Resi',validators=[DataRequired()])
    tanggal = StringField(label = 'Tanggal',validators=[DataRequired(),Length(max=30)])
    arrived_at = StringField(label='Lokasi Terkini',validators=[DataRequired(),Length(max=30)])
    submit= SubmitField()

class dropPointForm(FlaskForm):
    searchCity = StringField(label='Masukkan nama kota',validators=[DataRequired(),Length(max=30)])
    submit = SubmitField()

class checkResiForm(FlaskForm):
    noresi = IntegerField(label='No Resi',validators=[DataRequired()])
    submit = SubmitField()