import os, funcMaterias;

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

def cadastraHorarios(agenda, horarios, materias, materia):
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
    funcMaterias.exibeMaterias(materias);
    materia = str(input());

    cadastraHorarios(agenda, horarios, materias, materia);

def atualizaHorarios(agenda, materias) :
    os.system("clear");
    print("Escolha o horário da matéria será adicionada. Utilize o formato da universidade (número/letra/números). ");
    horarios = str(input("Caso você queira colocar vários horários de uma vez, separe por ';'. Ex: '25T5; 34M2'.\n"));
    horarios.replace(" ", "").upper();
    horarios = horarios.split(";");

    print("\nQual vai ser a nova matéria desses horários? Escolha uma dentre as suas seguintes, digitando o código da mesma:");
    funcMaterias.exibeMaterias(materias);
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

def removeHorariosMateria(agenda, codigo):
    for dia in agenda :
        for turno in agenda[dia] :
            for horario in agenda[dia][turno] :
                if agenda[dia][turno][horario] and agenda[dia][turno][horario]["codigo"] == codigo :
                    agenda[dia][turno][horario] = None