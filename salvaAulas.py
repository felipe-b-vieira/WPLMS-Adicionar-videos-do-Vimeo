import requests
import json
import base64

#abre os arquivos com informações de videos e do usuario, a primeira linha é só infos do usuario
nomeArquivo = input("Por favor, entre com o nome do arquivo:\n")
arq = open(nomeArquivo, encoding="utf8")
infosSistema = arq.readline().split(',')

#4 infos genericas para salvar as aulas, usuario, senha do app, url para as requests api no site, e código do autor
user = 'admin'
pythonapp = infosSistema[1]
url = infosSistema[2]
autor = int(infosSistema[3])
cursoId = int(infosSistema[4])
cursoId = str(cursoId)

print(user)
#header do request
token = base64.standard_b64encode(str(user + ':' + pythonapp).encode('ascii'))
headers = {'Authorization': 'Basic ' + token.decode('utf-8'),
			'Content-Type':'application/json',
'User-Agent':'Mozilla',
'Accept':'*/*',
}

#pega as infos do curso, curriculo
courses = requests.get(url + 'course/'+cursoId,headers=headers)
cJson = courses.json()
curriculum = cJson['vibe_course_curriculum']


for aula in arq:
	infosAula = aula.split(',')
	#pega o codigo do video no vimeo
	linkSeparado = infosAula[2].split('/')
	infosAula[2] = linkSeparado[len(linkSeparado)-2]
	#post json, aqui que envia as informações, abaixo são as essenciais para a aula, mas novas podem ser adicionadas
	post = {'title': infosAula[0],
			'status': 'publish',
			'content': '[embed]https://vimeo.com/'+infosAula[2]+'/[/embed]',
			'author': autor,
			'format': 'video',
			'vibe_type' : 'play',
			'vibe_duration' : infosAula[1],
			}
	#faz o request real e adiciona a aula no site.
	print(url + 'units/')
	r = requests.post(url + 'unit/', headers=headers, json=post)
	print('Your post is published on ' + str(r.content))
	rJson = r.json()
	curriculum.append(rJson['id'])



post={
	'vibe_course_curriculum':curriculum,
}
r = requests.post(url + 'course/'+cursoId, headers=headers, json=post)
print('Your post is published on ' + str(r.content))