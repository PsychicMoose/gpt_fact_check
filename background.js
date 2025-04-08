chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
      id: "fact-check",
      title: "Fact Check with GPT",
      contexts: ["selection"]
    });
  });
  
  chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "fact-check") {
      console.log("Context menu clicked. Selected text:", info.selectionText);
  
      fetch("http://127.0.0.1:5005/fact-check", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: info.selectionText })
      })
        .then(res => res.json())
        .then(data => {
            chrome.notifications.create({
              type: "basic",
              iconUrl: "icon.png", // you can use any 128x128 icon here
              title: "GPT Verdict",
              message: data.verdict
            });
          })
          
        .catch(err => {
          alert("Error contacting GPT backend: " + err.message);
        });
    }
  });
  
  