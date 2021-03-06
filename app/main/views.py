from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import PitchForm, CommentForm, Vote
from ..models import User, Pitch, Comment
from flask_login import login_required, current_user
from .. import db, photos


@main.route('/')
def index():
    '''
    Function that renders the index.html and its functions
    '''
    pitches = Pitch.query.all()

    return render_template('index.html', pitches=pitches)

@main.route('/')
def wired():
    '''
    function that renders the category wired and its functions
    '''
    wired_pitch = Pitch.query.filter_by(category='wired').all()

    return render_template('wired.html', wired=wired_pitch)

@main.route('/')
def business():
    '''
    function that renders the category wired and its functions
    '''
    business_pitch = Pitch.query.filter_by(category='wired').all()

    return render_template('business.html', business=business_pitch)


@main.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        body = pitch_form.body.data
        author = pitch_form.author.data
        category = pitch_form.category.data

        new_pitch = Pitch(title=title, body=body, author=author, category=category, upvotes=0, downvotes=0, users=current_user)
        new_pitch.save_pitches()
        return redirect(url_for('main.index'))

    return render_template('new.html', pitch_form=pitch_form)

@main.route('/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentForm()
    vote_radio = Vote()
    pitch = Pitch.query.get(id)
    if comment_form.validate_on_submit():
        title = comment_form.title.data
        comment = comment_form.comment.data

        new_comment = Comment(comment=comment,title=title,user=current_user)
        new_comment.save_comment()
        return redirect(url_for('main.index'))


    return render_template('comment.html',comment_form=comment_form,pitch=pitch,vote_radio=vote_radio)

# @main.route('/update', methods=['POST'])
# def update():
#     pitch = Pitch.query.get(id)
#     pitch.upvotes = request.args.get('jsdata')
#     pitch.downvotes = request.args.get('jsdata')

#     return render_template('button.html', pitch=pitch)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    '''
    Function rendering the profile page for our user
    '''
    user = User.query.filter_by(username=uname).first()


    if user is None:
        abort(404)

    return render_template('profile/profile.html', user=user)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))