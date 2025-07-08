import os, pickle, funcExibicao, funcHorarios, funcMaterias;

#####################################
##### Projeto Class - Versão 5  #####
#####################################

# recebimento de arquivos/preenchimento de dados
# materias
try :
    lerMaterias = open("materias.dat", "rb");
    materias = pickle.load("materias.dat");
    lerMaterias.close();
except:
    salvarMaterias = open("materias.dat", "wb");
    materias = {
        "DCT1102": {
            "nome": "Introdução à informática",
            "professor": "Luís Paulo",
        },
        "DCT3101": {
            "nome": "Teoria Geral da Administração",
            "professor": "Humberto Habelo",
        },
        "DCT1301": {
            "nome": "Fundamentos da Matemática",
            "professor": "Almir",
        },
        "a": {
            "nome": "a",
            "professor": "a",
        },
    };
    pickle.dump(materias, salvarMaterias);
    salvarMaterias.close();
# horarios
try :
    lerHorarios = open("horarios.dat", "rb");
    horarios = pickle.load("horarios.dat");
    lerHorarios.close();
except:
    salvarHorarios = open("horarios.dat", "wb");
    horarios = {
        "M": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": materias["DCT1102"],
            "6": materias["DCT1102"],
        },
        "T": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": materias["DCT1301"],
            "6": materias["DCT1301"],
        },
        "N": {
            "1": materias["DCT3101"],
            "2": materias["DCT3101"],
            "3": None,
            "4": None,
            "5": None,
            "6": None,
        },
    };
    pickle.dump(horarios, salvarHorarios);
    salvarHorarios.close();
# agenda
try :
    lerAgenda = open("agenda.dat", "rb")
    agenda = pickle.load("agenda.dat")
    lerAgenda.close();
except :
    salvarAgenda = open("agenda.dat", "wb");
    agenda = {
        "2": horarios,
        "3": horarios,
        "4": horarios,
        "5": horarios,
        "6": horarios,
    };
    pickle.dump(agenda, salvarAgenda);
    salvarAgenda.close();

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
    print("############               Seus horários vagos são os seguintes              ############");
    print("#########################################################################################");
    print();

    listaHorariosAtuais(agenda, "M");
    listaHorariosAtuais(agenda, "T");
    listaHorariosAtuais(agenda, "N");

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
def menuHorariosVagos() :
    os.system("clear");
    print("#########################################################################################");
    print("############               Seus horários vagos são os seguintes              ############");
    print("#########################################################################################");
    print();

    listaHorariosVagos(agenda, "M");
    listaHorariosVagos(agenda, "T");
    listaHorariosVagos(agenda, "N");

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
def checaHorariosAtuais(horarios):
    haOcupados = False
    for horario in horarios.values():
        for ehOcupado in horario.values():
            if ehOcupado != None:
                return True;
    return haOcupados;
def listaHorariosAtuais(agenda, turno):
    horarios = pegaHorariosTurno(agenda, turno);
    if turno == "M" :
        turno = "Manhã"
    elif turno == "T":
        turno = "Tarde"
    if turno == "N":
        turno = "Noite"
    haOcupados = checaHorariosAtuais(horarios);
    if haOcupados :
        print("#########################################################################################");
        print(f"#############                       Horários da {turno}                       #############");
        print("#########################################################################################");
        print();
        exibeHorariosAtuais(horarios);
    else :
        print("#########################################################################################");
        print(f"#############              Você não possui horários pela {turno}              #############");
        print("#########################################################################################");
        print();
def checaHorarioVago(horarios):
    haVagos = False
    for horario in horarios.values():
        for ehVago in horario.values():
            if ehVago == True:
                return True;
    return haVagos;
def listaHorariosVagos(agenda, turno):
    horarios = pegaHorariosVagos(agenda, turno);
    if turno == "M" :
        turno = "Manhã"
    elif turno == "T":
        turno = "Tarde"
    if turno == "N":
        turno = "Noite"
    haVagos = checaHorarioVago(horarios);
    if haVagos :
        print("#########################################################################################");
        print(f"#############                    Horários vagos da {turno}                    #############");
        print("#########################################################################################");
        print();
        exibeHorariosVagos(horarios);
    else :
        print("#########################################################################################");
        print(f"#############           Você não possui horários vagos pela {turno}           #############");
        print("#########################################################################################");
        print();
