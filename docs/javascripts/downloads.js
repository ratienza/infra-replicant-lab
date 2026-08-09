(function () {
  function triggerBlobDownload(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      URL.revokeObjectURL(url);
      a.remove();
    }, 1000);
  }

  async function downloadLocal(path, filename, fallbackType) {
    const response = await fetch(path, { cache: 'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const source = await response.blob();
    const blob = new Blob([source], { type: source.type || fallbackType });
    triggerBlobDownload(blob, filename);
  }

  window.replicantDownloadHtml = function () {
    return downloadLocal('/downloads/Replicant-Lab.html', 'Replicant-Lab.html', 'text/html;charset=utf-8')
      .catch(err => alert(`No se pudo descargar el HTML: ${err.message}`));
  };

  window.replicantDownloadPdf = function () {
    return downloadLocal('/downloads/Replicant-Lab.pdf', 'Replicant-Lab.pdf', 'application/pdf')
      .catch(err => alert(`No se pudo descargar el PDF: ${err.message}`));
  };

  function addHeaderDownloadButton() {
    if (document.querySelector('[data-replicant-downloads]')) return;

    const palette = document.querySelector('[data-md-component="palette"]');
    if (!palette || !palette.parentNode) return;

    const link = document.createElement('a');
    link.href = '/descargas/';
    link.className = 'md-header__button md-icon';
    link.setAttribute('data-replicant-downloads', '1');
    link.setAttribute('aria-label', 'Descargas');
    link.setAttribute('title', 'Descargas');
    link.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5 20h14v-2H5m14-9h-4V3H9v6H5l7 7 7-7Z"/></svg>';

    palette.parentNode.insertBefore(link, palette.nextSibling);
  }

  function init() {
    addHeaderDownloadButton();
  }

  document.addEventListener('DOMContentLoaded', init);
  if (typeof document$ !== 'undefined') document$.subscribe(init);
})();
