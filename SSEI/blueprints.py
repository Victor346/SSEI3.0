from flask import Blueprint, render_template, abort
import threading



simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

def contar():
    i = 0
    while i < 245453:
        print(i)
        i += 1
    return

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    yourThread = threading.Thread()
    try:
        return render_template('page/%s.html' % page)
    except:
        yourThread = threading.Timer(1, contar, ())
        yourThread.start()
        return 'No encontre la pagina'
