function placeOrder(file, color, length, width, height) {
    var form_data = new FormData();
    form_data.append("file", file);
    form_data.append("color", color);
    form_data.append("length", length);
    form_data.append("width", width);
    form_data.append("height", height);

    $.ajax({
        type: 'POST',
        url: '/placeOrder',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: function(data) {
            console.log('Success!');
        },
    });
}