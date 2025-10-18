# 🧱 Jogo da Forca — Versão Final (Branch Main)

Este é o **Jogo da Forca em sua versão final e modularizada**, resultado da evolução de várias iterações anteriores do projeto.  
Aqui, o código atinge **maturidade estrutural e técnica**, adotando um design **limpo, extensível e orientado a boas práticas de desenvolvimento em Python**.

---

## ⚙️ Estrutura e Tecnologias Utilizadas

### 🧠 **Conceitos de Programação**
- Programação **Orientada a Objetos (POO)** aplicada de forma modular.
- **Encapsulamento** de responsabilidades por arquivos e classes.
- **Funções e métodos bem definidos**, cada um com papel claro e documentado.
- **Manipulação de listas e strings** para representar o estado do jogo.
- **Controle de fluxo robusto**, garantindo uma experiência fluida no terminal.

### 🧩 **Aspectos Técnicos**
- Arquitetura **modular** com pastas organizadas e separação de responsabilidades:
  - `Game.py` → Lógica central do jogo (classe principal).
  - `hangman.py` → Controle e exibição do desenho ASCII da forca.
  - `terminal.py` → Utilitários para o terminal (limpeza, pausa e mensagens coloridas).
  - `palavras.py` → Banco de palavras.
- **Entrada e saída otimizadas** com tratamento de erros e mensagens contextuais.
- Uso de **códigos ANSI** para colorir mensagens no terminal.
- Dependências exclusivamente **da biblioteca padrão do Python**.

### 🧮 **Conceitos de Software e Boas Práticas**
- Separação clara de **camadas**:
  - Interface de usuário (terminal)
  - Lógica de negócio (classe `Game`)
  - Dados (lista de palavras)
- Aplicação de **Single Responsibility Principle** — cada módulo tem um propósito único.
- Código **limpo e legível**, com tipagem explícita (`list[str]`, `str`, `bool`).
- Estrutura de **loop principal controlado** via `main.py` com inicialização protegida:
  ```python
  if __name__ == '__main__':
      main()
  ```
- **.gitignore** configurado para manter o repositório limpo de arquivos temporários e compilados.

---

## 🕹️ Descrição do Jogo

O jogo segue o mesmo espírito do clássico **Hangman (Forca)**:  
O jogador tenta adivinhar uma palavra oculta, errando o mínimo possível antes que a forca seja completada.

- Cada tentativa exibe a **situação atual da forca**, as **letras descobertas** e as **tentativas erradas**.  
- É possível **chutar uma letra ou a palavra inteira**.  
- Feedback visual e colorido guia o jogador durante o processo.

---

## 📁 Estrutura do Projeto

```
.
├── .gitignore
├── main.py
└── src/
    ├── Game.py
    ├── hangman.py
    ├── palavras.py
    └── terminal.py
```

### 🧱 Descrição dos Módulos

- **main.py**  
  Controla o fluxo principal do jogo. Importa a classe `Game` e executa o loop principal com limpeza e pausa entre tentativas.

- **src/Game.py**  
  Contém a classe `Game`, responsável por toda a lógica: escolha da palavra, controle de erros, validação de tentativas e mensagens.

- **src/hangman.py**  
  Armazena os desenhos ASCII da forca e a função `get_hangman_pose()` para exibir o estágio atual do boneco.

- **src/palavras.py**  
  Banco de palavras que o jogo utiliza para gerar o desafio.

- **src/terminal.py**  
  Utilitários de terminal: funções de limpar tela (`cls`), pausar (`pause`) e imprimir mensagens coloridas (`alertar`, `informar`, `confirmar`).

---

## 🧑‍💻 Execução

Para rodar o jogo, basta executar o arquivo principal:

```bash
python main.py
```

O jogo será executado diretamente no terminal.  
Compatível com **Windows, macOS e Linux** (embora o `pause` e `cls` tenham comportamento otimizado para Windows).

---

## 💬 Exemplo de Interação

```
+---------+
|         |
|         O
|        /|\
|        / \
|
|
|
|
====================
Palavra oculta: _ _ _ _ _
Tentativas erradas: a, e

Faça sua tentativa:
> o
[SUCESSO] Parabéns, a palavra oculta contém a letra 'o', continue assim!
```

---

## 🌱 Evolução do Projeto

Este projeto é o resultado de uma **linha evolutiva** que passou por diferentes versões:  
Cada uma explorou novos conceitos e melhorias, culminando nesta versão modular final.

- 🪓 **Versão 1** — Protótipo procedural básico.  
- 🎨 **Versão 2** — Adição de arte ASCII e modularização funcional.  
- 🧠 **Versão 3** — Reescrita em POO, estruturando o jogo em classes e métodos.  

Essas versões estão disponíveis em **outras branches do repositório**, e vale a pena visitá-las para ver o processo de aprendizado e refatoração que levou até aqui.

---

## ✨ Conclusão

Esta versão representa a consolidação de:
- **Boas práticas de programação Python**  
- **Organização modular e escalável**  
- **Evolução prática de um projeto real**  

Explore as **outras branches** do repositório para acompanhar o crescimento técnico do projeto e entender a transição entre versões.  
Cada uma delas mostra uma etapa da jornada — da simplicidade à estrutura profissional.

---

**Desenvolvido por [Lucca]**  
Estudante de Engenharia da Computação | Analista de Dados  
Explorando Python, modularização e boas práticas de desenvolvimento.

---
