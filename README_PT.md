# True-Info — ferramenta simples para obter informação confiável


[![Bandit](https://github.com/LuisGomes18/True-Info/actions/workflows/bandit.yml/badge.svg)](https://github.com/LuisGomes18/True-Info/actions/workflows/bandit.yml)

[![CodeQL](https://github.com/LuisGomes18/True-Info/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/LuisGomes18/True-Info/actions/workflows/github-code-scanning/codeql)

Este projeto ajuda a pesquisar informação sobre um tema, evitando automaticamente sites que você considera pouco confiáveis (por exemplo: sites de desinformação, canais negacionistas, ou fontes que você prefere bloquear).

O foco aqui é praticidade: pessoas não técnicas podem usar o programa pelo menu, sem tocar em código.

Como começar (rápido)

- Abra um terminal na pasta do projeto.
- Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

- Instale dependências:

```bash
pip install -r requirements.txt
```

- Execute o programa:

```bash
python app.py
```

Usando o menu (passo a passo)

Ao iniciar, você verá um menu com opções simples:

- `1 - Fazer pesquisa`: pesquisa um tema e traz resultados filtrados.
- `2 - Adicionar dominio blacklist`: adiciona um site à lista de sites bloqueados.
- `3 - Remover dominio blacklist`: remove um site da lista bloqueada.
- `4 - Ativar lista da blacklist`: ativa uma das listas prontas (por exemplo: Brasil, Portugal).
- `5 - Desativar lista blacklist`: desativa temporariamente uma lista ativa.
- `0 - Sair`: fecha o programa.

O menu guia a entrada — você só precisa digitar o número da opção e seguir as instruções na tela.

Onde ficam as listas

- As listas de sites estão na pasta `data/` (arquivos `.txt`, um domínio por linha).
- É recomendado usar o menu para alterar as listas, assim as mudanças ficam salvas automaticamente.

Recomendações rápidas

- Sempre documente por que um site foi bloqueado (por ex.: link de referência). Use o histórico do Git para registrar mudanças importantes.
- Caso tenha dúvidas, peça a alguém com experiência em verificação de informação para revisar as exclusões.

Informações técnicas e melhorias

Se você for desenvolvedor ou quiser ver sugestões técnicas (como adicionar testes, formatar o código, ou transformar o projeto em pacote), consulte `todo.md` — lá estão as melhorias recomendadas.

Ajuda

Se precisar de ajuda, diga o que tentou fazer e descreva o problema — posso guiar passo a passo.

---
Versão simplificada do README para usuários não técnicos.

Seção técnica (rápida)

Para quem preferir instruções técnicas mais diretas, aqui está um resumo curto e sem complicação.

- Requisitos: `Python 3.8+` e `pip`.
- Abra um terminal na pasta do projeto.
- (Recomendado) crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

- Instale dependências:

```bash
pip install -r requirements.txt
```

- Execute o programa:

```bash
python app.py
```

Dicas rápidas para editar listas

- Editar via menu: rode o programa e use as opções 2–5 para adicionar/remover/ativar/desativar listas sem tocar em arquivos.
- Editar manualmente: abra os arquivos em `data/` e adicione/remova domínios (um por linha). Depois comite as mudanças se quiser salvar o histórico.


Ética e responsabilidade

Ferramentas de filtragem não substituem verificação humana. Use critérios éticos e verificáveis ao construir listas de exclusão. Evite censura indevida; prefira critérios públicos, replicáveis e baseados em evidências.

Contribuições

PRs são bem-vindos. Para mudanças de política de filtragem, descreva critérios e evidências. Para funcionalidades, inclua testes quando possível.
