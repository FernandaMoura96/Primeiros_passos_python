import pygame
import time
import random

# --- Configurações Iniciais ---
pygame.init()

# Cores
branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (200, 0, 0)
verde = (0, 200, 0)

# Tamanho da tela
largura_tela = 600
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha Simples')

# Tamanho do bloco e velocidade
tamanho_bloco_cobra = 10
velocidade_cobra = 15

# Objeto relógio para controlar a velocidade do jogo
relogio = pygame.time.Clock()

# Fontes
fonte_estilo = pygame.font.SysFont("bahnschrift", 25)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 20)


# --- Funções do Jogo ---

def sua_pontuacao(pontuacao):
    """Exibe a pontuação atual na tela."""
    texto = fonte_pontuacao.render("Pontos: " + str(pontuacao), True, amarelo)
    tela.blit(texto, [0, 0])


def desenhar_cobra(tamanho_bloco_cobra, lista_cobra):
    """Desenha cada segmento da cobra."""
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_bloco_cobra, tamanho_bloco_cobra])


def mensagem(msg, cor):
    """Exibe mensagens de status na tela (ex: Game Over)."""
    texto = fonte_estilo.render(msg, True, cor)
    tela.blit(texto, [largura_tela / 6, altura_tela / 3])


def loop_jogo():
    """Função principal do loop do jogo."""
    jogo_acabou = False
    fim_de_jogo = False

    # Posição inicial da cabeça da cobra
    x1 = largura_tela / 2
    y1 = altura_tela / 2

    # Mudança de posição (inicialmente parada)
    x1_muda = 0
    y1_muda = 0

    # Lista que armazena os segmentos da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da maçã (aleatória, alinhada à grade)
    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco_cobra) / 10.0) * 10.0

    while not jogo_acabou:

        while fim_de_jogo == True:
            # Tela de Game Over
            tela.fill(preto)
            mensagem("Você Perdeu! Pressione C para Jogar Novamente ou Q para Sair.", vermelho)
            sua_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        jogo_acabou = True
                        fim_de_jogo = False
                    if evento.key == pygame.K_c:
                        loop_jogo()  # Reinicia o jogo

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_acabou = True

            # --- Controle de Movimento ---
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_muda = -tamanho_bloco_cobra
                    y1_muda = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_muda = tamanho_bloco_cobra
                    y1_muda = 0
                elif evento.key == pygame.K_UP:
                    y1_muda = -tamanho_bloco_cobra
                    x1_muda = 0
                elif evento.key == pygame.K_DOWN:
                    y1_muda = tamanho_bloco_cobra
                    x1_muda = 0

        # --- Checagem de Colisão com as Bordas ---
        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            fim_de_jogo = True

        # Atualiza a posição da cabeça
        x1 += x1_muda
        y1 += y1_muda

        # Preenche a tela com a cor de fundo
        tela.fill(preto)

        # Desenha a maçã (alimento)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco_cobra, tamanho_bloco_cobra])

        # Adiciona a nova cabeça à lista de segmentos
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)

        # Remove o último segmento para simular o movimento
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # --- Checagem de Colisão com o Próprio Corpo ---
        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                fim_de_jogo = True

        # Desenha a cobra atualizada
        desenhar_cobra(tamanho_bloco_cobra, lista_cobra)

        # Atualiza a pontuação (o comprimento é -1 porque o 1º segmento é a cabeça)
        sua_pontuacao(comprimento_cobra - 1)

        # Atualiza a tela
        pygame.display.update()

        # --- Lógica de Comer a Maçã ---
        if x1 == comida_x and y1 == comida_y:
            # Gera nova posição da maçã
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco_cobra) / 10.0) * 10.0

            # Aumenta o tamanho da cobra (e, consequentemente, a pontuação)
            comprimento_cobra += 1

        # Controla a velocidade do jogo
        relogio.tick(velocidade_cobra)

    # Sai do Pygame
    pygame.quit()
    quit()


# Inicia o jogo
loop_jogo()