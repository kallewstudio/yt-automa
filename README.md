# **Video Cutter - Instruções de Uso**

## **Descrição**
O **Video Cutter** é um aplicativo em Python que permite:
- **Baixar vídeos do YouTube.**
- **Cortar vídeos automaticamente** em clipes ou shorts.
- Ajustar vídeos para o formato **vertical (1080x1920)** com um **fundo desfocado**, ideal para redes sociais.

---

## **Pré-requisitos**
Antes de usar o aplicativo, certifique-se de ter os seguintes itens instalados no seu sistema:

1. **Python 3.10 ou superior**  
   > [Baixar Python](https://www.python.org/downloads/)

2. **Dependências do projeto**  
   Instale as bibliotecas necessárias com o comando abaixo:
   ```bash
   pip install -r requirements.txt

## **Instalação** ##
Clone ou baixe este repositório:

bash
Copiar código
git clone https://github.com/kallewstudio/yt-automa
cd video-cutter
Certifique-se de que o arquivo requirements.txt esteja presente.

Instale as dependências do projeto:

bash
Copiar código
pip install -r requirements.txt

## **Como Usar** ##
1. Executar o aplicativo
Inicie o aplicativo com o comando:

bash
Copiar código
python interface.py
2. Inserir o link do vídeo do YouTube
Cole o link do vídeo que deseja processar no campo indicado.
3. Selecionar o tipo de corte
Short: Clipes de até 59 segundos.
Clipe: Segmentos maiores de 1 minuto.
4. Processar o vídeo
Clique no botão "Processar" e acompanhe os logs no painel.


## **Saída** ##
Os vídeos processados serão salvos na pasta output/, organizada da seguinte forma:

Título do vídeo (nome da pasta):

Exemplo: output/TITULO_DO_VIDEO/
Vídeos cortados:

Nomeados no formato:
Copiar código
YYYYMMDD_HHMMSS_XXX.mp4
Exemplo:
20241119_120345_123.mp4
Formato Final
Proporção Vertical (1080x1920):
Fundo desfocado: Ampliado e ajustado para preencher a tela.
Vídeo original centralizado: Mantendo a proporção original (16:9).
Erros Comuns
1. Erro de bibliotecas
Se encontrar erros de importação ou dependências, execute novamente:

bash
Copiar código
pip install -r requirements.txt
2. Problemas de permissão no sistema operacional
Certifique-se de que o Python tem permissões para criar arquivos e pastas no diretório output/.

3. Erros ao baixar vídeos
Verifique se o link do YouTube é válido.
Certifique-se de que o yt-dlp está atualizado:
bash
Copiar código
pip install --upgrade yt-dlp
Contribuindo
Se você encontrar problemas ou tiver sugestões para melhorias, abra uma issue ou envie um pull request neste repositório.

## **Licença** ##
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## **Contato** ##
Se precisar de ajuda, entre em contato:

Email: kallew182@gmail.com
GitHub: kallewstudio/yt-automa
markdown
Copiar código

---

## **Destaques do Formato** ##
1. **Cabeçalhos bem organizados** para separar seções importantes.
2. **Links úteis**, como o link para download do Python e seu repositório GitHub.
3. **Destaques em listas numeradas e com marcadores**, facilitando a leitura.
4. **Exemplos formatados**, como os nomes dos arquivos de saída.

Você pode copiar e salvar como `README.md` no seu projeto. Se precisar de mais ajustes, é só pedir! 🚀





