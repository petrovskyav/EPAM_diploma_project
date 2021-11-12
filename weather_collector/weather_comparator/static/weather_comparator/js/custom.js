$(function () {
    $("#setDate").click(function () {
        var today = new Date();
        var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        $('#inputDate').val(date);
    });

    $("#getDate").click(function () {
        var date = new Date($('#inputDate').val());
        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();
        window.location = ("/".concat(year, '/', month, '/', day))
    });
});