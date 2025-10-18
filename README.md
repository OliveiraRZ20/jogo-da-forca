# 🧠 Jogo da Forca — Versão 3 (Programação Orientada a Objetos)

Terceira e mais evoluída versão do **Jogo da Forca**, agora totalmente **reescrita em Programação Orientada a Objetos (POO)**.  
Essa fase marca a **maturidade do projeto**, com separação de responsabilidades, encapsulamento e estrutura extensível.

---

## ⚙️ Especificações Técnicas e Conhecimentos Aplicados

### 🧠 **Conceitos de Programação**
- **Classes e Objetos** como base da arquitetura.
- **Atributos de instância** (`self.palavra_atual`, `self.chances`, `self.letras_descobertas`).
- **Métodos especializados** (`tentativa()`, `verifica_win()`, `verifica_end()`, `mostra_tela()`).
- **Encapsulamento** da lógica principal dentro da classe `Hangman`.
- Uso do **paradigma POO** para controlar o fluxo do jogo.
- Melhor uso do `if __name__ == "__main__":` para inicialização segura do programa.

### 🧩 **Aspectos Técnicos**
- Atributo de classe `board` representando os estágios ASCII da forca.
- Métodos claros e coesos, cada um com função específica.
- Controle de estado completo (vitória, derrota, saída).
- Estrutura totalmente **expansível**, preparada para:
  - Interface gráfica.
  - Banco de palavras externo.
  - Ranking e pontuação.

### 🧮 **Conceitos de Software**
- **Reutilização de código** com métodos autoexplicativos.  
- **Organização modular**, fácil de dar manutenção.  
- **Boas práticas de design de software**:
  - Separação entre lógica, entrada e saída.
  - Controle de erros e estados mais previsível.
  - Padrões de design básicos aplicados.

---

## 🕹️ Descrição do Jogo

Mesma dinâmica das versões anteriores — adivinhar a palavra antes de esgotar as chances —  
mas agora com **arquitetura POO**, o que torna o jogo mais limpo, profissional e escalável.

---

## 📁 Estrutura do Projeto

```
forca-v3.py
└── class Hangman:
      ├── __init__()
      ├── limpa_tela()
      ├── tentativa()
      ├── verifica_end()
      ├── verifica_win()
      └── mostra_tela()
```

---

## 🔄 Características da Versão

- Reescrita completa sob paradigma **Orientado a Objetos**.  
- Maior **clareza de propósito** em cada método.  
- Jogo controlado por **loop principal externo**, chamando métodos da classe.  
- Ideal para aprendizado avançado de POO aplicada em jogos de terminal.

---

## 💡 Próximos Passos

- Implementar **ranking de pontuação**.
- Criar **modo multiplayer** (um jogador define a palavra).
- Integrar com **Tkinter ou Pygame** para uma interface gráfica.
- Armazenar estatísticas e progresso localmente.

---

## 🧑‍💻 Autor

Desenvolvido por **Lucca**  
Estudante de Engenharia da Computação | Analista de Dados  
Evoluindo da lógica procedural à POO para criar soluções escaláveis e elegantes em Python.

---
