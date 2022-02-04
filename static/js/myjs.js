/*
常用工具方法
*/
function StandardPost (url,args)
{
    var form = $("<form method='post' target='_blank'></form>");
    form.attr({"action":url});
    for (arg in args)
    {
        var input = $("<input type='hidden'>");
        input.attr({"name":arg});
        input.val(args[arg]);
        form.append(input);
    }
    $(document.body).append(form);
    form.submit();
}