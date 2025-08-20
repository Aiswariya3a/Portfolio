document.addEventListener("DOMContentLoaded", () => {
  // --- Get Live Data from Django ---
  const projectsDataElement = document.getElementById("projects-data");
  const skillsDataElement = document.getElementById("skills-data");

  const projectsData = projectsDataElement
    ? JSON.parse(projectsDataElement.textContent)
    : [];
  const skillsData = skillsDataElement
    ? JSON.parse(skillsDataElement.textContent)
    : [];

  const konamiCode = [
    "ArrowUp",
    "ArrowUp",
    "ArrowDown",
    "ArrowDown",
    "ArrowLeft",
    "ArrowRight",
    "ArrowLeft",
    "ArrowRight",
    "b",
    "a",
  ];
  let konamiIndex = 0;
  let matrixInterval = null;
  let isGameActive = false;

  // MOVED: alphabet is now in the main scope so our keydown listener can access it
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

  const konamiOverlay = document.getElementById("konami-overlay");
  const canvas = document.getElementById("matrix-canvas");
  const ctx = canvas.getContext("2d");
  const gameInfo = document.getElementById("game-info");

  let score = 0;
  let targets = [];

  const startMatrix = () => {
    isGameActive = true;
    score = 0;
    targets = [];
    gameInfo.innerText = "Score: 0";
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const fontSize = 20;
    const columns = Math.floor(canvas.width / fontSize);
    const rainDrops = Array.from({ length: columns }).fill(1);

    const draw = () => {
      ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.font = fontSize + "px monospace";
      ctx.fillStyle = "#04D9FF";
      for (let i = 0; i < rainDrops.length; i++) {
        const text = alphabet.charAt(
          Math.floor(Math.random() * alphabet.length)
        );
        ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
        if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
          rainDrops[i] = 0;
        }
        rainDrops[i]++;
      }
      if (Math.random() < 0.03) {
        targets.push({
          char: alphabet.charAt(Math.floor(Math.random() * alphabet.length)),
          x: Math.floor(Math.random() * columns) * fontSize,
          y: 0,
        });
      }
      ctx.fillStyle = "#F472B6";
      targets = targets.filter((target) => {
        ctx.fillText(target.char, target.x, target.y);
        target.y += fontSize;
        return target.y < canvas.height;
      });
    };
    if (matrixInterval) clearInterval(matrixInterval);
    matrixInterval = setInterval(draw, 50);
  };

  const stopMatrix = () => {
    isGameActive = false;
    if (matrixInterval) clearInterval(matrixInterval);
    matrixInterval = null;
  };

  document.addEventListener("keydown", (event) => {
    if (isGameActive) {
      const keyPressed = event.key.toUpperCase();
      let hit = false;

      // Only process valid alphanumeric keys for the game
      if (alphabet.includes(keyPressed)) {
        for (let i = targets.length - 1; i >= 0; i--) {
          if (targets[i].char === keyPressed) {
            targets.splice(i, 1);
            score += 10;
            hit = true;
            break;
          }
        }

        // NEW: If it was a valid key but didn't hit anything, apply a penalty.
        if (!hit) {
          score -= 5;
        }

        gameInfo.innerText = `Score: ${score}`;
      }

      if (hit) return;
    }

    // Konami Code Logic
    if (event.key === konamiCode[konamiIndex]) {
      konamiIndex++;
      if (konamiIndex === konamiCode.length) {
        konamiOverlay.classList.remove("hidden");
        startMatrix();
        konamiIndex = 0;
      }
    } else {
      konamiIndex = 0;
    }
  });

  konamiOverlay.addEventListener("click", () => {
    konamiOverlay.classList.add("hidden");
    stopMatrix();
  });

  // --- AI Chat Widget ---
  // Find all the necessary HTML elements first
  const chatToggle = document.getElementById("chat-toggle");
  const chatWindow = document.getElementById("chat-window");
  const chatClose = document.getElementById("chat-close");
  const chatMessages = document.getElementById("chat-messages");
  const chatInput = document.getElementById("chat-input");
  const chatSend = document.getElementById("chat-send");

  // This is a safety check: only run the chat script if all elements were found
  if (
    chatToggle &&
    chatWindow &&
    chatClose &&
    chatMessages &&
    chatInput &&
    chatSend
  ) {
    const getBotResponse = (userMessage) => {
      const message = userMessage.toLowerCase();
      if (message.includes("hello") || message.includes("hi")) {
        return "Hello there! I'm Aiswariya's AI assistant. How can I help you today?";
      }
      if (message.includes("how are you")) {
        return "I'm a set of logical rules operating at peak efficiency! Thanks for asking. What would you like to know about Aiswariya?";
      }
      if (message.includes("help")) {
        return "You can ask me about Aiswariya's 'skills', 'projects', 'education', 'internships', or how to 'contact' her.";
      }
      if (message.includes("who are you")) {
        return "I am a digital assistant for Aiswariya S, a Computer Science student specializing in AI. I'm here to answer your questions about her work and experience.";
      }
      if (message.includes("education") || message.includes("college")) {
        return "Aiswariya is completed her B.E. in Computer Science and Engineering at KGISL Institute of Technology (2021-2025), with a CGPA of 8.4.";
      }
      if (message.includes("experience") || message.includes("internship")) {
        return "She has interned as an Innovation Engineer at KG Innovation Lab and as a Web Developer at Exposys Data Labs, where she built AI solutions and responsive websites.";
      }
      if (message.includes("skill")) {
        const skillNames = skillsData.map((skill) => skill.name).join(", ");
        return `Aiswariya's key skills include: ${skillNames}. You can see them all in the 'My Technical Arsenal' section!`;
      }
      if (message.includes("project") || message.includes("work")) {
        const projectTitles = projectsData.map((p) => p.title).join(", ");
        return `She has worked on several exciting projects, including: ${projectTitles}. Which one are you most interested in?`;
      }
      if (message.includes("monitoring") || message.includes("classroom") || message.includes("class")) {
        return "The Classroom Monitoring System uses deep learning to analyze student engagement. It was recognized by NEC Japan and presented at conferences!";
      }
      if (message.includes("chart") || message.includes("captioning")) {
        return "The AI Chart Captioning system used a VGG19 model to detect chart types with 85% accuracy and Google's Gemini API to generate captions.";
      }
      if (message.includes("fake account") || message.includes("detector")) {
        return "The Fake Account Detector was a machine learning model built with TensorFlow and deployed using Django to identify suspicious user profiles.";
      }
      if (message.includes("achievement") || message.includes("award")) {
        return "Her proudest achievements include being a Team Leader at the Smart India Hackathon 2024 Grand Finale and receiving the Special Achiever Award for the 2024-2025 academic year.";
      }
      if (message.includes("contact") || message.includes("email")) {
        return "The best way to get in touch is via the contact form on this page, or by emailing aiswariya3a@gmail.com directly.";
      }
      if (message.includes("thank") || message.includes("bye")) {
        return "You're welcome! Have a great day.";
      }
      if (message.includes("mathi") || message.includes("yuvarajan")) {
        return "Romba kashtam sir....";
      }
      return "That's a great question! I'm a rule-based assistant, so I can best answer questions about Aiswariya's skills, projects, or how to get in contact.";
    };

    const showChat = () => {
      chatWindow.classList.remove("hidden");
      setTimeout(() => {
        chatWindow.classList.remove("chat-hidden");
        chatWindow.classList.add("chat-visible");
      }, 10);
    };

    const hideChat = () => {
      chatWindow.classList.remove("chat-visible");
      chatWindow.classList.add("chat-hidden");
      setTimeout(() => {
        chatWindow.classList.add("hidden");
      }, 300);
    };

    const addMessage = (message, sender) => {
      const messageElement = document.createElement("div");
      messageElement.classList.add("chat-bubble");
      messageElement.classList.add(
        sender === "user" ? "user-message" : "bot-message"
      );
      messageElement.textContent = message;
      chatMessages.appendChild(messageElement);
      chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll
    };

    const handleSendMessage = () => {
      const messageText = chatInput.value.trim();
      if (messageText === "") return;

      addMessage(messageText, "user");
      chatInput.value = "";

      // Simulate bot thinking and reply
      setTimeout(() => {
        const botResponse = getBotResponse(messageText);
        addMessage(botResponse, "bot");
      }, 1000);
    };

    // --- Attach all the event listeners ---
    chatToggle.addEventListener("click", () => {
      const isHidden = chatWindow.classList.contains("hidden");
      if (isHidden) {
        showChat();
      } else {
        hideChat();
      }
    });

    chatClose.addEventListener("click", hideChat);

    chatSend.addEventListener("click", handleSendMessage);

    chatInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        handleSendMessage();
      }
    });
  }
});
