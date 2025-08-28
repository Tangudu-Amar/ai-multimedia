function toggleFields() {
    const type = document.getElementById("file_type").value;
    document.getElementById("imageInput").style.display = (type === "image") ? "block" : "none";
    document.getElementById("audioInput").style.display = (type === "audio") ? "block" : "none";
    document.getElementById("videoInput").style.display = (type === "video") ? "block" : "none";
}

function previewImage(event) {
    hideServerPreview();
    const file = event.target.files[0];
    const maxSizeMB = 20;
    if (file.size > maxSizeMB * 1024 * 1024) {
        alert(`❌ File too large! Max allowed size is ${maxSizeMB}MB.`);
        event.target.value = "";
        document.getElementById('imagePreview').style.display = 'none';
        return;
    }

    const reader = new FileReader();
    reader.onload = function () {
        const output = document.getElementById('imagePreview');
        output.src = reader.result;
        output.style.display = 'block';
    }
    reader.readAsDataURL(file);
}

function previewAudio(event) {
    hideServerPreview();
    const file = event.target.files[0];
    const maxSizeMB = 20;
    if (file.size > maxSizeMB * 1024 * 1024) {
        alert(`❌ File too large! Max allowed size is ${maxSizeMB}MB.`);
        event.target.value = "";
        document.getElementById('audioPreview').style.display = 'none';
        return;
    }

    const audioPreview = document.getElementById('audioPreview');
    audioPreview.src = URL.createObjectURL(file);
    audioPreview.style.display = 'block';
    audioPreview.load(); // Reloads the audio element with new source
}

function previewVideo(event) {
    hideServerPreview();
    const file = event.target.files[0];
    const maxSizeMB = 20;

    if (file.size > maxSizeMB * 1024 * 1024) {
        alert(`❌ File too large! Max allowed size is ${maxSizeMB}MB.`);
        event.target.value = "";
        document.getElementById('videoPreview').style.display = 'none';
        return;
    }

    const videoPreview = document.getElementById('videoPreview');
    videoPreview.src = URL.createObjectURL(file);
    videoPreview.style.display = 'block';
    videoPreview.load(); // Reloads the video element with new source
}

function previewImageFromURL(url) {
    hideServerPreview();
    const image = document.getElementById('imagePreview');
    if (url && (url.startsWith('http://') || url.startsWith('https://'))) {
        image.src = url;
        image.style.display = 'block';
    } else {
        image.style.display = 'none';
    }
}

function hideServerPreview() {
    const serverPreview = document.getElementById('serverPreview');
    if (serverPreview) {
        serverPreview.style.display = 'none';
    }
}

function showLoadingOnButton(form) {
    const button = form.querySelector(".custom-button");
    const spinner = button.querySelector(".button-spinner");
    const text = button.querySelector(".button-text");

    if (spinner && text) {
        spinner.style.display = "inline-block";
        text.textContent = "Analyzing...";
    }

    return true; // IMPORTANT: this allows the form to submit
}

// This is the new function that was missing
function copySummary() {
    const summaryTextarea = document.getElementById("summaryText");
    summaryTextarea.select();
    document.execCommand("copy"); // Still works, but consider the modern API
    alert("Summary copied to clipboard!");
}


// Event listeners to handle the page state
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function () {
            document.getElementById("loading").style.display = "block";
        });
    }

    // Event listener for the Copy button
    const copyButton = document.querySelector(".btn-copy");
    if (copyButton) {
        copyButton.addEventListener("click", copySummary);
    }
});
