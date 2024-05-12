<script>
    import Button from "../../components/button.svelte";
    import Topbar from "../../components/topbar.svelte";
    import { ContactsStore } from "../../stores/contacts-store";
  
  
    const postRequestString = "http://localhost:5173/emailer/"; 
    // yours may be different, see what link pops up when you run django server, then add /emailer on the end
  
    let emailErrorString= ""
  
    let remove_email = (email) => {
      ContactsStore.update(prev => prev.filter(contact => contact != email))
    };
  
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
      console.log("Send Another Summary")
      // todo
    }
  
  </script>
  
    
      <Topbar> </Topbar>
  
      <div class="content-container">
  
        <div class="title-container">
          <h1>Summary Sent!</h1>
          <h3>Your summary has been sent to the recipients below.</h3>
          <p><strong>Recipients:</strong></p>
        </div>
  
        {#if emailErrorString}
          <div class="caption">{emailErrorString}</div>
        {/if}
  
  
        <div class="recipients-container">
          {#each $ContactsStore as email}
          <div class="email-token">
            <div class="token">{email}</div>
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
      right: 10px;
      bottom: 10px;
    }
  
    .title-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-bottom: 5%;
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
  
    .caption {
      color: crimson;
      padding-bottom: 10px;
    }
  
  
  
  
  </style>
