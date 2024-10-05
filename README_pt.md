# honkai-star-rail-helper

`honkai-star-rail-helper` é uma utilidade projetada para gerenciar e processar dados de personagens, habilidades e recomendações de relíquias para o jogo [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail). Ele lê os arquivos de entrada, processa vários atributos, como informações dos personagens e conjuntos de habilidades, e gera os resultados em um formato organizado. Os dados de entrada são provenientes dos pacotes de atualização oficiais no repositório [StarRailData](https://github....

## Última Tabela de Personagens
<!-- CHARACTER_TABLE_START -->
|            |   | A Destruição                        | A Caça              | A Erudição | A Harmonia              | A Inexistência | A Preservação           | A Abundância |
| ---------- | - | ----------------------------------- | ------------------- | ---------- | ----------------------- | -------------- | ----------------------- | ------------ |
| Físico     | 5 | Clara\|Desbrava{M#dor}{F#dora}\|Yunli | Boothill            | Argenti    | Robin                   |                |                         |              |
| Físico     | 4 |                                     | Sushang             |            | Hanya                   | Luka           |                         | Natasha      |
| Fogo       | 5 | Vaga-lume                           | Topaz e Dinheirinho | Himeko     |                         | Jiaoqiu        | Desbrava{M#dor}{F#dora} | Lingsha      |
| Fogo       | 4 | Hook                                |                     |            | Asta                    | Guinaifen      |                         | Gallagher    |
| Gelo       | 5 | Jingliu                             | Yanqing             |            | Ruan Mei                |                | Gepard                  |              |
| Gelo       | 4 | Misha                               |                     | Herta      |                         | Pela           | 7 de Março              |              |
| Raio       | 5 |                                     |                     | Jing Yuan  |                         | Acheron\|Kafka |                         | Bailu        |
| Raio       | 4 | Arlan                               | Moze                | Serval     | Tingyun                 |                |                         |              |
| Vento      | 5 | Blade                               | Feixiao             |            | Bronya                  | Cisne Negro    |                         | Huohuo       |
| Vento      | 4 |                                     | Dan Heng            |            |                         | Sampo          |                         |              |
| Quântico   | 5 |                                     | Seele               | Jade       | Sparkle                 | Loba Prateada  | Fu Xuan                 |              |
| Quântico   | 4 | Xueyi                               |                     | Qingque    |                         |                |                         | Lynx         |
| Imaginário | 5 | Dan Heng - Embebidor Lunae          | Dr. Ratio           |            | Desbrava{M#dor}{F#dora} | Welt           | Aventurine              | Luocha       |
| Imaginário | 4 |                                     | 7 de Março          |            | Yukong                  |                |                         |              |
<!-- CHARACTER_TABLE_END -->

## Principais Funcionalidades
- Baixa automaticamente dados dos personagens, CVs, conjuntos de habilidades e recomendações de relíquias.
- Processa e organiza os dados em diretórios de entrada/saída específicos de cada versão.
- Configuração dos números de versão via linha de comando para cada nova atualização.

## Requisitos

Certifique-se de que você tem o seguinte:
- **Python 3.8+** (confirme com `python3 --version`).
- Pacotes Python necessários listados em `requirements.txt`.

## Instalação

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(Opcional) Criar e ativar um ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scriptsctivate
   ```

3. **Instalar dependências (atualmente não são necessárias dependências adicionais):**
   ```bash
   # Não é necessário instalar dependências por enquanto, mas se necessário no futuro:
   # pip install -r requirements.txt
   ```

## Uso

### Executar a Ferramenta
   Navegue até o diretório `src/` e execute o script principal com o número da versão desejado:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - Substitua `<version_number>` pelo número da versão atual (por exemplo, `2.5`).
   - Se você quiser pular o download dos arquivos, adicione a opção `--skip-download`.

   Os arquivos de entrada serão baixados para a pasta `input/{version}`, e a saída será salva na pasta `output/{version}`.

### Exemplo de Uso

- Para executar o script com a versão `2.5` e baixar os arquivos:
  ```bash
  python3 main.py --version 2.5
  ```

- Para executar o script com a versão `2.5` e pular o download dos arquivos:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- Para executar o script com a versão 2.5 e baixar os arquivos para idiomas específicos (por exemplo, EN e JP):
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## Contribuições

Aceitamos contribuições! Você pode:
- Enviar um pull request para novos recursos ou correções de bugs.
- Relatar problemas através do sistema de issues.
- Certifique-se de que todas as contribuições incluem testes e documentação relevante.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
