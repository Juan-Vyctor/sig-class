import os, pickle, funcExibicao as menuPrincipal, funcHorarios as menuHorarios, funcMaterias as menuMaterias;

#####################################
##### Projeto Class - Versão 5  #####
#####################################

# recebimento de arquivos/preenchimento de dados
# materias
try :
    arqMaterias = open("materias.dat", "rb");
    materias = {};
    materias = pickle.load(arqMaterias);
    arqMaterias.close();
except:
    arqMaterias = open("materias.dat", "wb");
    materias = {
        "DCT1102": {
            "codigo": "DCT1102",
            "nome": "Introdução à informática",
            "professor": "Luís Paulo",
        },
        "DCT3101": {
            "codigo": "DCT3101",
            "nome": "Teoria Geral da Administração",
            "professor": "Humberto Habelo",
        },
        "DCT1301": {
            "codigo": "DCT1301",
            "nome": "Fundamentos da Matemática",
            "professor": "Almir",
        },
        "a": {
            "codigo": "a",
            "nome": "a",
            "professor": "a",
        },
    }
    pickle.dump(materias, arqMaterias);
    arqMaterias.close();
# horarios
try :
    arqHorarios = open("horarios.dat", "rb");
    horarios = {};
    horarios = pickle.load(arqHorarios);
    arqHorarios.close();
except:
    arqHorarios = open("horarios.dat", "wb");
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
    pickle.dump(horarios, arqHorarios);
    arqHorarios.close();
# agenda
try :
    arqAgenda = open("agenda.dat", "rb");
    agenda = {};
    agenda = pickle.load(arqAgenda);
    arqAgenda.close();
except :
    arqAgenda = open("agenda.dat", "wb");
    agenda = {
        "2": horarios,
        "3": horarios,
        "4": horarios,
        "5": horarios,
        "6": horarios,
    };
    pickle.dump(agenda, arqAgenda);
    arqAgenda.close();

def salvaDados(materias, horarios, agenda) :
    arqMaterias = open("materias.dat", "wb");
    pickle.dump(materias, arqMaterias);
    arqMaterias.close();

    arqHorarios = open("horarios.dat", "wb");
    pickle.dump(horarios, arqHorarios);
    arqMaterias.close();

    arqAgenda = open("agenda.dat", "wb");
    pickle.dump(agenda, arqAgenda);
    arqAgenda.close();

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
        opcaoSecundaria = menuPrincipal.menuMaterias(materias);
        if opcaoSecundaria == "1" :
            menuMaterias.cadastraMateria(materias);
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        if opcaoSecundaria == "2":
            menuMaterias.removeMateria(agenda, materias);
            opcaoPrincipal = menuPrincipal.redirecionaSucesso();
        elif opcaoSecundaria == "0" :
            opcaoPrincipal = menuPrincipal.menuInicial();
        else :
            opcaoPrincipal = menuPrincipal.redirecionaErro();

    elif opcaoPrincipal != "0":
        opcaoPrincipal = menuPrincipal.redirecionaErro();
os.system("clear");
print("#########################################################################################");
print("############               Você encerrou o programa, até logo!               ############");
print("#########################################################################################");
print();
print("Fim");

salvaDados(materias, horarios, agenda);