---
permalink: /download
---

no
<span id='bruh'></span>

<script src="/static/js/jquery-3.6.0.min.js">
<script>
    const params = new Proxy(new URLSearchParams(window.location.search), {
    get: (searchParams, prop) => searchParams.get(prop),
    });
    // Get the value of "some_key" in eg "https://example.com/?some_key=some_value"
    let value = params.guid; // "some_value"
    // document.getElementById('bruh').innerHTML = value;
    var data = $.csv.toObjects("https://github.com/arifhamed/files-001/raw/main/apk.csv"):
    document.getElementById('bruh').innerHTML = data
    // window.open("https://www.google.com", "_self");
</script>