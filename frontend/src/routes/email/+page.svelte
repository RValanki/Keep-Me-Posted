<script>
    let postRequestString = "http://localhost:8000/emailer/"  // yours may be different, see what link pops up when you run django server, then add /emailer on the end
    let contacts = []
    let contents = ""

    let buttonPressed = () => {
        let data = new FormData()
        data.append('contents', contents)
        data.append('contacts', contacts)
            
        fetch(postRequestString, {method: 'POST', data: data}).then(response => {
            console.log(response)
        })
    }
</script>

<div>This is where we will add the emails</div>
<button on:click={buttonPressed}>Send email</button>


