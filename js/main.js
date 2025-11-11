
// Small script to lazy-load Instagram embeds when user clicks the section title
function loadInsta(){
  const el = document.getElementById('insta-embed');
  if(el.innerHTML.trim()===''){
    el.innerHTML = `
      <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/inclusao.gf.oficial/" data-instgrm-version="14" style="background:#FFF; border:0; margin: 1px auto; max-width:540px; padding:0;">
        <a href="https://www.instagram.com/inclusao.gf.oficial/" target="_blank">Visite o perfil @inclusao.gf.oficial</a>
      </blockquote>
      <script async src="//www.instagram.com/embed.js"></script>
    `;
  }
  return false;
}
