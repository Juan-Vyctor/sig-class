import os

#####################################
##### Projeto Class - Versão 4  #####
#####################################

# preenchimento de dados
materias = {
    "Introdução à informática": {
        "nome": "Introdução à informática",
        "professor": "Luís Paulo",
    },
    "Teoria Geral da Administração": {
        "nome": "Teoria Geral da Administração",
        "professor": "Humberto Habelo",
    },
    "Fundamentos da Matemática": {
        "nome": "Fundamentos da Matemática",
        "professor": "Almir",
    },
    "a": {
        "nome": "a",
        "professor": "a",
    },
}
horarios = {
    "M": {
        "1": None, "2": None, "3": None, "4": None, "5": materias["Introdução à informática"], "6": materias["Introdução à informática"],
    },
    "T": {
        "1": None, "2": None, "3": None, "4": None, "5": materias["Fundamentos da Matemática"], "6": materias["Fundamentos da Matemática"],
    },
    "N": {
        "1": materias["Teoria Geral da Administração"], "2": materias["Teoria Geral da Administração"], "3": None, "4": None, "5": None, "6": None,
    },
};
agenda = {
    "2": horarios,
    "3": horarios,
    "4": horarios,
    "5": horarios,
    "6": horarios,
};

# funções de exibição
def menuInicial() :
    os.system("clear");
    print("#########################################################################################");
    print("#############                        Projeto SIG-Class                      #############");
    print("#########################################################################################");
    print("#############                   1 - Ver horários atuais                     #############");
    print("#############                   2 - Checar horários vagos                   #############");
    print("#############                   3 - Visualizar matérias                     #############");
    print("#############                   0 - Sair                                    #############");
    print("#########################################################################################");
    print();
    
    opcaoPrincipal = str(input("Escolha uma das opções: "));
    return opcaoPrincipal;
