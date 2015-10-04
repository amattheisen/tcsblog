from flask.ext.wtf import Form
from flask.ext.babel import gettext
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        if self.nickname != User.make_valid_nickname(self.nickname.data):
           self.nickname.errors.append(gettext('This nickname has invalid characters. Please only use letters, numbers, dots and underscores.'))
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            return False
            self.nickname.errors.append(gettext('This nickname is already in use. Please choose another one.'))
        return True


class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])


class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])
