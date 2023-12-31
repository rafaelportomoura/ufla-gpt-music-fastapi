async function getMusicCards() {
  await removeAllCards();
  const query = INPUT.value;

  if (!query) {
    return;
  }
  INPUT.disabled = true;

  const response = await loading(getMusics, query);
  const musics = JSON.parse(response);

  for (const music of musics) {
    const card = createCard(music);
    CARDS_HTML.appendChild(card);
  }
  INPUT.disabled = false;
}

async function getMusics(query = '') {
  const response = await fetch(`/api/music?q=${query}`);
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
