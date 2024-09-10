<script>
  import { onMount } from 'svelte'


  const clientId = import.meta.env.SECRET_CLIENT_ID;

  onMount(async () => {
      const handleCredentialResponse = async (response) => {
          console.log('Encoded JWT ID token: ' + response.credential);
          };
      google.accounts.id.initialize({
          client_id: clientId,
          callback: handleCredentialResponse,
      });
      google.accounts.id.renderButton(
          document.getElementById('buttonDiv'),
          { theme: 'outline', size: 'large' } // customization attributes
      );
      google.accounts.id.prompt();
  });

</script>

<svelte:head>
  <script src="https://accounts.google.com/gsi/client"></script>
</svelte:head>

<main>
  <h1>Demo for <a href=https://stackoverflow.com/questions/72411045/google-auth-oauth-2-0-sveltekit-wierd-behavior>Google Auth OAuth 2.0 SvelteKit wierd behavior</a></h1>

  <p><a href=https://github.com/Leftium/google-signin-kit>View on Github</a></p>

  <div id=buttonDiv></div>
</main>