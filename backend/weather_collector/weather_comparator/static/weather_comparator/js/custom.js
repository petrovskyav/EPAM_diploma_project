$(function () {
    $("#setDate").click(function () {
        var today = new Date();
        var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        $('#inputDate').val(date);
    });



    $("#goto_yesterday").click(function () {
        var date = new Date();
        date.setDate(date.getDate()-1);
        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();
        console.log(("/".concat(year, '/', month, '/', day)));
        window.location = ("/".concat(year, '/', month, '/', day))

    });


    $("#getDate").click(function () {
        var date = new Date($('#inputDate').val());
        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();
        window.location = ("/".concat(year, '/', month, '/', day))
    });
});
