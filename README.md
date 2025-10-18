# 🎨 Jogo da Forca — Versão 2 (Melhorias Visuais e Estruturais)

Segunda versão do projeto **Jogo da Forca**, aprimorada com **arte ASCII**, **funções mais organizadas** e uma lógica mais fluida.  
Nesta fase, o foco foi tornar o jogo mais **imersivo visualmente** e **estruturado internamente**, preparando o terreno para futuras melhorias.

---

## ⚙️ Especificações Técnicas e Conhecimentos Aplicados

### 🧠 **Conceitos de Programação**
- Reforço da **modularização** com múltiplas funções independentes.
- Controle de fluxo aprimorado, mantendo a mesma base lógica da v1.
- Compreensão mais profunda de **listas**, **loops** e **condições aninhadas**.
- Aplicação de **estruturas de dados visuais (strings multilinha)**.

### 🧩 **Aspectos Técnicos**
- Função `display_hangman(chances)` que renderiza o estágio visual da forca conforme o número de tentativas.
- Lista de palavras ampliada (maior variedade).
- Uso das bibliotecas `random` e `os` como recursos centrais.
- Feedback visual progressivo e mensagens mais interativas.

### 🧮 **Conceitos de Software**
- Introdução de um **modelo MVC rudimentar**:
  - Back-end → lógica do jogo e controle de estado.
  - Front-end → exibição ASCII no terminal.
- Separação clara de **responsabilidades** entre funções.
- Princípios iniciais de **refatoração incremental** e **reutilização de código**.

---

## 🕹️ Descrição do Jogo

Agora o jogador vê a **forca sendo desenhada progressivamente** a cada erro.  
O jogo segue a mesma lógica base: adivinhar a palavra antes que o bonequinho seja “enforcado”.

---

## 📁 Estrutura do Projeto

```
forca-v2.py
├── limpa_tela()
├── display_hangman(chances)
└── game()
```

---

## 🔄 Características da Versão

- Sistema de **arte ASCII dinâmica** conforme o número de erros.  
- Código mais **legível e modular**.  
- Introdução de **funções auxiliares reutilizáveis**.  
- Maior cuidado com mensagens e apresentação no terminal.  
- Mantém o paradigma **procedural**, mas bem mais maduro.

---

## 💡 Limitações

- Lógica de vitória/derrota ainda misturada dentro do loop principal.  
- Sem encapsulamento em classes.  
- Estrutura limitada para expansão (ex: multiplayer, GUI, etc.).

---

## 🧑‍💻 Autor

Desenvolvido por **Lucca**  
Estudante de Engenharia da Computação | Analista de Dados  
Explorando modularização, refatoração e imersão visual no terminal.

---
