from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    up_image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png'])])

