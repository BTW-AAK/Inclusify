var generateButton = document.querySelector('#generateButton');

if(generateButton){
// Access your API key (see "Set up your API key" above)
const genAI = new GoogleGenerativeAI(API_KEY);



generateButton.addEventListener('click', function(event) {
console.log("running")
    run();

});

}

const genAI = new GoogleGenerativeAI("AIzaSyDHt49ArGg0gQZWevD3zNzOBQzKtcOTHmM");
async function run() {
    // For text-only input, use the gemini-pro model
    const model = genAI.getGenerativeModel({ model: "gemini-pro"});
    const prompt = "Write a story about a magic backpack."
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
  }
  