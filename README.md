## Jogo da Forca (CLI) 🎯

Um clássico jogo da forca para o terminal, escrito em Python, com arte ASCII, cores no console e uma lista de palavras em português.

Este projeto é ideal para praticar Python básico (laços, listas, condicionais, I/O) e brincar no terminal. Ele roda nativamente no Windows (usa `cls` e `pause`).

---

### Recursos

- Arte ASCII do boneco em 7 estágios conforme os erros
- Mensagens coloridas (sucesso/aviso/erro) no terminal
- Validação de entrada (só aceita caracteres alfabéticos)
- Palavras em português prontas para uso e fáceis de expandir
- Interface simples e direta, toda no terminal

---

### Requisitos

- Python 3.9 ou superior (usa anotações de tipo modernas como `list[str]`)
- Windows (cmd.exe) — por padrão, o projeto usa `cls` e `pause` do Windows

Observação sobre cores: as cores ANSI funcionam bem no Windows 10/11 (cmd, PowerShell e Windows Terminal). Se as cores não aparecerem, experimente rodar no Windows Terminal ou PowerShell.

---

### Como executar (Windows)

No prompt de comando (cmd):

```bat
cd caminho\para\jogo-da-forca
python --version
python main.py
```

Se você tiver múltiplas versões de Python instaladas, talvez precise usar `py -3.11 main.py` ou similar.

---

### Como jogar

1. O jogo sorteia uma palavra secreta em português.
2. Você pode chutar uma letra por vez ou arriscar a palavra inteira.
3. Cada erro desenha uma parte do boneco (máximo de 6 erros). No 7º estágio, o jogo termina.
4. Você vence ao descobrir todas as letras ou acertar a palavra inteira.

Exemplo de sessão:

```
		+---------+
		|         |
		|         
		|
		|
		|
		|
		|
		|
====================
Palavra oculta: _ _ _ _ _
Tentativas erradas: 
Faça sua tentativa:
> a
[SUCESSO] Parabéns, a palavra oculta contém a letra a, continue assim!
```

---

### Estrutura do projeto

```
├─ main.py                # Ponto de entrada do jogo
├─ testes.ipynb           # Notebook auxiliar (opcional)
├─ src/
│  ├─ Game.py             # Lógica principal do jogo (estado, tentativas, fim)
│  ├─ hangman.py          # Arte ASCII e função get_hangman_pose
│  ├─ palavras.py         # Lista de palavras em português
│  └─ terminal.py         # Utilitários de terminal (cls, pause, cores e mensagens)
```

Principais pontos do código:

- `Game`: controla palavra alvo, letras descobertas, erros e fluxo do jogo.
- `hangman.get_hangman_pose(erros)`: retorna a arte ASCII conforme a contagem de erros.
- `palavras.palavras`: lista de palavras usadas no sorteio.
- `terminal`: limpa a tela, pausa, e exibe mensagens coloridas (info/erro/sucesso).

---

### Personalização

- Adicionar palavras: edite `src/palavras.py` e inclua novos itens na lista `palavras`.
- Alterar a arte/estágios: ajuste `hangmanPoses` em `src/hangman.py`.
- Número de erros: atualmente o limite efetivo é 6 erros (há 7 poses). Se quiser mudar o limite, atualize:
	- a quantidade de poses em `hangmanPoses` e
	- a checagem em `Game.checar_finalizacao()` (condição que compara `self.erros`).
- Mensagens e cores: personalize `mensagem_colorida` e helpers em `src/terminal.py`.

---

### Portabilidade (Linux/macOS)

O projeto está configurado para Windows por padrão (`cls`, `pause`). Para portar:

- Troque `system("cls")` por `system("clear")` em `src/terminal.py`.
- Substitua `system("pause")` por uma pausa equivalente (por exemplo, `input("Pressione Enter para continuar...")`).

---

### Próximos passos (ideias)

- Dificuldades (fácil/médio/difícil) variando o número de erros
- Histórico de partidas e pontuação
- Dicas (ex: primeira e última letra)
- Testes automatizados (pytest) para a lógica do `Game`

---

Made with ❤️ em Python — por OliveiraRZ20
