// send email api function. 
// message: String, subject: String, Contacts: [String]

export let send_email = (message, subject, contacts) => {
    const postRequestString = "http://localhost:8000/emailer/" // may be different for your machine

    let data = new FormData()
    data.append('message', message)
    data.append('subject', subject)
    data.append('contacts', contacts)

    fetch(postRequestString, { method: "POST", body: data}).then((response) => {
          console.log(response);
          // do something with response
        }
      );
}
