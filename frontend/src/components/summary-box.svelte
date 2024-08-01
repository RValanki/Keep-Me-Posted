<!-- Summary box component

    Contains the summary generated and the subject

    Author: Diya Ramesh, Brenda Dang
    Last modified: 1/08/2024

-->

<!--  -->
<script>
    export let emailSubject = "Your subject will be generated here...";
    export let summaryGenerated = "Your summary will be generated here..."
</script>

<div class="bg-blue-500 rounded-lg p-4">
    <div>
        <caption>Email Subject</caption>
        <body>{emailSubject}</body>
    </div>
    <div>
        <caption>Summary</caption>
        <caption>{summaryGenerated}</caption>
    </div>
</div>