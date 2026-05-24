# Das Ramificações à Álgebra: Modelar Sequências

Simulador pedagógico em Python que modela o crescimento da árvore de **Bruno Munari** (do livro *Drawing a Tree*) como uma **sequência geométrica**, cujo termo geral é uma **potência de base 2**: uₙ = 2ⁿ⁻¹.

Desenvolvido para o 8.º ano (tema **Álgebra** — sequências e potências), articulando a Matemática com a Arte e a Natureza.

**Autora:** Celeste Silva · **Versão:** 2.0.0 · **Data:** 2026-04-15

---

## Para que serve

Cada nível da árvore tem o dobro dos ramos do nível anterior. O simulador desenha a árvore nível a nível e mostra, ao lado, os termos da sequência na forma de potência, permitindo **ver** e **validar** a regularidade matemática.

## Como executar

1. É necessário ter o **Python 3** instalado (a biblioteca `turtle` já vem incluída).
2. Descarregue o ficheiro `Simulador_Munari.py` (botão **Code → Download ZIP**, ou abra o ficheiro e transfira-o).
3. Execute com:

   python Simulador_Munari.py

## Como usar na aula (alterar a base e o nível)

Ao iniciar, o simulador pergunta dois valores:

- **Base** (de 2 a 4): número de ramos em que cada ramo se divide.
  - Base 2 → sequência uₙ = 2ⁿ⁻¹
  - Base 3 → sequência uₙ = 3ⁿ⁻¹
  - Base 4 → sequência uₙ = 4ⁿ⁻¹
- **Níveis**: até onde a árvore cresce (máximo 8 para a base 2; 5 para as bases 3 e 4).

No menu, as teclas permitem: **A** — nova árvore · **T** — calcular um termo (uₙ) · **S** — sair.

## Licença e créditos

- **Código:** licença **MIT** (ver ficheiro `LICENSE`) — pode ser usado, modificado e partilhado **desde que se mantenha a atribuição à autora**.

© 2026 Celeste Silva. Inspirado em *Drawing a Tree*, de Bruno Munari.
