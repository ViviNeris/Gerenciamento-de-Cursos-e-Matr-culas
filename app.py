from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)
# Listas com os dicionários que são as entidades cursos, alunos e matrículas
cursos = [
    {
        'curso_id': '01',
        'curso_name': 'HMTL',
        'curso_description': 'Curso básico de HTML',
        'curso_duration':'10 horas',
        'curso_created_at':'17/02/2025',
        'curso_updated_at':'17/02/2025'
    },
    {
        'curso_id': '02',
        'curso_name': 'CSS',
        'curso_description': 'Curso básico de CSS',
        'curso_duration':'15 horas',
        'curso_created_at':'10/02/2025',
        'curso_updated_at':'17/02/2025'
    }
]
alunos = [
    {
        'aluno_id': '01',
        'aluno_name': 'Carlos Silva',
        'aluno_email': 'carlos_silva@gmail.com',
        'aluno_created_at': '15/01/2025',
        'aluno_updated_at': '17/02/2025'
    },
    {
        'aluno_id': '02',
        'aluno_name': 'Ana Souza',
        'aluno_email': 'ana_souza@gmail.com',
        'aluno_created_at': '15/12/2024',
        'aluno_updated_at': '17/02/2025'
    }
]
matriculas = [
    {
        'matricula_id': '01',
        'curso_id': '01',
        'aluno_id': '01',
        'enrollment_date': '10/02/2025'
    },
    {
        'matricula_id': '02',
        'curso_id': '02',
        'aluno_id': '02',
        'enrollment_date': '17/02/2025'
    }
]
# Classe cursos que herda 'Resource' que é um recurso da API RESTFull
class Cursos(Resource):
    def get(self): # Método GET dentro da classe 'Cursos'. 
        return {'cursos': cursos} # Retorna um dicionário com a lista de cursos quando uma solicitação GET é feita.

class Curso(Resource): # Classe Curso
    argumentos = reqparse.RequestParser() # Objeto  'RequestParser' para analisar os argumentos
    argumentos.add_argument('curso_name') # Argumentos
    argumentos.add_argument('curso_description')
    argumentos.add_argument('curso_duration')
    argumentos.add_argument('curso_created_at')
    argumentos.add_argument('curso_updated_at')

    def encontrar_curso(curso_id): #Função para encontrar o curso
        for curso in cursos: # Loop que percorre a lista de cursos
            if curso['curso_id'] == curso_id: # Se id co curso for igual ao fornecido
                return curso # Retorna o curso
        return None # Senão, não retorna nada

    def get(self, curso_id):# Método GET que têm parametros 'self'(ele mesmo) e 'curso_id
        curso = Curso.encontrar_curso(curso_id) # Chama a função ' encontrar_curso' da classe 'Curso'  
        if curso: # Se curso for encontrado
            return curso # Retornar curso
        return {'mensagem':'Curso não encontrado.'}, 404 # Senão, Not found --> Não encontrado

    def post(self, curso_id):# Método POST que têm parametros 'self'(ele mesmo) e 'curso_id
        dados = Curso.argumentos.parse_args() # Variável 'dados que analisa e valida os argumentos fornecidos usando o 'parser'
        novo_curso = { # Dicionário com informações do novo curso
            'curso_id': curso_id,
            'curso_name': dados['curso_name'],
            'curso_description': dados['curso_description'],
            'curso_duration': dados['curso_duration'],
            'curso_created_at': dados['curso_created_at'],
            'curso_updated_at': dados['curso_updated_at']
        }

        cursos.append(novo_curso) # Adiciona novo curso a lista de cursos
        return novo_curso, 200 # Código de Sucesso
        
    def put(self, curso_id): # Método PUT que têm parametros 'self'(ele mesmo) e 'curso_id
        dados = Curso.argumentos.parse_args() # Variável 'dados que analisa e valida os argumentos fornecidos usando o 'parser'
        novo_curso = { # Dicionário com informações do novo curso
            'curso_id': curso_id,
            'curso_name': dados['curso_name'],
            'curso_description': dados['curso_description'],
            'curso_duration': dados['curso_duration'],
            'curso_created_at': dados['curso_created_at'],
            'curso_updated_at': dados['curso_updated_at']
        }

        curso = Curso.encontrar_curso(curso_id) # Chama a função ' encontrar_curso' da classe 'Curso'  
        if curso: # Se curso for encontrado
            curso.update(novo_curso) # Atualiza o curso existente com as novas informações
            return novo_curso, 200 # Retorna o curso criado e o Código de Sucesso
        cursos.append(novo_curso) # Se o curso não for encontrado, adicionamos ele a nova lista de cursos.
        return novo_curso, 201 # Retorna o curso criado e o Código de Created

    def delete(self, curso_id): # Método DELETE que têm parametros 'self'(ele mesmo) e 'curso_id
        global cursos # Declarando que a variável 'cursos' é global para que seja possível mudar a lista 'cursos'
        cursos = [curso for curso in cursos if curso['curso_id'] != curso_id] # Para cada 'curso' na lista 'cursos' e, se curso for diferente de 'curso_id' mantenha-o na lista
        return{'mensagem':'Curso deletado.'} # Senão, delete o curso

