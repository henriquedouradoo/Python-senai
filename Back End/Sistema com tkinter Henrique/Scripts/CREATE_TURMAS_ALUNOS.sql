CREATE TABLE Turmas_Alunos(
    codigo_turma INTEGER
        REFERENCES Turmas ( codigo ),

    matricula_aluno INTEGER
        REFERENCES Alunos ( matricula ),

    PRIMARY KEY(
        codigo_turma,
        matricula_aluno
    )
)