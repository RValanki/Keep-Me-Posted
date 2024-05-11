<script>
  import Button from "../../components/button.svelte"
  import Topbar from "../../components/topbar.svelte";

  const postRequestString = "http://127.0.0.1:8000/emailer/"; // yours may be different, see what link pops up when you run django server, then add /emailer on the end


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
  }

</script>

  
    <Topbar> </Topbar>

    <div class="content-container">

      <div class="title-container">
        <h1>Add Recipients</h1>
        <h3>Add the emails you would like to send the summary to.</h3>
      </div>

      <div class="enter-email-container">enter email container </div>

      <div class="recipients-container">recipients container </div>

    </div>

    <div class="button-container">
      <Button handleClick={nextPage} icon="../../src/assets/arrow-right.png" text="Choose Pathway"></Button>
    </div>
    
  

<style> 


  .content-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 5%;
    padding-bottom: 5%;
  }

  .button-container {
    display: flex;
    justify-content: end;
  }

  .title-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }



</style>