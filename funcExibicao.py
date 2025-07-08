import os, funcHorarios, funcMaterias;

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

def menuHorariosAtuais(agenda) :
    os.system("clear");
    print("#########################################################################################");
    print("############               Seus horários vagos são os seguintes              ############");
    print("#########################################################################################");
    print();

    funcHorarios.listaHorariosAtuais(agenda, "M");
    funcHorarios.listaHorariosAtuais(agenda, "T");
    funcHorarios.listaHorariosAtuais(agenda, "N");

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

def menuHorariosVagos(agenda) :
    os.system("clear");
    print("#########################################################################################");
    print("############               Seus horários vagos são os seguintes              ############");
    print("#########################################################################################");
    print();

    funcHorarios.listaHorariosVagos(agenda, "M");
    funcHorarios.listaHorariosVagos(agenda, "T");
    funcHorarios.listaHorariosVagos(agenda, "N");

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

def menuMaterias(materias) :
    os.system("clear");
    print("#########################################################################################");
    print("#############               Aqui estão as matérias cadastradas              #############");
    print("#########################################################################################");
    
    funcMaterias.exibeMaterias(materias);

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
    print("#############   Você digitou uma opção inválida, voltando ao menu inicial    ############");
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