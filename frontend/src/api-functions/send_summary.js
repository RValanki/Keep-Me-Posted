export let send_summary = async (transcript, baseURL) => {
    const postRequestString = baseURL + "/api/summary"; 
    let data = new FormData()
    transcript = transcript
    data.append('transcript', transcript);

    try {
        const response = await fetch(postRequestString, { method: "POST", body: formData });
        const jsonResponse = await response.json();
        return jsonResponse.summary; 

    } catch (error) {
        console.error("Error:", error);
        return null; 
    }
}