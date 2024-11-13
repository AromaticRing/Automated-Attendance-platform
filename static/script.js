const video = document.getElementById('video');
const captureButton = document.getElementById('captureButton');
const attendanceList = document.getElementById('attendanceList');
const viewAttendanceButton = document.getElementById('viewAttendance');

// Access webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(error => console.error('Error accessing webcam:', error));

// Capture image and send to server
captureButton.addEventListener('click', () => {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const dataUrl = canvas.toDataURL('image/jpeg');
    fetch('/capture', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: dataUrl })
    })
    .then(response => response.json())
    .then(data => {
        alert(`Attendance marked for: ${data.name}`);
    });
});

// View attendance
viewAttendanceButton.addEventListener('click', () => {
    fetch('/view_attendance')
    .then(response => response.text())
    .then(data => {
        attendanceList.textContent = data;
    });
});
