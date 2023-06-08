function addToolToDBPressed(){
    let textField = document.querySelector("#title");
    let room = document.querySelector("#room");
    let type = document.querySelector("#type");

    let tool = {
        title: textField.value,
        room: room.value,
        type: type.value,
    }

    fetch(`http://127.0.0.1:8000/save-tool`,{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(tool)
    })
    .then(response => response.json())
    .then(data => console.log(data));
}

function gettool(){
    let container = document.querySelector("#tools-list")

    fetch(`http://127.0.0.1:8000/db-tools`)
    .then(response => response.json())
    .then(data => {
        console.log(data)

        for (let tool of data){
            toolItem = document.createElement("div")
            toolItem.setAttribute("class", "tool-item")
            toolItem.setAttribute("id", tool.id)
            toolItem.textContent = `${tool.id} ${tool.title} ${tool.room} ${tool.type}`;
            container.appendChild(toolItem);
           
            // generate button
            // onclick funcDelete(this)
        }
    });
}

function deleteFromDBPressed(){
    let tool_id = document.querySelector

    fetch(`http://127.0.0.1:8000/delete-tool/${tool_id}`,)
    .then(response => response.json())
    .then(data => console.log(data));
}
