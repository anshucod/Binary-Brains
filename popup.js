document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("checkNews").addEventListener("click", async () => {
    let text = document.getElementById("newsInput").value;

    let response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text })
    });

    let result = await response.json();
    
    // FIX: Use result.fake_news instead of result.prediction
    document.getElementById("result").innerText = 
      result.fake_news ? "🚨 Fake News" : "✅ Real News";
  });
});
