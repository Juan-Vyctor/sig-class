import os

#####################################
##### Projeto Class - Versão 4  #####
#####################################

# preenchimento de dados
materias = {
    "Introdução à informática" : {
        "nome" : "Introdução à informática",
        "professor" : "Luís Paulo"
    },
    "Teoria Geral da Administração" : {
        "nome" : "Teoria Geral da Administração",
        "professor" : "Humberto Habelo"
    }
};
horarios = {
    "M": {
        "1": None, "2": None, "3": None, "4": None, "5": materias["Introdução à informática"], "6": materias["Introdução à informática"],
    },
    "T": {
        "1": None, "2": None, "3": None, "4": None, "5": materias["Introdução à informática"], "6": materias["Introdução à informática"],
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
def menuPrincipal() :
    os.system("clear");
    print("#########################################################################################");
    print("#############                        Projeto SIG-Class                      #############");
    print("#########################################################################################");
    print("#############                   1 - Ver horários atuais                     #############");
    print("#############                   2 - Visualizar matérias                     #############");
    print("#############                   3 - Checar horários vagos                   #############");
    print("#############                   4 - Adicionar matéria                       #############");
    print("#############                   5 - Adicionar horário                       #############");
    print("#############                   0 - Sair                                    #############");
    print("#########################################################################################");
    print();
    
    opcaoPrincipal = input("Escolha uma das opções: ");
    return opcaoPrincipal;
def menuHorariosAtuais() :
    os.system("clear");
    print("#########################################################################################");
    print("#############                       Sua agenda está assim                   #############");
    print("#########################################################################################");
    print();

    print("#############                         Horários da Manhã                     #############");
    horariosManha = pegaHorariosTurno(agenda, "M");
    for dia in horariosManha :
        for horario in horariosManha[dia] :
            print(dia + "a feira", end=', ');
            print(str(horario) + "o horário:");
            aula = horariosManha[dia][horario];
            print("Matéria: " + aula["nome"]);
            print("Professor(a) responsável: " + aula["professor"] + "\n");
    print();

    print("Horários da Tarde");
    horariosTarde = pegaHorariosTurno(agenda, "T");
    for horario in horariosTarde :
        print("Matéria: " + horario["nome"]);
        print("Professor(a) responsável: " + horario["professor"]);
    print();

    print("Horários da Noite");
    horariosNoite = pegaHorariosTurno(agenda, "N");
    for horario in horariosNoite :
        print("Matéria: " + horario["nome"]);
        print("Professor(a) responsável: " + horario["professor"]);
    print();

    print("#########################################################################################");
    print("#############                       O que deseja fazer?                     #############");
    print("#########################################################################################");
    print("#############                   1 - Adicionar horário                       #############");
    print("#############                   2 - Atualizar horário                       #############");
    print("#############                   3 - Remover horário                         #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();

    opcaoSecundaria = input("Escolha uma das opções: ");
    return opcaoSecundaria;
def menuMaterias() :
    os.system("clear");
    print("#########################################################################################");
    print("#############               Aqui estão as matérias cadastradas              #############");
    print("#########################################################################################");
    print();
    listaMaterias(materias);
    print();
    print("#########################################################################################");
    print("#############                       O que deseja fazer?                     #############");
    print("#########################################################################################");
    print("#############                   1 - Criar nova matéria                      #############");
    print("#############                   2 - Remover uma matéria                     #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();

    opcaoSecundaria = input("Escolha uma das opções: ");
    return opcaoSecundaria;
def menuHorariosVagos() :
    os.system("clear");
    print("#########################################################################################");
    print("############               Seus horários vagos são os seguintes              ############");
    print("#########################################################################################");
    print();
    
    print("Horários da Manhã");
    horariosManha = pegaHorariosVagos(agenda);
    for horario in horariosManha :
        exibeHorarioVago(horario);
    print();

    print("Horários da Tarde");
    horariosTarde = pegaHorariosVagos(agenda);
    for horario in horariosTarde :
        exibeHorarioVago(horario);
    print();
    
    print("Horários da Noite");
    horariosNoite = pegaHorariosVagos(agenda);
    for horario in horariosNoite :
        exibeHorarioVago(horario);

    print();
    print("#########################################################################################");
    print("#############                       O que deseja fazer?                     #############");
    print("#########################################################################################");
    print("#############                   1 - Adicionar matéria à um dos horários     #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();

    opcaoSecundaria = input("Escolha uma das opções: ");
    return opcaoSecundaria;
def menuNovaMateria() :
    os.system("clear");
    print("#########################################################################################");
    print("############   Confira suas matérias já existentes antes de criar uma nova   ############");
    print("#########################################################################################");
    print();
    listaMaterias(materias);
    print();
    print("#########################################################################################");
    print("#############                       O que deseja fazer?                     #############");
    print("#########################################################################################");
    print("#############                   1 - Criar nova matéria                      #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();
    
    opcaoSecundaria = input("Escolha uma das opções: ");
    return opcaoSecundaria
def menuNovoHorario() :
    os.system("clear");
    print("#########################################################################################");
    print("# Aqui estão os horários livres, apenas neles podem ser adicionados um novo compromisso #");
    print("#########################################################################################");
    print();
    
    print("Horários da Manhã");
    horariosManha = pegaHorariosVagos(agenda);
    for horario in horariosManha :
        exibeHorarioVago(horario);
    print();

    print("Horários da Tarde");
    horariosTarde = pegaHorariosVagos(agenda);
    for horario in horariosTarde :
        exibeHorarioVago(horario);
    print();
    
    print("Horários da Noite");
    horariosNoite = pegaHorariosVagos(agenda);
    for horario in horariosNoite :
        exibeHorarioVago(horario);
    
    print();
    print("#########################################################################################");
    print("#############                       O que deseja fazer?                     #############");
    print("#########################################################################################");
    print("#############                   1 - Escolher um dos horários                #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();
    
    opcaoSecundaria = input("Escolha uma das opções: ");
    return opcaoSecundaria;
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
    print("#############                   2 - Visualizar matérias                     #############");
    print("#############                   3 - Checar horários vagos                   #############");
    print("#############                   4 - Adicionar matéria                       #############");
    print("#############                   5 - Adicionar horário                       #############");
    print("#############                   0 - Sair                                    #############");
    print("#########################################################################################");
    print();
    
    opcaoPrincipal = input("Escolha uma das opções: ");
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
def pegaHorariosVagos(agenda) :
    vagos = {};

    for dia in agenda :
        for turno in dia :
            for horario in turno :
                if horario == None :
                    vagos[dia][turno][horario] = dia[turno][horario];
    
    return vagos;
def exibeHorarioVago(horario) :
    dados = horario.keys();
    dia = dados[0];
    turno = dados[1];
    hora = dados[2];
    
    print("Dia: " + dia);
    print("Turno: " + turno);
    print("Horário: " + hora);
def cadastraHorarios(agenda, materias) :
    os.system("clear");
    materia = str(input("Qual matéria vai ser adicionada?"));
    print("Escolha qual em qual horário a matéria será adicionada. Utilize o formato da universidade (número/letra/números).");
    horarios = str(input("\nCaso você queira colocar vários horários de uma vez, separe por ';'. Ex: '12T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    for horario in horarios :
        if "M" in horario :
            dados = horario.split("M");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["M"][aula] = materias[materia];
        elif "T" in horario:
            dados = horario.split("T");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["T"][aula] = materias[materia];
        elif "N" in horario:
            dados = horario.split("N");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["N"][aula] = materias[materia];
def atualizaHorarios(agenda, materias) :
    os.system("clear");
    materia = str(input("Qual matéria vai ser adicionada?"));
    print("Escolha qual em qual horário a matéria será adicionada. Utilize o formato da universidade (número/letra/números).");
    horarios = str(input("\nCaso você queira colocar vários horários de uma vez, separe por ';'. Ex: '12T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    for horario in horarios :
        if "M" in horario :
            dados = horario.split("M");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["M"][aula] = materias[materia];
        elif "T" in horario:
            dados = horario.split("T");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["T"][aula] = materias[materia];
        elif "N" in horario:
            dados = horario.split("N");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["N"][aula] = materias[materia];
def removeHorarios(agenda) :
    print("Escolha qual em qual horário a matéria será removida. Utilize o formato da universidade (números/letra/números).");
    horarios = str(input("Caso você queira remover vários horários de uma vez, separe por ';'. Ex: '12T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    for horario in horarios :
        if "M" in horario :
            dados = horario.split("M");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["M"][aula] = None;
        elif "T" in horario:
            dados = horario.split("T");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["T"][aula] = None;
        elif "N" in horario:
            dados = horario.split("N");
            dia = dados[0];
            aula = dados[1];
            agenda[dia]["N"][aula] = None;    

# funções de matérias
def listaMaterias(materias) :
    for materia in materias :
        print(materia["nome"]);
def cadastraMateria(materias) :
    os.system("clear");
    materia = str(input("Qual o nome da matéria a ser adicionada?"));
    professor = str(input("Quem ministra essa matéria?"));
    materias[materia] = {
        "nome": materia,
        "professor": professor
    };
def removeMateria(materias) :
    os.system("clear");
    nome = str(input("Qual o nome da matéria a ser removida?"));
    professor = str(input("Quem ministra essa matéria?"));
    for materia in materias :
        if materia["nome"] == nome and materia["professor"] == professor :
            del materias[materia];

opcaoPrincipal = "";
while opcaoPrincipal != "0":
    opcaoPrincipal = menuPrincipal();
    
    # horarios atuais
    if opcaoPrincipal == "1":
        opcaoSecundaria = menuHorariosAtuais();
        if opcaoSecundaria == "1" :
            cadastraHorarios(agenda);
        elif opcaoSecundaria == "2" :
            cadastraHorarios(agenda);
        elif opcaoSecundaria == "3" :
            removeHorarios(agenda);
        elif opcaoSecundaria == 0 :
            opcaoPrincipal = menuPrincipal();
        else :
            opcaoPrincipal = redirecionaErro();
            
    # materias
    elif opcaoPrincipal == "2":
        opcaoSecundaria = menuMaterias();
        if opcaoSecundaria == "1" :
            cadastraMateria(agenda);
        elif opcaoSecundaria == 0 :
            opcaoPrincipal = menuPrincipal();
        else :
            opcaoPrincipal = redirecionaErro();
            
    # horarios vagos
    elif opcaoPrincipal == "3":
        opcaoSecundaria = menuHorariosVagos;
        if opcaoSecundaria == "1" :
            cadastraHorarios(agenda, materias);
        elif opcaoSecundaria == 0 :
            opcaoPrincipal = menuPrincipal();
        else :
            opcaoPrincipal = redirecionaErro();
            
    # nova materias
    elif opcaoPrincipal == "4":
        if opcaoSecundaria == 1 :
            cadastraMateria(materias);
        elif opcaoSecundaria == 0 :
            opcaoPrincipal = menuPrincipal();
        else :
            opcaoPrincipal = redirecionaErro();
            
    # novo horário
    elif opcaoPrincipal == "5":
        if opcaoSecundaria == 1 :
            cadastraHorarios(agenda);
        elif opcaoSecundaria == 0 :
            opcaoPrincipal = menuPrincipal();
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
