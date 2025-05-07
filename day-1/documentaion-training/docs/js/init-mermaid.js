document.addEventListener("DOMContentLoaded", () => {
  if (typeof mermaid !== "undefined") {
    mermaid.initialize({ startOnLoad: false });

    const blocks = document.querySelectorAll("pre > code.language-mermaid");
    blocks.forEach((block, index) => {
      const parent = block.parentElement;
      const container = document.createElement("div");
      container.classList.add("mermaid");
      container.innerHTML = block.textContent;

      parent.replaceWith(container);
    });

    // Render Mermaid after replacing blocks
    mermaid.init();
  }
});
