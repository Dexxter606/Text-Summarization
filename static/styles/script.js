const selectedText = document.querySelector("#test");

const selection1 = document.querySelector("#option1");
const selection2 = document.querySelector("#option2");

var select = "";

selection1.addEventListener("click", (e) => {
  e.preventDefault();
  select = selection1.value;
});

selection2.addEventListener("click", (e) => {
  e.preventDefault();
  select = selection2.value;
});

if (selectedText) {
  selectedText.addEventListener("click", function (event) {
    event.preventDefault();
    document.getElementById("textarea").value = select;
  });
} else {
  console.log("nahi chala");
}
