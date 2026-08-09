(function () {
  const scriptUrl = document.currentScript && document.currentScript.src;
  const siteRoot = scriptUrl ? new URL('../', scriptUrl) : new URL('./', document.baseURI);

  function siteUrl(relativePath) {
    return new URL(relativePath, siteRoot);
  }

  function triggerBlobDownload(blob, filename) {
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    setTimeout(() => {
      URL.revokeObjectURL(url);
      link.remove();
    }, 1000);
  }

  async function downloadLocal(relativePath, filename, fallbackType) {
    const response = await fetch(siteUrl(relativePath), { cache: 'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const source = await response.blob();
    const blob = new Blob([source], { type: source.type || fallbackType });
    triggerBlobDownload(blob, filename);
  }

  window.replicantDownloadHtml = function () {
    return downloadLocal('downloads/Replicant-Lab.html', 'Replicant-Lab.html', 'text/html;charset=utf-8')
      .catch(error => alert(`No se pudo descargar el HTML: ${error.message}`));
  };

  window.replicantDownloadPdf = function () {
    return downloadLocal('downloads/Replicant-Lab.pdf', 'Replicant-Lab.pdf', 'application/pdf')
      .catch(error => alert(`No se pudo descargar el PDF: ${error.message}`));
  };

  function addHeaderRepositoryButton() {
    if (document.querySelector('[data-replicant-repository]')) return;
    const palette = document.querySelector('[data-md-component="palette"]');
    if (!palette || !palette.parentNode) return;

    const link = document.createElement('a');
    link.href = 'https://github.com/ratienza/infra-replicant-lab';
    link.className = 'md-header__button md-icon';
    link.setAttribute('data-replicant-repository', '1');
    link.setAttribute('aria-label', 'Repositorio en GitHub');
    link.setAttribute('title', 'Repositorio en GitHub');
    link.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.58 2 12.23c0 4.52 2.87 8.35 6.84 9.71.5.1.68-.22.68-.49l-.01-1.91c-2.78.62-3.37-1.21-3.37-1.21-.45-1.18-1.11-1.49-1.11-1.49-.91-.64.07-.63.07-.63 1 .08 1.53 1.06 1.53 1.06.89 1.57 2.34 1.12 2.91.86.09-.67.35-1.12.63-1.38-2.22-.26-4.56-1.14-4.56-5.06 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.71 0 0 .84-.28 2.75 1.05A9.3 9.3 0 0 1 12 6.93a9.3 9.3 0 0 1 2.5.35c1.91-1.33 2.75-1.05 2.75-1.05.55 1.41.2 2.45.1 2.71.64.72 1.03 1.63 1.03 2.75 0 3.93-2.34 4.8-4.57 5.05.36.32.68.95.68 1.91l-.01 2.8c0 .27.18.59.69.49A10.25 10.25 0 0 0 22 12.23C22 6.58 17.52 2 12 2Z"/></svg>';
    palette.parentNode.insertBefore(link, palette);
  }

  function addHeaderDownloadButton() {
    if (document.querySelector('[data-replicant-downloads]')) return;
    const palette = document.querySelector('[data-md-component="palette"]');
    if (!palette || !palette.parentNode) return;

    const link = document.createElement('a');
    link.href = siteUrl('descargas/').href;
    link.className = 'md-header__button md-icon';
    link.setAttribute('data-replicant-downloads', '1');
    link.setAttribute('aria-label', 'Descargas');
    link.setAttribute('title', 'Descargas');
    link.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5 20h14v-2H5m14-9h-4V3H9v6H5l7 7 7-7Z"/></svg>';
    palette.parentNode.insertBefore(link, palette.nextSibling);
  }

  function init() {
    addHeaderRepositoryButton();
    addHeaderDownloadButton();
  }

  document.addEventListener('DOMContentLoaded', init);
  if (typeof document$ !== 'undefined') document$.subscribe(init);
})();
