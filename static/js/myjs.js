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
 * 用ajax调用后台服务
 * @param func 回调函数
 * @param url svc地址
 * @param param 入参
 * @param refresh_page 成功是否刷新页面,默认刷新
 */
function ajax_svc(func,url,param,refresh_page=true){
    $.ajax({
        url: url,
        dataType: "json",
        data:param,
        success: function (result) {
            console.log(result)
            //获取数据
            var data = result.data;
            var svc_code = result.svc_code
            //alert(svc_code)
            if(svc_code==100 & refresh_page){
                location.reload();
            }
            //alert("从服务器端获取数据成功.")
            //console.log(data)
            if (func != null){
                func(data)
            }
        },
        error: function () {
            alert("ajax调用服务失败.");
        }
    });
}

/**
 *
 */
function ajax_call(url,param){
    ajax_fetch(null,url,param)
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
            if (func != null){
                func(data)
            }
        },
        error: function () {
            alert("ajax加载失败.");
        }
    });
}

/**
 * pure html ajax get
 */
function html_ajax_fetch(func,url,param,handsonTable){
    $.ajax({
        url: url,
        type:"GET",
        data:param,
        success: function (result) {
            //console.log(result)
            //alert("从服务器端获取数据成功.")
            if (func != null){
                func(result,handsonTable)
            }
        },
        error: function () {
            alert("ajax加载失败.");
        }
    });
}
/**
 * 将腾讯返回数据转化为字典
 * @param data
 * @returns {*|{}}
 */
function tengxunStockDataToDict(data){
    dataArray = data.split(";");
    stockDataDict = {}
    for (let i = 0; i < dataArray.length; i++) {
        stockData = dataArray[i].trim()
        if (stockData.length == 0) continue;
        let allParts  = stockData.split("~")
        let code = allParts[2]
        //let name = allParts[1]
       // let price = allParts[3]
       // let exchange = allParts[38]
        //let amount = allParts[37]
       // let zd = allParts[32]//涨跌幅
       // let captial = allParts[45]
        //alert(name+' 最新价 '+price+' 最新市值 '+captial
        //+ ' 换手 '+exchange+' 当日成交金额 '+amount +' 涨跌幅 '+zd+"%")
        stockDataDict[code]={
            'code':code,
            'name':allParts[1],
            '最新':allParts[3],
            '涨幅':allParts[32],
            '换手':allParts[38],
            '金额':allParts[37],
            '总市值':allParts[45],
        }
    }
    return stockDataDict
}
/**
 * 转换代码为腾讯行情查询字符串,要用,号分割
 * @param codes
 * @returns {string}
 */
function txQueryCodeStr(codes){
    var codeStr =''
    for(i = 0; i < codes.length; i++) {
        code = headCode(codes[i]);
        codeStr+=code+','
    }
    return codeStr
}
/**
 * 为代码增加市场代码头
 * @param code
 * @returns {string}
 */
function headCode(code){
    if (code>='400000'){
        return 'sh'+code;
    }else{
        return 'sz'+code;
    }
}
/**
 * 从handsontable中取得要刷新的代码
 * @param handsonTable
 * @returns {string}
 */
function getQueryCodes(handsonTable){
    hotData = handsonTable.getData()
    var codes = []
    $.each(hotData, function(key, val) {     //以jQuery对象的方法调用，兼容性好;也可以用$(a)将a转化为jquery对象，然后以$(a).each(function(){})的形式调用,下面的方法同
        codes.push(val[0])
    });
    //codes.shift()
    codeStr = txQueryCodeStr(codes)
    return codeStr
}

