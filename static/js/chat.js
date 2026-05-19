document.addEventListener("DOMContentLoaded", () => {
  const chatBtn    = document.getElementById("chatbot-button");
  const chatBox    = document.getElementById("chatbot-container");
  const messagesEl = document.getElementById("chatbot-messages");
  const input      = document.getElementById("chatbot-input");
  const sendBtn    = document.getElementById("chatbot-send");

  if (!chatBtn || !chatBox || !messagesEl || !input || !sendBtn) {
    console.error("Chatbot: falta algún elemento crítico del DOM", {
      chatBtn, chatBox, messagesEl, input, sendBtn
    });
    // No return here: permitimos que la UI mínima funcione si falta closeBtn
  }

  // Abrir / cerrar con toggle
  if (chatBtn) {
    chatBtn.addEventListener("click", () => {
      chatBox.classList.toggle("hidden");
      if (!chatBox.classList.contains("hidden")) input.focus();
    });
  }

  // Delegación global para cerrar (funciona aunque #chatbot-close no exista ahora)
  document.addEventListener("click", (e) => {
    const el = e.target;
    if (!el) return;
    if (el.id === "chatbot-close" || el.closest && el.closest("#chatbot-close")) {
      chatBox && chatBox.classList.add("hidden");
    }
  });

  // Funciones de mensajes (idénticas a las tuyas, con protecciones)
  function addMessage(text, sender = "bot") {
    if (!messagesEl) return;
    const wrapper = document.createElement("div");
    wrapper.className = `chat-msg chat-msg--${sender}`;
    const senderLabel = document.createElement("div");
    senderLabel.className = "chat-msg__sender";
    senderLabel.textContent = sender === "user" ? "Tú" : "Portgas Bot";
    const bubble = document.createElement("div");
    bubble.className = "chat-msg__bubble";
    bubble.textContent = text;
    wrapper.appendChild(senderLabel);
    wrapper.appendChild(bubble);
    messagesEl.appendChild(wrapper);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function showTyping() {
    if (!messagesEl) return;
    removeTyping();
    const typing = document.createElement("div");
    typing.className = "chat-typing";
    typing.id = "chat-typing-indicator";
    typing.innerHTML = "<span></span><span></span><span></span>";
    messagesEl.appendChild(typing);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }
  function removeTyping() {
    const t = document.getElementById("chat-typing-indicator");
    if (t) t.remove();
  }

  function botResponse(userText) {
    userText = (userText || "").toLowerCase();
    if (userText.includes("hola") || userText.includes("buenas") || userText.includes("hey"))
      return "¡Hola! 🔥 Soy Portgas Bot. ¿En qué puedo ayudarte hoy?";
    if (userText.includes("receta"))
      return "Puedo recomendarte recetas según tu objetivo: volumen, definición o pérdida de peso. ¿Cuál es el tuyo?";
    if (userText.includes("ejercicio") || userText.includes("rutina"))
      return "Tenemos ejercicios de fuerza, cardio, HIIT y movilidad. ¿Qué grupo muscular quieres trabajar?";
    if (userText.includes("gimnasio"))
      return "Puedo mostrarte gimnasios disponibles. Visita la sección Gimnasios y filtra por provincia.";
    if (userText.includes("caloría") || userText.includes("proteína") || userText.includes("nutrición"))
      return "En la sección de Recetas puedes filtrar por calorías y proteínas según tus objetivos.";
    if (userText.includes("gracias"))
      return "¡De nada! Sigue encendiendo tu potencial 🔥";
    if (userText.includes("adiós") || userText.includes("adios") || userText.includes("hasta luego"))
      return "¡Hasta pronto! No pares de entrenar 💪";
    return "No estoy seguro de entenderte, pero puedo ayudarte con recetas, ejercicios y gimnasios. ¿Qué necesitas?";
  }

  function handleSend() {
    if (!input || !sendBtn) return;
    const text = input.value.trim();
    if (!text) return;
    addMessage(text, "user");
    input.value = "";
    sendBtn.disabled = true;
    showTyping();
    setTimeout(() => {
      removeTyping();
      addMessage(botResponse(text), "bot");
      sendBtn.disabled = false;
    }, 700);
  }

  if (sendBtn) sendBtn.addEventListener("click", handleSend);
  if (input) input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  });

  setTimeout(() => {
    addMessage("¡Hola! 🔥 Soy Portgas Bot. Pregúntame sobre ejercicios, recetas o gimnasios.", "bot");
  }, 400);
});
