import os;

def exibeMaterias(materias) :
    print();
    for materia in materias:
        print("Código da Matéria: " + materia);
        print("Matéria: " + materias[materia]["nome"]);
        print("Professor(a) responsável: " + materias[materia]["professor"] + "\n");

def cadastraMateria(materias) :
    os.system("clear")
    codigo = str(input("Qual o código da matéria a ser adicionada? "))
    materia = str(input("Qual o nome da matéria a ser adicionada? "));
    professor = str(input("Quem ministra essa matéria? "));
    materias[codigo] = {
        "nome": materia,
        "professor": professor
    };

def removeMateria(materias) :
    os.system("clear");
    codigo = input("Digite o código da matéria que você deseja remover: ");
    for materia in materias :
            if materia == codigo :
                apagar = materia;
    if apagar :
        del materias[apagar];