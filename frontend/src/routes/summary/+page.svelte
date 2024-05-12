<script>
    import { expoInOut } from "svelte/easing";

    const postRequestString = "http://127.0.0.1:8000/summariser/"; // yours may be different, see what link pops up when you run django server, then add /emailer on the end

    let transcript = ""

    let buttonPressed = () =>
    {
        let data = new FormData();
        transcript = transcript
        data.append("transcript", transcript);

        fetch(postRequestString, {
            method: "POST", 
            body: data
        }).then((response) => {
            if (response.status != 200) 
                {
                    console.log('Error: ' + response.status)
                    console.log(response)
                    document.getElementById("summary").innerHTML = "Error: " + response.text()
                }
            return response.json()
        }).then((data) => {
            if (data){
                if (data.summary){
                document.getElementById("summary").innerHTML = data.summary
                }
            }
            else{
                console.log(data)
            }
        })
    }
</script>

<body>
    <h1>Summariser</h1>
    <textarea bind:value={transcript} placeholder="Enter your transcript here" rows="10"></textarea>
    <button on:click={buttonPressed}>Summarise</button>
    <p id="summary"></p>
</body>