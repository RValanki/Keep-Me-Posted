<!-- Summary and Transcipt will be sent after generation page

    The end page when user reaches the end before the summary has generated with transcipt attached

    Author: Parul Garg
    Last Modified: 8/08/2024
-->



<script>
    import Button from "../../components/button.svelte";
    import Topbar from "../../components/topbar.svelte";
    import { ContactsStore } from "../../stores/contacts-store";
    import clock from "../../assets/clock.png"
    import { goto } from "$app/navigation";

    
    //the next page in the sequence
    let nextPage = () => {
        console.log("clicked");
        goto("/upload-audio")
    } 
  
    </script>
    
      <Topbar> </Topbar>
  
      <div class="flex flex-col items-center pt-3 pb-10">
        
  
        <div class="title-container">
          <div class="flex justify-center">
            <img class="flex flex-row justify-center items-center p-0 bg-indigo-200 flex-none order-none flex-grow-0 w-24 h-24" src={clock} alt="Clock" />
          </div>
          <h1 class="pt-3">Your Summary and Transcript Will Be Sent..</h1>
          <p class="subheading">After the summary has been completely generated, it will be sent automatically with the transcript.</p>
        </div>
        
        <div class="all-recipients-container">
          <div class="recipients-txt">Recipients:</div>
    
          <div class="recipients-container">
            
            {#each $ContactsStore as email}
            <div class="email-token">
              <div class="token">{email}</div>
            </div>
          {/each}
          </div>
      </div>
  
      </div>
  
      <div class="button-container">
        <div class="button-holder">
          <Button handleClick={nextPage} text="Send Another Summary"></Button>
        </div>
      </div>

  <style>

  
    .button-container {
      position: absolute;
      right: 45vw;
      bottom: 10px;
    }
  
    .title-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 3%
    }

    .all-recipients-container {
      display: flex;
      gap: 50px;
      padding-top: 3%;

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
    .subtitle {
      padding-bottom: 3%;
    }

    .subheading {
      padding-top: 3%;
    }
    .recipients-txt{
      font-weight: 700;
    }
  
  </style>
