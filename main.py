import os

#####################################
##### Projeto Class - Versão 1 #####
#####################################

resp1 = '';
while resp1 != '0':
    os.system('clear');
    print("#########################################################################################");
    print("#############                        Projeto SIG-Class                      #############");
    print("#########################################################################################");
    print("#############                   1 - Ver horários atuais                     #############");
    print("#############                   2 - Visualizar matérias                     #############");
    print("#############                   3 - Checar horários vagos                   #############");
    print("#############                   4 - Adicionar matéria                       #############");
    print("#############                   5 - Adicionar horário                       #############");
    print("#############                   0 - Sair                                    #############");
    print();
    resp1 = input("Escolha uma das opções: ");

    if resp1 == '1':   
        print();
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
        print();
        resp2 = input("Escolha uma das opções: ");
    elif resp1 == '2':
        print();
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
        print();
        resp2 = input("Escolha uma das opções: ");
    elif resp1 == '3':
        print();
        print("#########################################################################################");
        print("############               Seus horários vagos são os seguintes              ############");
        print("#########################################################################################");
        # lance tipo horario['materia'] == null ou sei lá como fica em Python
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   0 - Voltar                                  #############");
        print();
        resp2 = input("Escolha uma das opções: ");
    elif resp1 == '4':
        print();
        print("#########################################################################################");
        print("############   Confira suas matérias já existentes antes de criar uma nova   ############");
        print("#########################################################################################");
        # vai mostrar todas que já tem pra depois adiciona uma nova
        # ter todos os checks de repetir e afins e pipipipopopopo
        print();
        print("#########################################################################################");
        print("#############                       O que deseja fazer?                     #############");
        print("#########################################################################################");
        print("#############                   1 - Criar nova matéria                      #############");
        print("#############                   0 - Voltar                                  #############");
        print();
        resp2 = input("Escolha uma das opções: ");
    elif resp1 == '5':
        print();
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
        print();
        resp2 = input("Escolha uma das opções: ");
    elif resp1 == '0':
        print();
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
        input("Escolha uma das opções: ");

print("Fim");