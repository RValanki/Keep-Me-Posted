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

    /**
     * add_email function is for displaying the user emails in the display field
     */
    let add_email = () =>{
        let emailInputField = document.getElementById("inputEmail");
        let displayField = document.getElementById("display");
        displayField.innerHTML = emailInputField.value;
    }
</script>

<!-- This link is currently used for using google material icons-->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">

      <!-- this style heading class is for making the "Add Recepients" heading centered in the page-->
<style>
    .heading{
        text-align: center;
    }
</style>

<br>

<div class="heading">Add Receipents<br><br><br><br><br><br>
<!-- Below is HTML code for the input field and add button-->
<label for = "email">Enter User Email Address:</label>
<input id="inputEmail" placeholder = "test@example.com">
<!-- on click the add button calls the add_email function-->
<button on:click={add_email}>Add +</button><br><br><br><br><br>


<div id="display" style="width:250px; height:25px; margin:auto; border:2px solid lightgrey; border-radius:60px; align-items:right" >
    <!--The added users will be displayed in this field-->
    <span style="position:fixed">
        <!--The remove user button is created inside the display field-->
    <button style = "height:23px; border-radius:100px; border-color:antiquewhite; background-color: lightgray;cursor:pointer; color:gray; padding:0%; ">
        <i class = "material-icons" style="font-size: 20px;">
            remove
        </i>
    </button>
    </span>

</div>
</div>




