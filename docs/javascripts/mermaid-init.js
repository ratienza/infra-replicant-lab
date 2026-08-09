(function () {
  let sequence = 0;

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'loose',
    theme: 'base',
    fontFamily: 'Arial, sans-serif',
    flowchart: { htmlLabels: true, useMaxWidth: true },
    themeVariables: {
      primaryColor: '#e8f1f8',
      primaryTextColor: '#173f65',
      primaryBorderColor: '#52728d',
      lineColor: '#667085',
      fontSize: '15px'
    }
  });

  async function renderMermaid() {
    const diagrams = [...document.querySelectorAll('.mermaid:not([data-processed="true"])')];

    for (const diagram of diagrams) {
      const source = (diagram.querySelector('code')?.textContent || diagram.textContent).trim();
      const result = await mermaid.render(`replicant-mermaid-${++sequence}`, source);
      diagram.innerHTML = result.svg;
      diagram.dataset.processed = 'true';
      diagram.classList.remove('mermaid');
      diagram.classList.add('mermaid-rendered');
      if (result.bindFunctions) result.bindFunctions(diagram);
    }

    document.documentElement.dataset.mermaid = 'ready';
  }

  renderMermaid().catch(error => {
    document.documentElement.dataset.mermaid = 'error';
    console.error('Mermaid render failed', error);
  });
})();
