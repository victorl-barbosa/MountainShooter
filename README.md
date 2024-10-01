# Mountain Shooter

Este projeto foi desenvolvido como parte dos requisitos para a faculdade. O jogo "Mountain Shooter" é um jogo de tiro em plataforma, com múltiplos níveis e inimigos.

## Descrição

O jogo possui três níveis (Level 1, Level 2, e Level 3) com backgrounds e inimigos diferenciados. O jogador pode escolher entre modos de jogo solo ou cooperativo, e cada nível possui desafios únicos, incluindo inimigos com comportamentos específicos e músicas distintas para cada nível.

## Funcionalidades Implementadas

1. **Menu**: 
   - Inclusão do nome e RU do aluno no canto inferior esquerdo.
   - Opções de novo jogo (1P, 2P cooperativo, 2P competitivo), score e sair.

2. **Level 3**:
   - Aparece entre o Level 2 e a tela de score.
   - Mantém o score dos outros níveis.
   - Possui duração dupla comparada aos Levels 1 e 2.
   - Background exclusivo com efeito de parallax.
   - Música distinta.
   - Novo tipo de inimigo, "Enemy3", com comportamento de movimento único:
     - Move-se horizontalmente da direita para a esquerda.
     - Move-se verticalmente, subindo com velocidade normal e descendo com o dobro da velocidade ao atingir a borda superior da tela.
   - Enemy3 atira e causa dano, com um asset de tiro diferente dos outros inimigos.

## Requisitos do Projeto

1. **Menu com Nome e RU**: Adição do nome "Victor Luiz Caetano Barbosa" e RU "4525758" no canto inferior esquerdo do menu.

2. **Level 3**:
   - Implementação do Level 3 entre os outros níveis e antes do score.
   - Manutenção do score dos níveis anteriores.
   - Duração do Level 3 definida como o dobro dos outros níveis.
   - Adição de um background exclusivo para o Level 3.
   - Inclusão de uma música exclusiva para o Level 3.
   - Implementação de Enemy3 como o único inimigo no Level 3 com movimentação diferenciada.
   
