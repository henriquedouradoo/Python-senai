import sqlite3

class Professor:

    '''Classe para criar professor'''

    def __init__ (self, nome, cpf, telefone = None, email = None,  formacao = None, especialidade = None ):

        '''construtor da classe professor'''

        self.nome = nome
        self.cpf = cpf
        self.__matricula = 0
        self.telefone = telefone
        self.email = None
        self.verifica_email(email)
        self.formacao = formacao
        self.especialidade = especialidade

        self.banco_de_dados()

    @property
    def matricula (self):
        return self.__matricula

    def verifica_email(self,email):
        if email != '':
                
            if '@' in email:
                self.email = email

            else:
                raise ValueError ('E-mail incorreto!')

        else:
            self.email = email
    
    @classmethod
    def listar(cls):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = """
            SELECT *
            FROM Professores
        """
        cursor.execute(sql)

        lista_professores = cursor.fetchall()

        conexao.close()

        return lista_professores

    def banco_de_dados (self):
        conexao = sqlite3.connect ('gestao_escolar.db')

        cursor = conexao.cursor()

        sql = f'''
            INSERT INTO Professores(
                Nome,
                CPF,
                Telefone,
                Email,
                Formacao,
                Especialidade
            )

        Values(
            '{self.nome}',
            '{self.cpf}',
            '{self.telefone}',
            '{self.email}',
            '{self.formacao}',
            '{self.especialidade}'
        )
        '''

        cursor.execute(sql)

        self.__matricula = cursor.lastrowid

        conexao.commit()

        conexao.close()

    def __repr__ (self):

        impressao = f'''
        ---- CADASTRO PROFESSORES ----
Matricula: {self.__matricula}
Nome Completo: {self.nome}
CPF: {self.cpf}
Telefone: {self.telefone}
Formacao: {self.formacao}
Especialidade: {self.especialidade}
            '''
        return impressao

if __name__ == '__main__':
    # professor1 = Professor(nome = 'Ricardo', cpf = 58404, email = 'ricard@gmail.com' )
    print(Professor.listar())

