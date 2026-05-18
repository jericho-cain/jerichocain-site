const dataPath = "/files/teaching/phys123/labs/galaxy-rotation-lab/data/milkyway.json";

let observed = null;

function visibleMatterCurve(r) {
  return 260 * Math.exp(-r / 5);
}

function darkMatterCurve(r, strength) {
  return strength * (1 - Math.exp(-r / 4));
}

function modelCurve(radii, haloStrength) {
  return radii.map(r => {
    const vVisible = visibleMatterCurve(r);
    const vDark = darkMatterCurve(r, haloStrength);
    return Math.sqrt(vVisible ** 2 + vDark ** 2);
  });
}

function drawPlot(haloStrength) {
  const radii = observed.radius_kpc;
  const model = modelCurve(radii, haloStrength);

  Plotly.react("rotation-plot", [
    {
      x: radii,
      y: observed.velocity_kms,
      mode: "markers+lines",
      name: "Observed Milky Way"
    },
    {
      x: radii,
      y: model,
      mode: "lines",
      name: "Model with dark halo"
    }
  ], {
    xaxis: { title: "Distance from Galactic Center (kpc)" },
    yaxis: { title: "Rotation Speed (km/s)" },
    margin: { t: 30 }
  });
}

  function createReport() {
  const name = document.getElementById("student-name").value || "No name entered";
  const haloValue = document.getElementById("halo-slider").value;

  const questions = [
    {
      prompt: "Describe what happens to the model rotation curve when the dark matter halo strength is increased.",
      answer: document.getElementById("q1").value
    },
    {
      prompt: "At low halo strength, how does the model compare to the observed Milky Way rotation curve in the outer regions?",
      answer: document.getElementById("q2").value
    },
    {
      prompt: "What evidence suggests visible matter alone cannot explain galaxy rotation speeds?",
      answer: document.getElementById("q3").value
    },
    {
      prompt: "Find a halo strength that gives the closest match. Record the value and explain your choice.",
      answer: document.getElementById("q4").value
    },
    {
      prompt: "Does the model perfectly match the observations? Why might real galaxies be more complicated?",
      answer: document.getElementById("q5").value
    }
  ];

  const report = document.getElementById("lab-report");
  report.classList.remove("hidden");

  const plotImage = document
  .getElementById("rotation-plot")
  .getElementsByTagName("svg")[0]
  ?.outerHTML || "<p>Plot image unavailable.</p>";

  report.innerHTML = `
    <h2>Galaxy Rotation and Dark Matter Lab Report</h2>
    <p><strong>Student:</strong> ${name}</p>
    <p><strong>Final halo strength:</strong> ${haloValue}</p>
    <div class="report-plot-container">
      <div class="report-plot">
        ${plotImage}
      </div>
    </div>
    <hr>
    ${questions.map((q, i) => `
      <h3>Question ${i + 1}</h3>
      <p><strong>${q.prompt}</strong></p>
      <p>${q.answer || "No answer entered."}</p>
    `).join("")}
    <button onclick="window.print()">Print or Save as PDF</button>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  const slider = document.getElementById("halo-slider");
  const value = document.getElementById("halo-value");
  const submitButton = document.getElementById("submit-lab");

  submitButton.addEventListener("click", createReport);

  fetch(dataPath)
    .then(response => response.json())
    .then(data => {
      observed = data;

      value.textContent = slider.value;
      drawPlot(Number(slider.value));

      slider.addEventListener("input", () => {
        value.textContent = slider.value;
        drawPlot(Number(slider.value));
      });
    });
});