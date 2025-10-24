# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Padrões de Commit

Todas as mensagens de commit devem seguir o padrão **Conventional Commits** para manter um histórico de mudanças claro e consistente.

### Formato

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

### Tipos Principais

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Mudanças na documentação
- `style`: Formatação, ponto e vírgula faltando, etc (sem mudança de código)
- `refactor`: Refatoração de código
- `test`: Adição ou correção de testes
- `chore`: Manutenção de tarefas, configurações, etc

### Exemplos

```
feat(assignments): adiciona tarefa de estruturas de dados

Cria nova tarefa sobre listas, pilhas e filas com exemplos práticos
e exercícios guiados para os estudantes.
```

```
fix(index): corrige carregamento de tarefas no portal

O bug ocorria quando não havia tarefas com data de entrega próxima.
Adiciona validação para exibir mensagem apropriada.
```

```
docs: atualiza README com instruções de configuração
```

```
style(css): ajusta espaçamento e cores do tema
```

```
refactor: reorganiza estrutura de pastas de templates
```

```
test: adiciona testes para validação de datas
```
