from bottle import route, run, debug


@route('/login')
def Login():
	print('step in server')
	return 'Hello Orca'
debug(True)
run()