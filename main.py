import os

#####################################
##### Projeto Class - Versão 4  #####
#####################################

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
    
    print("Horários da Manhã");
    horariosManha = pegaHorariosTurno(agenda, "M");
    for horario in horariosManha :
        print("Matéria: " + horario["nome"]);
        print("Professor(a) responsável: " + horario["professor"]);
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
    print("#############                   1 - Remover matéria                         #############");
    print("#############                   0 - Voltar                                  #############");
    print("#########################################################################################");
    print();
    opcaoSecundaria = input("Escolha uma das opções: ");
    
    return opcaoSecundaria;

# funções de horarios
def pegaHorariosTurno(agenda, turno) :
    horarios = {};

    horario = 1;
    for dia in agenda :
        for horario in range(7) :
            horarios["nome"] = dia[turno][horario]["nome"];
            horarios["professor"] = dia[turno][horario]["professor"];

    return horarios;

def pegaHorariosVagos(agenda) :
    vagos = {};

    for dia in agenda :
        for turno in dia :
            for horario in turno :
                if horario == None :
                    vagos[dia][turno][horario] = dia[turno][horario];
    
    return vagos;

def cadastraHorario(agenda, horarios, materias) :
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

def removeHorario(agenda, horarios) :
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

#funções de matérias
def mostraMaterias(materias) :
    for materia in materias :
        print(materia["nome"]);

def cadastraMateria(materias, materia, professor) :
    materias[materia] = {
        "nome": materia,
        "professor": professor
    };

opcaoPrincipal = "";
while opcaoPrincipal != "0":
    opcaoPrincipal = menuPrincipal();
    if opcaoPrincipal == "1":
        opcaoSecundaria = menuHorariosAtuais();
        if opcaoSecundaria == "1" :
            horarios = str(input("Escolha qual em qual horário a matéria será removida. Utilize o formato da universidade (números/letra/números).\nCaso você queira colocar vários horários de uma vez, separe por ';'. Ex: '12T5; 34M2'.\n"));
            removeHorario(agenda, horarios);
        elif opcaoSecundaria == "0" :
            # ainda em andamento
            os.clear();
    elif opcaoPrincipal == "2":
        os.system("clear");
        print("#########################################################################################");
        print("#############               Aqui estão as matérias cadastradas              #############");
        print("#########################################################################################");
        print();
        mostraMaterias(materias);
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   1 - Criar nova matéria                      #############");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        opcaoSecundaria = input("Escolha uma das opções: ");
    elif opcaoPrincipal == "3":
        os.system("clear");
        #arrumar
        print("#########################################################################################");
        print("############               Seus horários vagos são os seguintes              ############");
        print("#########################################################################################");
        print();
        
        print("Horários da Manhã");
        horariosManha = pegaHorariosVagos(agenda);
        for horario in horariosManha :
            print();
        print();

        print("Horários da Tarde");
        horariosTarde = pegaHorariosVagos(agenda);
        for horario in horariosTarde :
            print("Matéria: " + horario["nome"]);
            print("Professor(a) responsável: " + horario["professor"]);
        print();
        
        print("Horários da Noite");
        horariosNoite = pegaHorariosVagos(agenda);
        for horario in horariosNoite :
            print("Matéria: " + horario["nome"]);
            print("Professor(a) responsável: " + horario["professor"]);
        print();

        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   1 - Adicionar matéria à um dos horários     #############");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        opcaoSecundaria = input("Escolha uma das opções: ");
    elif opcaoPrincipal == "4":
        os.system("clear");
        print("#########################################################################################");
        print("############   Confira suas matérias já existentes antes de criar uma nova   ############");
        print("#########################################################################################");
        print();
        mostraMaterias(materias);
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   1 - Criar nova matéria                      #############");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        opcaoSecundaria = input("Escolha uma das opções: ");

        if opcaoSecundaria == 1 :
            os.system("clear");
            materia = str(input("Qual o nome da matéria a ser adicionada?"));
            professor = str(input("Quem ministra essa matéria?"));

            cadastraMateria(materias, materia, professor);
        elif opcaoSecundaria == 0 :
            # aqui vai ser só um return mesmo não sei ainda como vai funcionar insira módulos i guess
            os.system("clear");
        else :
            print();
            print("#########################################################################################");
            print("############    Você digitou uma opção inválida, voltando ao menu inicial    ############");
            print("#########################################################################################");
            print();
    elif opcaoPrincipal == "5":
        os.system("clear");
        print("#########################################################################################");
        print("# Aqui estão os horários livres, apenas neles podem ser adicionados um novo compromisso #");
        print("#########################################################################################");
        print();

        print("Horários da Manhã");
        horariosManha = pegaHorariosVagos(agenda);
        for horario in horariosManha :
            print();
        print();

        print("Horários da Tarde");
        horariosTarde = pegaHorariosVagos(agenda);
        for horario in horariosTarde :
            print("Matéria: " + horario["nome"]);
            print("Professor(a) responsável: " + horario["professor"]);
        print();
        
        print("Horários da Noite");
        horariosNoite = pegaHorariosVagos(agenda);
        for horario in horariosNoite :
            print("Matéria: " + horario["nome"]);
            print("Professor(a) responsável: " + horario["professor"]);
        
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   1 - Escolher um dos horários                #############");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        opcaoSecundaria = input("Escolha uma das opções: ");

        if opcaoSecundaria == 1 :
            os.system("clear");
            materia = str(input("Qual matéria vai ser adicionada?"));
            horarios = str(input("Escolha qual em qual horário a matéria será adicionada. Utilize o formato da universidade (número/letra/números).\nCaso você queira colocar vários horários de uma vez, separe por ';'. Ex: '12T5; 34M2'.\n"));

            cadastraHorario(agenda, horarios, materias);
                    
        elif opcaoSecundaria == 0 :
            # aqui vai ser só um return mesmo não sei ainda como vai funcionar insira módulos i guess
            os.system("clear");
        else :
            print();
            print("#########################################################################################");
            print("############    Você digitou uma opção inválida, voltando ao menu inicial    ############");
            print("#########################################################################################");
            print();
    elif opcaoPrincipal == "0":
        os.system("clear");
        print("#########################################################################################");
        print("############               Você encerrou o programa, até logo!               ############");
        print("#########################################################################################");
        print();
        input("Escolha uma das opções: ");
    else:
        print();
        print("#########################################################################################");
        print("############    Você digitou uma opção inválida, voltando ao menu inicial    ############");
        print("#########################################################################################");
        print();

print("Fim");