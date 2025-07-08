import os, pickle, funcExibicao as menuPrincipal, funcHorarios as menuHorarios, funcMaterias as menuMaterias;

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

opcaoPrincipal = menuPrincipal.menuInicial();
while opcaoPrincipal != "0":
    # horarios atuais
    if opcaoPrincipal == "1":
        opcaoSecundaria = menuPrincipal.menuHorariosAtuais(agenda);
        if opcaoSecundaria == "1" :
            menuHorarios.menuCadastraHorarios(agenda, materias);
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        elif opcaoSecundaria == "2" :
            menuHorarios.menuCadastraHorarios(agenda, materias)
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        elif opcaoSecundaria == "3" :
            menuHorarios.menuRemoveHorarios(agenda)
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        elif opcaoSecundaria == "0" :
            opcaoPrincipal = menuPrincipal.menuInicial();
        else :
            opcaoPrincipal = menuPrincipal.redirecionaErro();

    # horarios vagos
    elif opcaoPrincipal == "2":
        opcaoSecundaria = menuPrincipal.menuHorariosVagos(agenda);
        if opcaoSecundaria == "1" :
            menuHorarios.menuCadastraHorarios(agenda, materias);
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        elif opcaoSecundaria == "2" :
            menuHorarios.menuCadastraHorarios(agenda, materias)
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        elif opcaoSecundaria == "3" :
            menuHorarios.menuRemoveHorarios(agenda)
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        elif opcaoSecundaria == "0" :
            opcaoPrincipal = menuPrincipal.menuInicial();
        else :
            opcaoPrincipal = menuPrincipal.redirecionaErro();

    # materias
    elif opcaoPrincipal == "3":
        opcaoSecundaria = menuMaterias();
        if opcaoSecundaria == "1" :
            menuMaterias.cadastraMateria(materias);
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        if opcaoSecundaria == "2":
            menuMaterias.removeMateria(materias);
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        elif opcaoSecundaria == "0" :
            opcaoPrincipal = menuPrincipal.menuInicial();
        else :
            opcaoPrincipal = menuPrincipal.redirecionaErro();

    elif opcaoPrincipal == "0":
        os.system("clear");
        print("#########################################################################################");
        print("############               Você encerrou o programa, até logo!               ############");
        print("#########################################################################################");
        print();
    else:
        opcaoPrincipal = menuPrincipal.redirecionaErro();
print("Fim");