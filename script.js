let formSchema = [];

function addField(type) {
    const label = prompt("Field Label:", "Question text...");
    if (!label) return;
    formSchema.push({ type, label });
    render();
}

function render() {
    const container = document.getElementById('fields-container');
    container.innerHTML = '';
    formSchema.forEach((f, i) => {
        const div = document.createElement('div');
        div.className = 'field-box';
        div.innerHTML = `<strong>${f.label}</strong><br><input type="${f.type}" disabled style="width:100%; padding:8px; margin-top:5px; border:1px solid #ddd; border-radius:4px;">`;
        container.appendChild(div);
    });
}

async function saveForm() {
    const name = document.getElementById('form-name-input').value;
    const desc = document.getElementById('form-desc-input').value;
    
    if(!name || formSchema.length === 0) {
        alert("Please provide a name and at least one field!");
        return;
    }

    const res = await fetch('/save', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ 
            name: name, 
            description: desc, // NEW FIELD
            fields: formSchema 
        })
    });
    
    if(res.ok) window.location.href = '/';
}