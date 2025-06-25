import os

#####################################
##### Projeto Class - Versão 3 #####
#####################################

horarios = {
    "M": {
        "1": None, "2": None, "3": None, "4": None, "5": None, "6": None,
    },
    "T": {
        "1": None, "2": None, "3": None, "4": None, "5": None, "6": None,
    },
    "N": {
        "1": None, "2": None, "3": None, "4": None, "5": None, "6": None,
    },
};

agenda = {
    "2": horarios,
    "3": horarios,
    "4": horarios,
    "5": horarios,
    "6": horarios,
};

materias = {};

resp1 = "";
while resp1 != "0":
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
    resp1 = input("Escolha uma das opções: ");

    if resp1 == "1":
        os.system("clear");
        print("#########################################################################################");
        print("#############                       Sua agenda está assim                   #############");
        print("#########################################################################################");
        print();
        # aqui vai ter uma ruma de coisa mostrando como os horários da semana
        # tão, pegando os dados salvos e imprimindo
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        resp2 = input("Escolha uma das opções: ");
    elif resp1 == "2":
        os.system("clear");
        print("#########################################################################################");
        print("#############         Aqui estão os horários, divididos por matéria         #############");
        print("#########################################################################################");
        # ideia parecida, mas um foreach em cada matéria mostrando esparado
        # pra ficar mais fácil de ver o que tá onde
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        resp2 = input("Escolha uma das opções: ");
    elif resp1 == "3":
        os.system("clear");
        print("#########################################################################################");
        print("############               Seus horários vagos são os seguintes              ############");
        print("#########################################################################################");
        # lance tipo horario["materia"] == null ou sei lá como fica em Python
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        resp2 = input("Escolha uma das opções: ");
    elif resp1 == "4":
        os.system("clear");
        print("#########################################################################################");
        print("############   Confira suas matérias já existentes antes de criar uma nova   ############");
        print("#########################################################################################");
        print();
        # vai mostrar todas que já tem pra depois adiciona uma nova
        # ter todos os checks de repetir e afins e pipipipopopopo
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   1 - Criar nova matéria                      #############");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        resp2 = input("Escolha uma das opções: ");
    
        if resp2 == 1 :
            os.system("clear");
            materia = str(input("Qual o nome da matéria a ser adicionada?"));
            professor = str(input("Quem ministra essa matéria?"));
    
            # aqui é o lance que Flavius falou pra adicionar um professor também
            # assim com dicionário é mais fácil de acessar
            materias[materia] = {
                "nome": materia,
                "professor": professor
            };
        elif resp2 == 0 :
            # aqui vai ser só um return mesmo não sei ainda como vai funcionar insira módulos i guess
            os.system("clear");
        else :
            print();
            print("#########################################################################################");
            print("############    Você digitou uma opção inválida, voltando ao menu inicial    ############");
            print("#########################################################################################");
            print();
    elif resp1 == "5":
        os.system("clear");
        print("#########################################################################################");
        print("# Aqui estão os horários livres, apenas neles podem ser adicionados um novo compromisso #");
        print("#########################################################################################");
        # vai mostrar a listinha dos horários livres igual no que já tem
        # mas ai tu vai adicionar uma matéria
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   1 - Escolher um dos horários                #############");
        print("#############                   0 - Voltar                                  #############");
        print("#########################################################################################");
        print();
        resp2 = input("Escolha uma das opções: ");
    
        if resp2 == 1 :
            os.system("clear");
            materia = str(input("Qual matéria vai ser adicionada?"));
            horario = str(input("Escolha qual em qual horário a matéria será adicionada. Utilize o formato da universidade (número/letra/números)"));
    
            # esse pedaço aqui todo é pra achar qual o index de onde tá o período da aula
            # se é manhã tarde ou noite no caso
            posicao = 0;
            loop = True
            while loop == True :
                if posicao < horario.count() :
                    if horario[posicao].isalpha() == True :
                        loop = False;
                    else : 
                        posicao += 1;
                else :
                    print("#########################################################################################");
                    print("############   Você digitou um formato inválido, voltando ao menu inicial    ############");
                    print("#########################################################################################");
                    loop = False;

            # aqui quebra a string em 3 pra ter separado certinho o quer
            dias = horario[0:posicao];
            hora = horario[posicao].upper();
            aulas = horario[(posicao+1):];
        
            # aqui só sai metendo as matéria em cada canto mesmo
            for dia in dias :
                for aula in aulas :
                    agenda[dia][hora][aula] = materias[materia];
        elif resp2 == 0 :
            # aqui vai ser só um return mesmo não sei ainda como vai funcionar insira módulos i guess
            os.system("clear");
        else :
            print();
            print("#########################################################################################");
            print("############    Você digitou uma opção inválida, voltando ao menu inicial    ############");
            print("#########################################################################################");
            print();
    elif resp1 == "0":
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