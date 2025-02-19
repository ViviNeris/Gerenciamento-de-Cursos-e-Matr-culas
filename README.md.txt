Projeto: Sistema de Gerenciamento de Cursos e Matrículas

API RESTful para um sistema de gerenciamento de
cursos e matrículas. A API permite o cadastro de cursos, alunos e matrículas, além de
fornecer funcionalidades para consultar e gerenciar esses dados. Entidades, funcionalidades e validações conforme orientado no teste técnico Back End

Softwares:
Python 3.13.2 - Link para download: https://www.python.org/downloads/
Postman 9.4 - Link para download: https://www.postman.com/downloads/
Dependências do projeto - listadas no arquivo requirements.txt
Editor de Código - Visual Studio Code

Instruções de Instalação:
1. Clone o repositório:
git clone [https://github.com/ViviNeris/Gerenciamento-de-Cursos-e-Matr-culas.git](https://github.com/ViviNeris/Gerenciamento-de-Cursos-e-Matr-culas.git)

2. Acesse a pasta do projeto:
cd Gerenciamento-de-Cursos-e-Matr-culas

3. Crie um ambiente virtual:
python3 -m venv venv

4. Ative o ambiente virtual:
Para Windows:
venv\Scripts\activate

Para Linux Linux/macOS:
source venv/bin/activate

5. Instale as dependências:
pip install -r requirements.txt

Instruções de Execução:

1. Inicie a API:
python app.py

2. A API estará disponível em `http://127.0.0.1:5000`.

Instruções de Teste:
Exemplos de Uso:

* **Listar todos os cursos:**
    * Método: GET
    * URL: 'http://127.0.0.1:5000/cursos'
    * Resposta esperada:
    [
        {
            "curso_id": "01",
            "curso_name": "HMTL",
            "curso_description": "Curso básico de HTML",
            "curso_duration": "10 horas",
            "curso_created_at": "17/02/2025",
            "curso_updated_at": "17/02/2025"
        },
        {
            "curso_id": "02",
            "curso_name": "CSS",
            "curso_description": "Curso básico de CSS",
            "curso_duration": "15 horas",
            "curso_created_at": "10/02/2025",
            "curso_updated_at": "17/02/2025"
        }
    ]

* **Obter um curso específico:**
    * Método: GET
    * URL: 'http://127.0.0.1:5000/cursos/01'
    * Resposta esperada:
 {
        "curso_id": "01",
        "curso_name": "HMTL",
        "curso_description": "Curso básico de HTML",
        "curso_duration": "10 horas",
        "curso_created_at": "17/02/2025",
        "curso_updated_at": "17/02/2025"
 }

* **Cadastrar um novo curso:**
    * Método: POST
    * URL: 'http://127.0.0.1:5000/cursos/03'
    * Corpo da requisição:
{
     "curso_id": "03",
    "curso_name": "Python",
    "curso_description": "Python do básico ao avançado",
    "curso_duration": "40 horas",
    "curso_created_at": "25/12/2024",
    "curso_updated_at": "10/01/2025"
}
    * Resposta esperada:
{
     "curso_id": "03",
    "curso_name": "Python",
    "curso_description": "Python do básico ao avançado",
    "curso_duration": "40 horas",
    "curso_created_at": "25/12/2024",
    "curso_updated_at": "10/01/2025"
}

* **Cadastrar um novo curso ou alterar um curso existente:**
    * Método: PUT
    * URL: 'http://127.0.0.1:5000/cursos/04'
    * Corpo da requisição:
{
    "curso_name": "Java",
    "curso_description": "Java Básico",
    "curso_duration": "50 horas",
    "curso_created_at": "01/01/2025",
    "curso_updated_at": "15/02/2025"
}
    * Resposta esperada:
{
    "curso_id": "04",
    "curso_name": "Java",
    "curso_description": "Java Básico",
    "curso_duration": "50 horas",
    "curso_created_at": "01/01/2025",
    "curso_updated_at": "15/02/2025"
}
* ** Deletar um curso:**
     * Método: DELETE
     * URL: 'http://127.0.0.1:5000/cursos/04'
     * Resposta esperada:
{
    "mensagem": "Curso deletado."
}

E assim sucessivamente para os demais endpoints

* ** Verificar se aluno está matriculado no curso:**
     * Método: GET
     * URL: 'http://127.0.0.1:5000/cursos/01/alunos'
     * Resposta esperada:
{
    "alunos": [
        {
            "aluno_id": "01",
            "aluno_name": "Carlos Silva",
            "aluno_email": "carlos_silva@gmail.com",
            "aluno_created_at": "15/01/2025",
            "aluno_updated_at": "17/02/2025"
        }
    ]
}

* ** Verificar se aluno está matriculado no curso:**
     * Método: GET
     * URL: 'http://127.0.0.1:5000/alunos/02/cursos'
     * Resposta esperada:
{
    "cursos": [
        {
            "curso_id": "02",
            "curso_name": "CSS",
            "curso_description": "Curso básico de CSS",
            "curso_duration": "15 horas",
            "curso_created_at": "10/02/2025",
            "curso_updated_at": "17/02/2025"
        }
    ]
}

Validações:
* ** Campos obrigatórios:
     * Método POST
     * URL: 'http://127.0.0.1:5000/alunos/03'
     * Corpo da requisição:
{
    "aluno_email": "viviane.neris@gmail.com",
    "aluno_created_at": "19/02/2025",
    "aluno_updated_at": "19/02/2025"
}

    * Resposta esperada:
{
    "mensagem": "O campo nome é obrigatório."
}
* ** Aluno não pode se matricular no mesmo curso duas vezes: 
     * Método POST
     * URL: 'http://127.0.0.1:5000/alunos/03'
     * Corpo da requisição:


{
    "curso_id": "02",
    "aluno_id": "02",
    "enrollment_date": "19/02/2025"
}
     * Resposta esperada:
{
    "mensagem": "Este aluno já está matriculado neste curso."
}
