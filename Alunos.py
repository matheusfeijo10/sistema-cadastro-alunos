import os
import subprocess
from time import sleep

RESET = "\033[0m"
BOLD = "\033[1m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

alunos = []


def limpar_tela():
    if os.name == "nt":
        subprocess.run("cls", shell=True, check=False)
    else:
        subprocess.run("clear", shell=True, check=False)


def efeito_carregamento(mensagem="Carregando"):
    limpar_tela()
    print(f"\n{AMARELO}{mensagem}...{RESET}", end="", flush=True)
    for _ in range(3):
        sleep(0.3)
        print(f"{AMARELO}.{RESET}", end="", flush=True)
    print("\n")


def pausar_para_leitura():
    input(f"\n{CYAN}Pressione [ENTER] para continuar...{RESET}")


def adicionar_aluno():
    efeito_carregamento("Carregando formulário")
    print(f"{AZUL}{BOLD}{'=' * 35}")
    print("         CADASTRAR ALUNO         ")
    print(f"{'=' * 35}{RESET}")

    while True:
        nome = input(f"\n{BOLD}Nome do aluno:{RESET} ").strip()
        if nome:
            break
        print(f"{VERMELHO}O nome não pode ser vazio.{RESET}")

    while True:
        try:
            idade = int(input(f"{BOLD}Idade do aluno:{RESET} ").strip())
            if idade >= 0:
                break
            print(f"{VERMELHO}A idade não pode ser negativa.{RESET}")
        except ValueError:
            print(f"{VERMELHO}Digite um número inteiro válido.{RESET}")

    while True:
        try:
            nota = float(
                input(f"{BOLD}Nota final (0.0 a 10.0):{RESET} ").replace(
                    ",", "."
                )
            )
            if 0 <= nota <= 10:
                break
            print(f"{VERMELHO}A nota deve estar entre 0.0 e 10.0.{RESET}")
        except ValueError:
            print(f"{VERMELHO}Digite um número válido (ex: 8.5).{RESET}")

    aluno = {"nome": nome, "idade": idade, "nota": nota}

    efeito_carregamento("Salvando")
    alunos.append(aluno)

    print(f"{VERDE}Aluno '{nome}' cadastrado com sucesso.{RESET}")
    pausar_para_leitura()


def listar_alunos():
    efeito_carregamento("Buscando registros")

    if not alunos:
        print(f"{AMARELO}Nenhum aluno cadastrado.{RESET}")
        pausar_para_leitura()
        return

    print(f"{AZUL}{BOLD}{'=' * 50}")
    print("             LISTA DE ALUNOS             ")
    print(f"{'=' * 50}{RESET}")

    for i, aluno in enumerate(alunos, start=1):
        cor_nota = VERDE if aluno["nota"] >= 6 else VERMELHO
        print(
            f"  {CYAN}{i}.{RESET} Nome: {BOLD}{aluno['nome']:<20}{RESET} | Idade: {aluno['idade']:<2} | Nota: {cor_nota}{aluno['nota']:.1f}{RESET}"
        )

    print(f"{AZUL}{'-' * 50}{RESET}")
    print(f"{BOLD}Total de registros:{RESET} {len(alunos)}")
    pausar_para_leitura()


def buscar_aluno():
    efeito_carregamento("Iniciando busca")

    if not alunos:
        print(f"{AMARELO}Nenhum aluno cadastrado.{RESET}")
        pausar_para_leitura()
        return

    nome_busca = input(f"{BOLD}Digite o nome para buscar:{RESET} ").strip()

    efeito_carregamento(f"Procurando por '{nome_busca}'")

    encontrados = [
        aluno for aluno in alunos if nome_busca.lower() in aluno["nome"].lower()
    ]

    if encontrados:
        print(f"{VERDE}{len(encontrados)} registro(s) encontrado(s):{RESET}\n")
        for aluno in encontrados:
            cor_nota = VERDE if aluno["nota"] >= 6 else VERMELHO
            print(
                f"  • Nome: {BOLD}{aluno['nome']}{RESET} | Idade: {aluno['idade']} anos | Nota: {cor_nota}{aluno['nota']:.1f}{RESET}"
            )
    else:
        print(f"{VERMELHO}Nenhum aluno encontrado com '{nome_busca}'.{RESET}")

    pausar_para_leitura()


def remover_aluno():
    efeito_carregamento("Carregando")

    if not alunos:
        print(f"{AMARELO}Nenhum aluno cadastrado.{RESET}")
        pausar_para_leitura()
        return

    nome_busca = input(
        f"{BOLD}Digite o nome do aluno para remover:{RESET} "
    ).strip()

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            confirmacao = (
                input(
                    f"{AMARELO}Deseja remover '{aluno['nome']}'? (s/n):{RESET} "
                )
                .strip()
                .lower()
            )

            if confirmacao == "s":
                efeito_carregamento("Excluindo")
                alunos.remove(aluno)
                print(
                    f"{VERDE}Aluno '{aluno['nome']}' removido com sucesso.{RESET}"
                )
            else:
                print(f"{MAGENTA}Remoção cancelada.{RESET}")

            pausar_para_leitura()
            return

    efeito_carregamento("Verificando")
    print(f"{VERMELHO}Nenhum aluno encontrado com o nome '{nome_busca}'.{RESET}")
    pausar_para_leitura()


def mostrar_media_geral():
    efeito_carregamento("Calculando")

    if not alunos:
        print(f"{AMARELO}Nenhum aluno cadastrado.{RESET}")
        pausar_para_leitura()
        return

    soma_notas = sum(aluno["nota"] for aluno in alunos)
    media = soma_notas / len(alunos)
    cor_media = VERDE if media >= 6 else VERMELHO

    print(f"{AZUL}{BOLD}{'=' * 40}")
    print("        DESEMPENHO GERAL DA TURMA       ")
    print(f"{'=' * 40}{RESET}")
    print(f"  • Alunos avaliados: {BOLD}{len(alunos)}{RESET}")
    print(f"  • Média Geral: {cor_media}{BOLD}{media:.2f}{RESET}")
    print(f"{AZUL}{'=' * 40}{RESET}")

    pausar_para_leitura()


limpar_tela()
efeito_carregamento("Iniciando sistema")

while True:
    limpar_tela()
    print(f"{CYAN}{BOLD}{'=' * 35}")
    print("          SISTEMA ESCOLAR        ")
    print(f"{'=' * 35}{RESET}")
    print(f"  {BOLD}1.{RESET} Adicionar aluno")
    print(f"  {BOLD}2.{RESET} Listar alunos")
    print(f"  {BOLD}3.{RESET} Buscar aluno")
    print(f"  {BOLD}4.{RESET} Remover aluno")
    print(f"  {BOLD}5.{RESET} Média geral")
    print(f"  {BOLD}6.{RESET} Sair")
    print(f"{CYAN}{'=' * 35}{RESET}")

    opcao = input(f"\n{BOLD}Opção (1-6):{RESET} ").strip()

    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        buscar_aluno()
    elif opcao == "4":
        remover_aluno()
    elif opcao == "5":
        mostrar_media_geral()
    elif opcao == "6":
        efeito_carregamento("Encerrando")
        print(f"{VERDE}Programa encerrado.{RESET}")
        break
    else:
        print(f"\n{VERMELHO}Opção inválida.{RESET}")
        sleep(1.2)