from flask import Flask
from flask.helpers import send_from_directory
from iweb.controller import RenderTemplateView
from flask.templating import render_template
from controller.toyota_controller import toyota
from iweb import iWeb
from config import Config

app = Flask(__name__)
app.register_blueprint(toyota)

app.config['db.host'] = Config.db_host
app.config['db.port'] = int(Config.db_port)
app.config['db.name'] = Config.db_name
app.config['controller.user_model'] = False
app.config['SERVER_NAME'] = 'fbcredibility.com:4040'

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT Rv]]jkojkiyd'

iweb = iWeb(app)

static_page = ['add']

for s in static_page:
    app.add_url_rule('/' + s, view_func=RenderTemplateView.as_view(s, template_name=s + '.html'))
    
@app.route('/getfile/<filename>', methods=['GET', 'POST'])
def get_file(filename):    
    return send_from_directory(directory=Config.base_path_file, filename=(filename))

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=4040, debug=True)