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
/*
给layui table重新渲染时,加载form的input值
 */
function reload_layui_table(){
    var where=getInputToWhere()
    table_render.reload({
        where: where
    });
}
/*
获取form的所有input值给一个数组
 */
function getInputToWhere(){
    var a= $( "form input");
    var where={}
    $.each(a,function(){
        where[this.name] = this.value
    })
    // alert(where)
    return where
}
/*
ajax取数据
 */
function getHandsonTableDate(func,url) {
    var data = {}
    //alert(url)
    $.ajax({
        url: url,
        dataType: "json",
        data:getInputToWhere(),
        success: function (result) {
            //console.log(result)
            //获取数据
            data = result.data;
            func(data);
        },
        error: function () {
            alert("ajax加载失败");
        }
    });
    return data;
}

/**
 * pure ajax get
 */
function ajax_fetch(func,url,param){
    $.ajax({
        url: url,
        dataType: "json",
        data:param,
        success: function (result) {
            console.log(result)
            //获取数据
            var data = result.data;
            //alert("从服务器端获取数据成功.")
            //console.log(data)
            func(data)
        },
        error: function () {
            alert("ajax加载失败.");
        }
    });
}