def exibeHorariosAtuais(horarios) :
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
def cadastraHorarios(agenda, horarios, materia):
    for horario in horarios:
        if "M" in horario:
            dados = horario.split("M")
            dias = dados[0]
            aulas = dados[1]
            for dia in dias:
                for aula in aulas:
                    agenda["2"]["M"][aula] = materias[materia]
        elif "T" in horario:
            dados = horario.split("T")
            dias = dados[0]
            aulas = dados[1]
            for dia in dias:
                for aula in aulas:
                    agenda[dia]["T"][aula] = materias[materia]
        elif "N" in horario:
            dados = horario.split("N")
            dias = dados[0]
            aulas = dados[1]
            for dia in dias:
                for aula in aulas:
                    agenda[dia]["N"][aula] = materias[materia]
def menuCadastraHorarios(agenda, materias) :
    os.system("clear");
    print("Escolha em qual horário a matéria será adicionada. Utilize o formato da universidade (número/letra/números). ");
    horarios = str(input("Caso você queira colocar vários horários de uma vez, separe por ';'. Ex: '25T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    print("\nQual matéria vai ser adicionada a esses horários? Escolha uma dentre as suas seguintes, digitando o código da mesma:");
    exibeMaterias(materias);
    materia = str(input());

    cadastraHorarios(agenda, horarios, materia);
def atualizaHorarios(agenda, materias) :
    os.system("clear");
    print("Escolha o horário da matéria será adicionada. Utilize o formato da universidade (número/letra/números). ");
    horarios = str(input("Caso você queira colocar vários horários de uma vez, separe por ';'. Ex: '25T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    print("\nQual vai ser a nova matéria desses horários? Escolha uma dentre as suas seguintes, digitando o código da mesma:");
    exibeMaterias(materias);
    materia = str(input());

    cadastraHorarios(agenda, horarios, materia);
def menuRemoveHorarios(agenda) :
    os.system("clear");
    print("Escolha o horário da matéria será removida. Utilize o formato da universidade (número/letra/números). ");
    horarios = str(input("Caso você queira colocar vários horários de uma vez, separe por ';'. Ex: '25T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    removeHorarios(agenda, horarios);
def removeHorarios(agenda, horarios):
    for horario in horarios:
        if "M" in horario:
            dados = horario.split("M")
            dias = dados[0]
            aulas = dados[1]
            for dia in dias:
                for aula in aulas:
                    agenda["2"]["M"][aula] = None;
        elif "T" in horario:
            dados = horario.split("T")
            dias = dados[0]
            aulas = dados[1]
            for dia in dias:
                for aula in aulas:
                    agenda[dia]["T"][aula] = None;
        elif "N" in horario:
            dados = horario.split("N")
            dias = dados[0]
            aulas = dados[1]
            for dia in dias:
                for aula in aulas:
                    agenda[dia]["N"][aula] = None;

# funções de matérias
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

opcaoPrincipal = menuInicial();
while opcaoPrincipal != "0":
    # horarios atuais
    if opcaoPrincipal == "1":
        opcaoSecundaria = menuHorariosAtuais();
        if opcaoSecundaria == "1" :
            menuCadastraHorarios(agenda, materias);
            opcaoPrincipal = redirecionaSucesso();
        elif opcaoSecundaria == "2" :
            menuCadastraHorarios(agenda, materias)
            opcaoPrincipal = redirecionaSucesso();
        elif opcaoSecundaria == "3" :
            menuRemoveHorarios(agenda)
            opcaoPrincipal = redirecionaSucesso();
        elif opcaoSecundaria == "0" :
            opcaoPrincipal = menuInicial();
        else :
            opcaoPrincipal = redirecionaErro();

    # horarios vagos
    elif opcaoPrincipal == "2":
        opcaoSecundaria = menuHorariosVagos();
        if opcaoSecundaria == "1" :
            menuCadastraHorarios(agenda, materias);
            opcaoPrincipal = redirecionaSucesso();
        elif opcaoSecundaria == "2" :
            menuCadastraHorarios(agenda, materias)
            opcaoPrincipal = redirecionaSucesso();
        elif opcaoSecundaria == "3" :
            menuRemoveHorarios(agenda)
            opcaoPrincipal = redirecionaSucesso();
        elif opcaoSecundaria == "0" :
            opcaoPrincipal = menuInicial();
        else :
            opcaoPrincipal = redirecionaErro();

    # materias
    elif opcaoPrincipal == "3":
        opcaoSecundaria = menuMaterias();
        if opcaoSecundaria == "1" :
            cadastraMateria(materias);
            opcaoPrincipal = redirecionaSucesso();
        if opcaoSecundaria == "2":
            removeMateria(materias);
            opcaoPrincipal = redirecionaSucesso();
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