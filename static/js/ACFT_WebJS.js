function calculateScore() {
    const gender = document.getElementById('gender').value;
    const age = document.getElementById('age').value;
    const mdl = parseInt(document.getElementById('mdl').value, 10);
    const hrp = parseInt(document.getElementById('hrp').value, 10);
    const spt = parseFloat(document.getElementById('spt').value);
    const sdc = document.getElementById('sdc').value;
    const plnk = document.getElementById('plnk').value;
    const tmr = document.getElementById('tmr').value;

    console.log("Selected gender:", gender);
    console.log("Selected age:", age);
    console.log("Selected mdl:", mdl);
    console.log("Selected hrp:", hrp);
    console.log("Selected spt:", spt);
    console.log("Selected sdc:", sdc);
    console.log("Selected plnk:", plnk);
    console.log("Selected tmr:", tmr);

    const formData = {
        age: age,
        gender: gender,
        mdl: mdl,
        hrp: hrp,
        spt: spt,
        sdc: sdc,
        plnk: plnk,
        tmr: tmr,
    };

    // Send a POST request to acft.py
    fetch('/calculate_acft', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (typeof data === 'string') {
            // If the response is a string, it's an error message
            const errorDiv = document.getElementById('error');
            errorDiv.innerHTML = `Error: ${data}`;
        } else {
            // Otherwise, it's a valid ACFT score
            const acftScore = data.acft_score;
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = `ACFT Score: ${acftScore}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
});}