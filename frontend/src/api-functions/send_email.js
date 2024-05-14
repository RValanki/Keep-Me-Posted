// send email api function. 
// message: String, subject: String, Contacts: [String]

export let send_email = async (message, subject, contacts, baseURL) => {
    const postRequestString = baseURL + "/api/sendemail" 

    let data = new FormData()
    data.append('message', message)
    data.append('subject', subject)
    data.append('contacts', contacts)

    try {
        const response = await fetch(postRequestString, { method: "POST", body: data})
        const jsonResponse = await response.json()
        return jsonResponse.details;
    } catch (error) {
        console.error("Error:", error)
        return null
    }
}
