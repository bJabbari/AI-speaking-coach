const dropzone = document.getElementById("dropzone");
const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const captionEl = document.getElementById("caption");
const responseEl = document.getElementById("response");
const generateBtn = document.getElementById("generateBtn");
const spinner = document.getElementById("spinner");

dropzone.addEventListener("click", () => imageInput.click());
imageInput.addEventListener("change", handleFile);

dropzone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropzone.classList.add("dragover");
});

dropzone.addEventListener("dragleave", () => {
    dropzone.classList.remove("dragover");
});

dropzone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropzone.classList.remove("dragover");
    const file = e.dataTransfer.files[0];
    imageInput.files = e.dataTransfer.files;
    handleFile();
});

function handleFile() {
    const file = imageInput.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        previewImage.src = e.target.result;
        previewImage.style.display = "block";
    };
    reader.readAsDataURL(file);
}

async function generate() {
    const file = imageInput.files[0];
    const band = document.getElementById("bandSelect").value;
    const apiKey = document.getElementById("apiKeyInput").value;

    if (!file) {
        alert("Please upload an image.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("band", band);
    formData.append("api_key", apiKey);


    // Disable button, show spinner
    generateBtn.disabled = true;
    spinner.style.display = "block";
    captionEl.innerText = "";
    responseEl.innerText = "";

    try {
        const res = await fetch("/generate", {
            method: "POST",
            body: formData,
        });

        const data = await res.json();
        captionEl.innerText = data.caption || "(not applicable)";
        if (data.speaking_response && data.speaking_response.trim()) {
            responseEl.innerText = data.speaking_response;
        } else {
            responseEl.innerHTML = '🔐 To enable this section, please provide your own API key from <a href="https://api.together.xyz/" target="_blank">https://api.together.xyz/</a>';
        }
        responseEl.style.display = "block";

    } catch (error) {
        alert("Something went wrong. Please try again.");
    } finally {
        generateBtn.disabled = false;
        spinner.style.display = "none";
    }
}