# O mesmo processo acontece na classe 'Aluno'
class Alunos(Resource):
    def get(self):
        return {'alunos': alunos}

class Aluno(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('aluno_name')
    argumentos.add_argument('aluno_email')
    argumentos.add_argument('aluno_created_at')
    argumentos.add_argument('aluno_updated_at')

    def encontrar_aluno(aluno_id):
        for aluno in alunos:
            if aluno['aluno_id'] == aluno_id:
                return aluno
        return None

    def get(self, aluno_id):
        aluno = Aluno.encontrar_aluno(aluno_id)
        if aluno:
            return aluno
        return {'mensagem':'Aluno não encontrado.'}, 404 # Not found --> Não encontrado

    def post(self, aluno_id):
        dados = Aluno.argumentos.parse_args()

        novo_aluno = {
            'aluno_id': aluno_id,
            'aluno_name': dados['aluno_name'],
            'aluno_email': dados['aluno_email'],
            'aluno_created_at': dados['aluno_created_at'],
            'aluno_updated_at': dados['aluno_updated_at']
        }

        alunos.append(novo_aluno)
        return novo_aluno, 200 # Código de Sucesso

    def put(self, aluno_id):

        dados = Aluno.argumentos.parse_args()
        novo_aluno = {
            'aluno_id': aluno_id,
            'aluno_name': dados['aluno_name'],
            'aluno_email': dados['aluno_email'],
            'aluno_created_at': dados['aluno_created_at'],
            'aluno_updated_at': dados['aluno_updated_at']
        }

        aluno = Aluno.encontrar_aluno(aluno_id)
        if aluno:
            aluno.update(novo_aluno)
            return novo_aluno, 200 # Código de Sucesso
        alunos.append(novo_aluno)
        return novo_aluno, 201 # Código de Created Criado

    def delete(self, aluno_id):
        global alunos
        alunos = [aluno for aluno in alunos if aluno['aluno_id'] != aluno_id]
        return{'mensagem':'Aluno deletado.'}

# O mesmo processo acontece na classe 'Matriculas'
class Matriculas(Resource):
    def get(self):
        return {'matriculas': matriculas}

class Matricula(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('curso_id')
    argumentos.add_argument('aluno_id')
    argumentos.add_argument('enrollment_date')

    def encontrar_matricula(matricula_id):
        for matricula in matriculas:
            if matricula['matricula_id'] == matricula_id:
                return matricula
        return None

    def get(self, matricula_id):
        matricula = Matricula.encontrar_matricula(matricula_id)
        if matricula:
            return matricula
        return {'mensagem':'Matrícula não encontrada.'}, 404 # Not found --> Não encontrado

    def post(self, matricula_id):
        
        dados = Matricula.argumentos.parse_args()
        nova_matricula = {
            'matricula_id': matricula_id,
            'curso_id': dados['curso_id'],
            'aluno_id': dados['aluno_id'],
            'enrollment_date': dados['enrollment_date']
        }

        matriculas.append(nova_matricula)
        return nova_matricula, 200 # Código de Sucesso

    def put(self, matricula_id):

        dados = Matricula.argumentos.parse_args()
        nova_matricula = {
            'matricula_id': matricula_id,
            'curso_id': dados['curso_id'],
            'aluno_id': dados['aluno_id'],
            'enrollment_date': dados['enrollment_date']
        }

        matricula = Matricula.encontrar_matricula(matricula_id)
        if matricula:
            matricula.update(nova_matricula)
            return nova_matricula, 200 # Código de Sucesso
        matriculas.append(nova_matricula)
        return nova_matricula, 201 # Código de Created Criado

    def delete(self, matricula_id):
        global matriculas
        matriculas = [matricula for matricula in matriculas if matricula['matricula_id'] != matricula_id]
        return{'mensagem':'Matrícula deletada.'}

class CursoAlunos(Resource):  # Classe 'CursoAlunos' para listar alunos de um curso
    def get(self, curso_id): # Método GET que têm parametros 'self'(ele mesmo) e 'aluno_id'
        alunos_matriculados = [] # Lista vazia de alunos matriculados
        for matricula in matriculas: # Loop que percorre a lista 'matriculas'
            if matricula['curso_id'] == curso_id: # Se o ID do curso na matrícula for igual ao 'curso_id' fornecido
                aluno = Aluno.encontrar_aluno(matricula['aluno_id']) # Encontra o aluno 'aluno_id' na matricula
                if aluno: # Se o aluno for encontrado
                    alunos_matriculados.append(aluno) # Adiciona esse aluno a lista 'alunos_matriculados'
        return {'alunos': alunos_matriculados} # Retorna um dicionário com a lista de alunos matriculados no curso

    class AlunoCursos(Resource):  # Classe 'AlunoCursos' para listar cursos de um aluno
        def get(self, aluno_id): # Método GET que têm parametros 'self'(ele mesmo) e 'aluno_id'
            cursos_matriculados = [] # Lista vazia de cursos matriculados
            for matricula in matriculas: # Loop que percorre a lista 'matriculas'
                if matricula['aluno_id'] == aluno_id: # Se o ID do aluno na matrícula for igual ao 'aluno_id' fornecido
                    curso = Curso.encontrar_curso(matricula['curso_id']) # Encontra o curso 'curso_id' na matricula
                    if curso: # Se o curso for encontrado
                        cursos_matriculados.append(curso) # Adiciona esse curso a lista 'cursos_matriculados'
            return {'cursos': cursos_matriculados} # Retorna um dicionário com a lista de cursos que o aluno está matriculado  
    
# Adicionando todas as rotas
api.add_resource(Cursos, '/cursos')
api.add_resource(Curso, '/cursos/<string:curso_id>')
api.add_resource(Alunos, '/alunos')
api.add_resource(Aluno, '/alunos/<string:aluno_id>')
api.add_resource(Matriculas, '/matriculas')
api.add_resource(Matricula, '/matriculas/<string:matricula_id>')
api.add_resource(CursoAlunos, '/cursos/<string:curso_id>/alunos')  
api.add_resource(AlunoCursos, '/alunos/<string:aluno_id>/cursos')  


if __name__ == '__main__': # Se o nome for o principal (app.py), rode o programa
    app.run(debug=True) #Deixar esse debug apenas enquanto estivermos produzindo a API. Depois retiramos

    # http://127.0.0.1:5000/cursos
    # http://127.0.0.1:5000/alunos
    # http://127.0.0.1:5000/matriculas
    # C:\Users\vivia\AppData\Local\Programs\Python\Python313\python.exe app.py
