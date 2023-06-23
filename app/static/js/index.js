const CARDS_HTML = document.getElementById('cards-section');
const input = document.getElementById('input-search');

let timer;

input.addEventListener('input', function () {
  clearTimeout(timer);

  timer = setTimeout(async () => {
    await getCards();
  }, 1000);
});

async function removeAllCards() {
  if (CARDS_HTML.childNodes) {
    while (CARDS_HTML.firstChild) {
      CARDS_HTML.firstChild.remove();
    }
  }
}
async function getCards() {
  await removeAllCards();
  const query = input.value;

  if (!query) {
    return;
  }
  input.disabled = true;

  const response = await loading(getMusics, query);
  const musics = JSON.parse(response);

  for (const music of musics) {
    const card = createCard(music);
    CARDS_HTML.appendChild(card);
  }
  input.disabled = false;
}

async function getMusics(query = '') {
  const response = await fetch(`/music?q=${query}`);
  if (response.status === 200) {
    return response.json();
  }

  throw new Error(response);
}
function createMusicLink(link) {
  const a = document.createElement('a');
  a.href = link;
  a.target = 'blank';
  return a;
}

function createMusicCard(music) {
  const card = document.createElement('div');
  card.classList.add('card');

  const default_jpg = 'https://www.vagalume.com.br/img/artist-default.jpg';

  const capa_html = document.createElement('img');
  capa_html.src = music.capa;
  capa_html.alt = music.band;
  capa_html.setAttribute('onerror', `this.src = '${default_jpg}'`);
  card.appendChild(capa_html);

  const description = document.createElement('div');
  description.id = 'description';

  const band_html = document.createElement('span');
  band_html.innerHTML = `Band: ${music.band}`;
  description.appendChild(band_html);
  description.appendChild(document.createElement('br'));

  const music_html = document.createElement('span');
  music_html.innerHTML = `Music: ${music.title}`;
  description.appendChild(music_html);

  card.appendChild(description);

  return card;
}

function createCard(music) {
  const card = createMusicLink(music.vagalume);

  card.appendChild(createMusicCard(music));

  return card;
}

async function loading(callback, ...args) {
  let response;
  let loading_html;
  try {
    loading_html = createLoading();
    CARDS_HTML.appendChild(loading_html);
    response = await callback(args);
  } catch (error) {
    CARDS_HTML.removeChild(loading_html);
    throw error;
  }
  CARDS_HTML.removeChild(loading_html);
  return response;
}

function createLoading() {
  const loading_html = document.createElement('div');
  loading_html.classList.add('container');
  loading_html.id = 'loading';
  const lds_default = document.createElement('div');
  lds_default.classList.add('lds-default');
  for (let i = 0; i < 12; i++) {
    lds_default.appendChild(document.createElement('div'));
  }
  loading_html.appendChild(lds_default);
  return loading_html;
}
