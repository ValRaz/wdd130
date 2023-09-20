const newParagraph = document.createElement("p");
newParagraph.innerText = "Added with Javascript!";
document.body.appendChild(newParagraph);
//adds new paragraph element 

const newImage = document.createElement("img");
newImage.setAtteribute("src", "https://picsum.photos/200");
newImage.setAttribute("alt", "Description of image");
document.body.appendChild(newImage);
//adds an image

const newDiv = document.createElement("div");
newDiv.innerHTML = "<ul><li>One</li><li>Two</li><li>Three</li></ul>";
document.body.appendChild(newDiv);
//adds a div with an unordered list

const newSection = document.createElement("section");
newSection.innerHTML = "<h2>CSE 121b</h2><p>Welcome to Javascript Language</p>";
document.body.appendChild(newSection);
//adds a new section with a heading2 and paragraph content
