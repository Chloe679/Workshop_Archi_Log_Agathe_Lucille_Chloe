// 🐟 Le Poisson Steve — commande secrète : taper "steve" n'importe où
(function () {
  const SECRET = "steve";
  let buffer = "";
  let audio = null;
  let toast = null;

  document.addEventListener("keydown", function (e) {
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;

    // Espace = stop
    if (e.key === " " && audio) {
      e.preventDefault();
      arreter();
      return;
    }

    buffer += e.key.toLowerCase();
    if (buffer.length > SECRET.length) {
      buffer = buffer.slice(-SECRET.length);
    }
    if (buffer === SECRET) {
      lancerLePoissonSteve();
      buffer = "";
    }
  });

  function arreter() {
    audio.pause();
    audio.currentTime = 0;
    audio = null;
    if (toast) {
      toast.remove();
      toast = null;
    }
  }

  function lancerLePoissonSteve() {
    audio = new Audio("/static/poisson_steve.mp3");
    audio.play();

    toast = document.createElement("div");
    toast.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: rgba(0,0,50,0.9);
      color: cyan;
      font-family: monospace;
      font-size: 0.9rem;
      padding: 10px 16px;
      border-radius: 6px;
      border: 1px solid cyan;
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 12px;
    `;

    const texte = document.createElement("span");
    texte.textContent = "🐟 poisson steve activé  [espace pour stopper]";
    toast.appendChild(texte);

    const boutonStop = document.createElement("button");
    boutonStop.textContent = "✕";
    boutonStop.style.cssText = `
      background: none;
      border: 1px solid cyan;
      color: cyan;
      font-family: monospace;
      cursor: pointer;
      padding: 2px 7px;
      border-radius: 4px;
    `;
    boutonStop.addEventListener("click", arreter);
    toast.appendChild(boutonStop);

    document.body.appendChild(toast);
  }
})();
