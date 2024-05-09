<script>
  const postRequestString = "http://127.0.0.1:8000/emailer/"; // yours may be different, see what link pops up when you run django server, then add /emailer on the end

  let contacts = [];

  let messageField = "";
  let emailField = ""

  let errorMessage = "";
  let confirmationMessage = "";

  let buttonPressed = () => {
    if (!(contacts.length) || !messageField) {
      errorMessage = "Please enter a message and add contacts.";
      // Clear error message after 2 seconds
      setTimeout(() => {
        errorMessage = "";
      }, 2000);

      return
    }

    let data = new FormData();
    contacts = contacts
    messageField = messageField

    data.append("message", messageField);
    data.append("contacts", contacts);

    fetch(postRequestString, { method: "POST", body: data}).then(
      (response) => {
        console.log(response);
        if (response.status == 200) {
          console.log('Email sent successfully')
          confirmationMessage = "Email sent successfully.";
          setTimeout(() => {
            confirmationMessage = "";
          }, 2000);

          contacts = []
          messageField = ""
        } else {
          errorMessage = "Email did not send successfully.";
          setTimeout(() => {
            errorMessage = "";
          }, 2000);
        }
      }
    );
  };

  /**
   * This function is used to remove the email from the array and display when the user clicks the delete
   * @param index
   */
  let remove_email = (index) => {
    contacts.splice(index, 1);
    contacts = contacts;
  };

  /**
   * add_email function is for displaying the user emails in the display field and for adding the user to the contact array
   */
  let add_email = () => {
    if (!emailField.trim()) {
      //This is to display error message when inputfield is empty
      errorMessage = "Please enter email address.";
      // Clear error message after 2 seconds
      setTimeout(() => {
        errorMessage = "";
      }, 2000);
    } else {
      //if input field is not empty then it will be pushed to the contacts list
      contacts.push(emailField);
      emailField = "";
      contacts = contacts;
    }
  };
</script>

<!-- This link is currently used for using google material icons-->
<link
  href="https://fonts.googleapis.com/icon?family=Material+Icons"
  rel="stylesheet"
/>

<body class="container">
  <div class="message">
    <p>Hello welcome to KeepMePosted!</p>
    <textarea placeholder="Enter your message here" bind:value={messageField}></textarea>
  </div>
  <!--If an error message is triggered the error message is displayed-->

  <div class="emails">
    <div class="emails-add">
      <label for="email">Enter Contact's Email Address:</label>
      <input placeholder="test@example.com" bind:value={emailField} />
      <button on:click={add_email}>Add +</button>
    </div>

    <!-- loops through each contact and prints -->
    <div class="emails-list">
      {#each contacts as email, index (index)}
        <div class="emails-item">
          <p>{email}</p>
          <button class="remove-button" on:click={remove_email(index)}>-</button
          >
        </div>
      {/each}
    </div>
  </div>

  <div class="send">
    <button type="button" on:click={buttonPressed}> Send </button>
  </div>

  <div class="alert">
    {#if errorMessage}
      <p id="error">{errorMessage}</p>
    {/if}

    {#if confirmationMessage}
     <p id="confirmation">{confirmationMessage}</p>
    {/if}
  </div>
</body>

<!-- this styling secton contains styles for many components used throughout the page-->
<style>
  body {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 50px;
  }

  textarea {
    width: 100%;
    height: 100px;
  }

  .emails {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 10px;
  }
  .emails-add {
    display: flex;
    gap: 10px;
  }

  .emails-list {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .emails-item {
    display: flex;
    height: 30px;
    gap: 30px;
    align-items: center;
  }

  .remove-button {
    border-radius: 50px;
    border: 3px lightGrey;
    cursor: pointer;
    background-color: lightblue;
    height: 20px;
  }

  .alert {
    width: 100%;
    text-align: center;
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
  }

  #error {
    color: red;
  }

  #confirmation {
    color: green;
  }
</style>
