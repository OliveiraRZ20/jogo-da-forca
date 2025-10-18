# 🪓 Jogo da Forca — Versão 1 (Protótipo)

Primeira versão do clássico **Jogo da Forca**, desenvolvida em Python de forma **procedural e direta**.  
Essa etapa marca o início do projeto, focando na **lógica essencial** do jogo e na estrutura básica do loop de tentativas.

---

## ⚙️ Especificações Técnicas e Conhecimentos Aplicados

### 🧠 **Conceitos de Programação**
- Estruturas de controle fundamentais (`while`, `if/else`, `for`).
- Listas dinâmicas para controle de letras descobertas e erradas.
- Manipulação de strings para verificar acertos.
- Uso da função `input()` para entrada interativa do jogador.
- Compreensão de loops e fluxo lógico de jogo.

### 🧩 **Aspectos Técnicos**
- Biblioteca `random` para escolha aleatória da palavra.
- Função `limpa_tela()` com `os.system("cls" / "clear")` para limpar o terminal.
- Implementação linear, com funções principais:
  - `limpa_tela()` — limpa o terminal.
  - `game()` — controla o fluxo do jogo.
- Primeira aplicação prática de um **loop de estado**: o jogo continua enquanto houver chances.

### 🧮 **Conceitos de Software**
- Estrutura simples, ideal para entender o ciclo de entrada → processamento → saída.
- Início da separação entre lógica e interface de texto.
- Enfoque em legibilidade e entendimento básico da linguagem.

---

## 🕹️ Descrição do Jogo

O jogador deve adivinhar uma palavra secreta chutando letras uma a uma.  
Cada erro consome uma chance. O jogo termina quando o jogador acerta todas as letras ou quando o número de chances se esgota.

---

## 📁 Estrutura do Projeto

```
forca-v1.py
```

---

## 🔄 Características da Versão

- Jogo **funcional**, sem elementos gráficos (sem desenho da forca).  
- Código **linear e didático**, voltado ao entendimento do fluxo básico.  
- Primeira aplicação de **controle de tentativas** e **feedback ao jogador**.  
- Sem modularização complexa — tudo resolvido dentro de um único escopo.

---

## 💡 Limitações

- Ausência de arte ASCII ou elementos visuais.
- Não há encapsulamento de funções nem reaproveitamento de componentes.
- Fluxo de vitória/derrota ainda simplificado.

---

## 🧑‍💻 Autor

Desenvolvido por **Lucca**  
Estudante de Engenharia da Computação | Analista de Dados  
Primeiro passo rumo à estruturação do jogo e aprimoramento da lógica Python.

---