def menuHorariosAtuais() :
    os.system("clear");
    print("#########################################################################################");
    print("#############                       Sua agenda está assim                   #############");
    print("#########################################################################################");
    print();

    print("#########################################################################################");
    print("#############                       Horários da Manhã                       #############");
    print("#########################################################################################");
    print();

    horariosManha = pegaHorariosTurno(agenda, "M");
    exibeHorariosOcupados(horariosManha);

    print("#########################################################################################");
    print("#############                       Horários da Tarde                       #############");
    print("#########################################################################################");
    horariosTarde = pegaHorariosTurno(agenda, "T")
    exibeHorariosOcupados(horariosTarde);

    print("#########################################################################################");
    print("#############                       Horários da Noite                       #############");
    print("#########################################################################################");
    horariosNoite = pegaHorariosTurno(agenda, "N")
    exibeHorariosOcupados(horariosNoite);

    print("#########################################################################################");
    print("#############                       O que deseja fazer?                     #############");
    print("#########################################################################################");
    print("#############                   1 - Adicionar horário                       #############");
    print("#############                   2 - Atualizar horário                       #############");
    print("#############                   3 - Remover horário                         #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();

    opcaoSecundaria = str(input("Escolha uma das opções: "))
    return opcaoSecundaria;
def menuMaterias() :
    os.system("clear");
    print("#########################################################################################");
    print("#############               Aqui estão as matérias cadastradas              #############");
    print("#########################################################################################");
    
    exibeMaterias(materias);

    print("#########################################################################################");
    print("#############                       O que deseja fazer?                     #############");
    print("#########################################################################################");
    print("#############                   1 - Criar nova matéria                      #############");
    print("#############                   2 - Remover uma matéria                     #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();

    opcaoSecundaria = str(input("Escolha uma das opções: "))
    return opcaoSecundaria;
def menuHorariosVagos() :
    os.system("clear");
    print("#########################################################################################");
    print("############               Seus horários vagos são os seguintes              ############");
    print("#########################################################################################");
    print();

    print("#########################################################################################");
    print("#############                       Horários da Manhã                       #############");
    print("#########################################################################################");
    print();

    horariosManha = pegaHorariosVagos(agenda, "M");
    exibeHorariosVagos(horariosManha);

    print("#########################################################################################");
    print("#############                       Horários da Tarde                       #############");
    print("#########################################################################################");
    horariosTarde = pegaHorariosVagos(agenda, "T")
    exibeHorariosVagos(horariosTarde);

    print("#########################################################################################");
    print("#############                       Horários da Noite                       #############");
    print("#########################################################################################");
    horariosNoite = pegaHorariosVagos(agenda, "N")
    exibeHorariosVagos(horariosNoite);

    print();
    print("#########################################################################################");
    print("#############                       O que deseja fazer?                     #############");
    print("#########################################################################################");
    print("#############                   1 - Adicionar matéria à um dos horários     #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();

    opcaoSecundaria = str(input("Escolha uma das opções: "))
    return opcaoSecundaria;
def redirecionaSucesso() :
    os.system("clear");
    print("#########################################################################################");
    print("#############                      Operação bem sucedida                    #############");
    print("#########################################################################################");
    print();
    print("#########################################################################################");
    print("#############                        Projeto SIG-Class                      #############");
    print("#########################################################################################");
    print("#############                   1 - Ver horários atuais                     #############");
    print("#############                   2 - Checar horários vagos                   #############");
    print("#############                   3 - Visualizar matérias                     #############");
    print("#############                   0 - Sair                                    #############");
    print("#########################################################################################");
    print();

    opcaoPrincipal = str(input("Escolha uma das opções: "))
    return opcaoPrincipal;
def redirecionaErro() :
    os.system("clear");
    print("#########################################################################################");
    print("############    Você digitou uma opção inválida, voltando ao menu inicial    ############");
    print("#########################################################################################");
    print();
    print("#########################################################################################");
    print("#############                        Projeto SIG-Class                      #############");
    print("#########################################################################################");
    print("#############                   1 - Ver horários atuais                     #############");
    print("#############                   2 - Checar horários vagos                   #############");
    print("#############                   3 - Visualizar matérias                     #############");
    print("#############                   0 - Sair                                    #############");
    print("#########################################################################################");
    print();

    opcaoPrincipal = str(input("Escolha uma das opções: "))
    return opcaoPrincipal;

# funções de horarios
def pegaHorariosTurno(agenda, turno) :
    utilizados = {};

    for dia in agenda :
        utilizados[dia] = {};
        for horario in range(1, 7) :
            aula = agenda[dia][turno][str(horario)];
            if aula != None :
                utilizados[dia][horario] = aula;

    return utilizados;
def pegaHorariosVagos(agenda, turno) :
    vagos = {}

    for dia in agenda:
        vagos[dia] = {}
        for horario in range(1, 7):
            aula = agenda[dia][turno][str(horario)]
            if aula == None:
                vagos[dia][horario] = True

    return vagos;
def exibeHorariosOcupados(horarios) :
    for dia in horarios :
        for horario in horarios[dia] :
            print("\n" + dia + "a feira", end=', ');
            print(str(horario) + "o horário:");
            aula = horarios[dia][horario];
            print("Matéria: " + aula["nome"]);
            print("Professor(a) responsável: " + aula["professor"]);
        print()
def exibeHorariosVagos(horarios):
    for dia in horarios:
        print("\nNa " + dia + "a feira, seus horários vagos são:");
        for horario in horarios[dia]:
            print(str(horario) + "o horário");
        print();
def cadastraHorarios(agenda, materias) :
    os.system("clear");
    print("Escolha em qual horário a matéria será adicionada. Utilize o formato da universidade (número/letra/números). ");
    horarios = str(input("Caso você queira colocar vários horários de uma vez, separe por ';'. Ex: '25T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    print("\nQual matéria vai ser adicionada a esses horários? Escolha uma dentre as suas seguintes:");
    exibeMaterias(materias);
    materia = str(input());

    for horario in horarios :
        if "M" in horario :
            dados = horario.split("M");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda['2']["M"][aula] = materias[materia];
        elif "T" in horario:
            dados = horario.split("T");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda[dia]["T"][aula] = materias[materia];
        elif "N" in horario:
            dados = horario.split("N");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda[dia]["N"][aula] = materias[materia];
def atualizaHorarios(agenda, materias) :
    os.system("clear");
    print("Escolha o horário da matéria será adicionada. Utilize o formato da universidade (número/letra/números). ");
    horarios = str(input("Caso você queira colocar vários horários de uma vez, separe por ';'. Ex: '25T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    print("\nQual vai ser a nova matéria desses horários? Escolha uma dentre as suas seguintes:");
    exibeMaterias(materias);
    materia = str(input());

    for horario in horarios :
        if "M" in horario :
            dados = horario.split("M");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda['2']["M"][aula] = materias[materia];
        elif "T" in horario:
            dados = horario.split("T");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda[dia]["T"][aula] = materias[materia];
        elif "N" in horario:
            dados = horario.split("N");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda[dia]["N"][aula] = materias[materia];
def removeHorarios(agenda) :
    os.system("clear");
    print("Escolha o horário da matéria será removida. Utilize o formato da universidade (número/letra/números). ");
    horarios = str(input("Caso você queira colocar vários horários de uma vez, separe por ';'. Ex: '25T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    for horario in horarios :
        if "M" in horario :
            dados = horario.split("M");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda['2']["M"][aula] = None;
        elif "T" in horario:
            dados = horario.split("T");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda[dia]["T"][aula] = None;
        elif "N" in horario:
            dados = horario.split("N");
            dias = dados[0];
            aulas = dados[1];
            for dia in dias :
                for aula in aulas :
                    agenda[dia]["N"][aula] = None;

# funções de matérias
def exibeMaterias(materias) :
    print();
    for materia in materias:
        print("Matéria: " + materias[materia]["nome"]);
        print("Professor(a) responsável: " + materias[materia]["professor"] + "\n");
def cadastraMateria(materias) :
    os.system("clear");
    materia = str(input("Qual o nome da matéria a ser adicionada? "));
    professor = str(input("Quem ministra essa matéria? "));
    materias[materia] = {
        "nome": materia,
        "professor": professor
    };
def removeMateria(materias) :
    os.system("clear");
    nome = str(input("Qual o nome da matéria a ser removida? "));
    professor = str(input("Quem ministra essa matéria? "));
    for materia in materias :
        nomeMateria = materias[materia]["nome"];
        nomeProfessor = materias[materia]["professor"];
        if nomeMateria == nome and nomeProfessor == professor :
            apagar = materia;
    del materias[apagar];

opcaoPrincipal = menuInicial();
while opcaoPrincipal != "0":
    # horarios atuais
    if opcaoPrincipal == "1":
        opcaoSecundaria = menuHorariosAtuais();
        if opcaoSecundaria == "1" :
            cadastraHorarios(agenda, materias)
            opcaoPrincipal = redirecionaSucesso()
        elif opcaoSecundaria == "2" :
            cadastraHorarios(agenda, materias);
        elif opcaoSecundaria == "3" :
            removeHorarios(agenda);
        elif opcaoSecundaria == 0 :
            opcaoPrincipal = menuInicial();
        else :
            opcaoPrincipal = redirecionaErro();

    # horarios vagos
    elif opcaoPrincipal == "2":
        opcaoSecundaria = menuHorariosVagos();
        if opcaoSecundaria == "1" :
            cadastraHorarios(agenda, materias)
            opcaoPrincipal = redirecionaSucesso()
        elif opcaoSecundaria == "0" :
            opcaoPrincipal = menuInicial();
        else :
            opcaoPrincipal = redirecionaErro();

    # materias
    elif opcaoPrincipal == "3":
        opcaoSecundaria = menuMaterias();
        if opcaoSecundaria == "1" :
            cadastraMateria(materias);
            opcaoPrincipal = redirecionaSucesso()
        if opcaoSecundaria == "2":
            removeMateria(materias)
            opcaoPrincipal = redirecionaSucesso()
        elif opcaoSecundaria == "0" :
            opcaoPrincipal = menuInicial();
        else :
            opcaoPrincipal = redirecionaErro();

    elif opcaoPrincipal == "0":
        os.system("clear");
        print("#########################################################################################");
        print("############               Você encerrou o programa, até logo!               ############");
        print("#########################################################################################");
        print();
    else:
        opcaoPrincipal = redirecionaErro();

print("Fim");