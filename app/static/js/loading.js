async function loading(callback, ...args) {
  let response;
  let loading_html;
  try {
    loading_html = createLoading();
    CARDS_HTML.appendChild(loading_html);
    response = await callback(args);
  } catch (error) {
    CARDS_HTML.removeChild(loading_html);
    INPUT.disabled = false;
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
