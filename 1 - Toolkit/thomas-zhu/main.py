class Python2Error(ZeroDivisionError):
    # Yep, ZeroDivisionError because using python 2 is ridiculous
    pass
if __import__('sys').version_info.major == 2:
    raise Python2Error('why are you still using python 2??')

flask = __import__('flask')
# some people ask me why i use __import__ rather than import
# (and why i don't capitalize the word 'i'). this is because
# of the infamous psychological disorder with which if you
# look at sth messy it makes you more frustrating, aka. OCD
# TODO, delete the last four lines

this_is_my_own_Flask, request, send_file = (
    flask.Flask, flask.request, flask.send_file
)

requests = __import__('requests')

BeautifulSoup = __import__('bs4').BeautifulSoup


app = this_is_my_own_Flask(__name__)

grocary_LEFT_PARENTHESIS_sic_PERIOD_RIGHT_PARENTHESIS_list = [
    'foo',
    'bar',
    'chocolate bar',
    'chocolate bar that is overpriced but worse than the former one',
    'chocolate bar that is not overpriced but still expensive',
    'chocolate bar that is extremely cheap but same as the first '
    'chocolate bar because if you look closely at the barcode you\'ll find '
    'that it is a cheap Chinese knockoff',
    'etc. (this is actually the name of the last item)',
]


@app.route('/')
def function_name():
    return send_file('index.html')


@app.route('/time')
def IdontKnowHowTo_name_a_funcTion___maybe():
    time = __import__('time').localtime()
    year = str(time.tm_year).rjust(4, '0')
    mon = str(time.tm_mon).rjust(2, '0')
    day = str(time.tm_mday).rjust(2, '0')
    hour = str(time.tm_hour).rjust(2, '0')
    min_ = str(time.tm_min).rjust(2, '0')
    sec = str(time.tm_sec).rjust(2, '0')
    return year + '/' + mon + '/' + day + '/ ' \
    + hour + ':' + min_ + ':' + sec


@app.route('/weather')
def Yes_i_might_have_a_clue():
    req = requests.get('https://www.google.com.hk/search?q=weather+of+north+korea')
    soup = BeautifulSoup(req.text)
    temp, = soup.find('span', class_='wob_t')
    return 'The weather of PyongYang is ' + temp + '.' # Don't forget the period!


@app.route('/list')
def iDontKnowButApparentlyMacLeonThinksThatEveryPythonProgrammerUsesCamelcaseThatsRidiculous():
    return '<ol><li>' + '<li>'.join(grocary_LEFT_PARENTHESIS_sic_PERIOD_RIGHT_PARENTHESIS_list) + '</ol>'


@app.route('/add', methods=('GET', 'POST'))
def this_style_is_good_I_might_actually_use_it_and_I_capitalized_I_for_no_reason():
    if request.method != 'POST':
        return '跟你说了用POST <a href="/" onclick="alert(\'!SURPRISE!\')">Back to main page</a>'
    grocary_LEFT_PARENTHESIS_sic_PERIOD_RIGHT_PARENTHESIS_list.append(request.form['item'])
    return 'successfully added item ' + request.form['item']


app.run('0.0.0.0', port=8765)