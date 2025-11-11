# Girassol Freitas - Site para GitHub Pages

Este repositório contém um site estático pronto para publicar no GitHub Pages.

## Como publicar
1. Crie um repositório no GitHub.
2. Faça `git init` na pasta local, adicione os arquivos e faça commit:

```bash
git init
git add .
git commit -m "Site Girassol Freitas"
git branch -M main
git remote add origin https://github.com/<seu-usuario>/<seu-repo>.git
git push -u origin main
```
3. No GitHub: Settings → Pages → Source: `main` branch e `/(root)`.

## Como inserir vídeos do Instagram
- Abra o perfil no browser e copie o link da publicação (formato `https://www.instagram.com/p/ID/`).
- Cole essas URLs em `data/insta_posts.json` (um array JSON). A página `instagram.html` tentará carregar os embeds automaticamente.

## Substituir imagens IA
- As imagens IA estão em `assets/images/ai_image_*.png`. Substitua por imagens próprias mantendo os nomes ou altere o HTML.

## PDFs
- Os PDFs originais estão em `assets/`.

## Observação legal
- Esta página contém resumos de leis; para uso jurídico consulte os textos integrais e assessoria jurídica.


---

## Deploy automático (script)
Para enviar o site ao GitHub com as configurações já preparadas, execute:

```bash
./deploy.sh
```

> O script configura a remote `https://github.com/girassolfreitas/girassolfreitas.git` e força o push no branch `main`.

## Domínio personalizado
Adicione o registro CNAME no seu provedor de DNS apontando `www.girassolfreitas.com.br` para `<usuario>.github.io` como instruído pelo GitHub Pages. O arquivo `CNAME` já está incluído no repositório.

## URL final
https://girassolfreitas.github.io/girassolfreitas/  (ou seu domínio personalizado https://www.girassolfreitas.com.br)


---

## Como preencher automaticamente os URLs dos posts do Instagram

Para preencher automaticamente os últimos posts públicos do perfil `@inclusao.gf.oficial` (em seu computador):

1. Certifique-se de ter Python 3 instalado e as bibliotecas `requests` e `beautifulsoup4`:

```bash
pip install requests beautifulsoup4
```

2. Execute o script localizado em `scripts/fetch_instagram_posts.py` na pasta do site:

```bash
python3 scripts/fetch_instagram_posts.py
```

3. O script criará/atualizará o arquivo `data/insta_posts.json` com até 12 URLs públicas de posts. Depois, abra `instagram.html` para ver os embeds.

> Observação: O Instagram pode bloquear requisições automatizadas. Se o script falhar, copie manualmente as URLs das publicações (cada publicação tem o formato `https://www.instagram.com/p/SHORTCODE/`) e cole no arquivo `data/insta_posts.json`.
