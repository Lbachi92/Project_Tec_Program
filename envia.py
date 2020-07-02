import psycopg2
from bottle import route, run, request

DSN = 'dbname=cadastros user=postgres host=db'
SQL = 'INSERT INTO geositio (nome, sitio, lat, longi, descri) VALUES (%s, %s, %s, %s, %s)'

def registro_geositio(nome, sitio, lat, longi, descri):
	connecta = psycopg2.connect(DSN)
	cursosql = connecta.cursor()
	cursosql.execute(SQL, (nome, sitio, lat, longi, descri))
	connecta.commit()
	cursosql.close()

	print('Sitio Cadastrado!')

@route('/', method='POST')
def send():
	print('rota post')
	nome = request.forms.get('nome')
	sitio = request.forms.get('sitio')
	lat = request.forms.get('lat')
	longi = request.forms.get('longi')
	descri = request.forms.get('descri')

	registro_geositio(nome, sitio, lat, longi, descri)
	return 'Sitio Cadastrado: Pesquisador: {} Sitio: {} Latitude: {} Longitude: {} Descrição {}'.format(
		nome, sitio, lat, longi, descri
	)

if __name__ == '__main__':
	run(host='0.0.0.0', port=8080, debug=True)