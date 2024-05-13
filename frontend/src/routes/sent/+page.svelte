<script>
    import Button from "../../components/button.svelte";
    import Topbar from "../../components/topbar.svelte";
    import { ContactsStore } from "../../stores/contacts-store";
    import greenTick from "../../assets/green-tick.png"
    

    let nextPage = () => {
        console.log("clicked");
    }
  
    </script>
    
      <Topbar> </Topbar>
      <div class="center-icon"><img class="green-tick" src={greenTick} alt="Green Tick" /></div>
  
      <div class="content-container">
  
        <div class="title-container">
          <h1>Summary Sent!</h1>
          <h3>Your summary has been sent to the recipients below.</h3>
          <p><strong>Recipients:</strong></p>
        </div>
  
  
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
  
  .center-icon{
    display: flex;
    justify-content: center;
}

.green-tick{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 0px;
    gap: 9.3px;

    width: 7vw;
    height: width;
    max-width: 100px;
    max-height: 100px;

    background: #D1E9FF;
    border-radius: 93.0233px;

    flex: none;
    order: 0;
    flex-grow: 0;

}
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
