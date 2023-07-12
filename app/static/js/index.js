const CARDS_HTML = document.getElementById('cards-section');
const INPUT = document.getElementById('input-search');

const callbacks = {
  music: getMusicCards,
};

async function verificarEnter(event, callback) {
  if (event.keyCode === 13) {
    event.preventDefault();
    await callbacks[callback]();
  }
}

async function removeAllCards() {
  if (CARDS_HTML.childNodes) {
    while (CARDS_HTML.firstChild) {
      CARDS_HTML.firstChild.remove();
    }
  }
}
