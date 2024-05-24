<script>
  import Button from "../../components/button.svelte";
  import Topbar from "../../components/topbar.svelte";
  import { ContactsStore } from "../../stores/contacts-store";
  import { goto } from "$app/navigation";

  const postRequestString = "http://127.0.0.1:8000/emailer/"; // yours may be different, see what link pops up when you run django server, then add /emailer on the end

  let emailString = ""
  let emailErrorString= ""
  let contacts = []

  let remove_email = (email) => {
    ContactsStore.update(prev => prev.filter(contact => contact != email))
  };

  let addEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(emailString)) {
      ContactsStore.update(prev => [...prev, emailString])
      emailString = ""
    } else {
      emailErrorString = "Please enter a valid email address."
      setTimeout(() => {
        emailErrorString = "";
      }, 3000);
    }

  }

  let sendEmail = () => {

    let data = new FormData();

    // data.append("message", messageField);
    // data.append("contacts", contacts);

    fetch(postRequestString, { method: "POST", body: data}).then(
      (response) => {
        console.log(response);
      }
    );
  };

  let nextPage = () =>{
    console.log("Go to next page")
    // todo
    goto("/choose_pathway")
  }

</script>

  
    <Topbar> </Topbar>

    <div class="content-container">

      <div class="title-container">
        <h1>Add Recipients</h1>
        <div class="subheading">Add the emails you would like to send the summary to.</div>
      </div>

      <div class="enter-email-container">
      
        <input id="email-input" type="email" placeholder="johndoe@email.com" bind:value={emailString}>
        <Button handleClick={addEmail} icon="../../src/assets/add-icon-blue.png" text="Add recipient" type="secondary"></Button>

      </div>

      {#if emailErrorString}
        <div class="caption">{emailErrorString}</div>
      {/if}


      <div class="recipients-container">
        {#each $ContactsStore as email}
        <div class="email-token">
          <div class="token">{email}</div>
          <button id="remove-button" on:click={remove_email(email)}><img id="remove-icon" src="../../src/assets/remove-icon.png" alt="Remove Icon"></button>
        </div>
      {/each}
      </div>

    </div>

    

    <div class="button-container">
      <div class="button-holder">
        <Button handleClick={nextPage} icon="../../src/assets/arrow-right.png" text="Choose Pathway"></Button>
      </div>
    </div>
    
  

<style> 


  .content-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 2%;
    padding-bottom: 10%;
  }

  .button-container {
    position: absolute;
    right: 30px;
    bottom: 30px;
  }

  .title-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 2%;
    padding-bottom: 5%;
  }

  .enter-email-container {
    display: flex;
    justify-content: center;
    gap: 5px;
    width: 100%;
    font-size: 1rem; /* 16px based on 16px default font size */
    font-weight: normal; /* 400, scale [1,1000] */
    padding-bottom: 5%;
  }

  #email-input {
    width: 40%;
    max-width: 400px;
    padding: 5px;
    border-radius: 8px;
    border: 2px solid #ccc
  }

  .recipients-container {
    display: flex;
    flex-wrap: wrap;
    max-width: 40%;
    gap: 5px;
  }

  .email-token {
    display: flex;
    background-color: #F8F9FC;
    padding: 4px;
    border-radius: 5px;
    justify-content: center;
    align-items: center;
    gap: 3px;
  }
  #remove-button {
    padding: 0;
    border: none;
    background: none;
  }

  #remove-button:hover {
    cursor: pointer;
  }

  #remove-icon {
    height: 10px;
  }

  .caption {
    color: crimson;
    padding-bottom: 10px;
  }

  .subheading{
    margin-top: 3%;
  }


</style>