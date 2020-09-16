from flask import render_template, Flask

app = Flask(__name__, static_folder='static/')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/dash/videos')
def upload():
    context = {
        'uploading_title': 'V A  SHIVA   Dr SHIVA LIVE MIT PhD Analysis of Michigan Votes Reveals Unfortunate Truth of US Voti',
        'uploading_filename': 'V A  SHIVA   Dr SHIVA LIVE MIT PhD Analysis of Michigan Votes Reveals Unfortunate Truth of US Voting.mp4',
    }
    return render_template('upload.html', **context)


@app.route('/dash/customise')
def customise():
    return render_template('customise.html')


@app.route('/dash/monetisation')
def monetisation():
    return render_template('dash_monetisation.html')


@app.route('/dash/sync')
def sync():
    return render_template('sync.html')


@app.route('/dash/sync-blank')
def sync_blank():
    return render_template('sync-blank.html')


@app.route('/dash/')
def dash_overview():
    return render_template('dash_overview.html')


@app.route('/dash/blank')
def dash_overview_blank():
    return render_template('dash_overview-blank.html')


@app.route('/channel')
def channel():
    return render_template('channel.html')


@app.route('/channel/blank')
def channel_blank():
    return render_template('channel_blank.html')
