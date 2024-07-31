<script>
  import Button from "../../components/button.svelte";
  import { ContactsStore } from "../../stores/contacts-store";

  let emailString = "";
  let emailErrorString = "";

  let addEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(emailString)) {
      ContactsStore.update((prev) => [...prev, emailString]);
      emailString = "";
    } else {
      emailErrorString = "Please enter a valid email address.";
      setTimeout(() => {
        emailErrorString = "";
      }, 3000);
    }
  };
</script>

<div class="enter-email-container">
  <input
    id="email-input"
    type="email"
    placeholder="johndoe@email.com"
    bind:value={emailString}
  />
  <Button
    handleClick={addEmail}
    icon="../../src/assets/add-icon-blue.png"
    text="Add recipient"
    type="secondary"
  ></Button>
</div>
