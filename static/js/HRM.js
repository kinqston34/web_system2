

// 員工基本資料
$("#baseQuery").click(()=>{
    
    let template = $("form.query2");
    
    let csrf = $("form.query2 input[name='csrfmiddlewaretoken']").val()
    template.text("");
    template.append(`<input type="hidden" name="csrfmiddlewaretoken" value="${csrf}">`);
    template.append(`<div>在職員工列表</div>`);
    if ($("#mode").val() == "name"){
        template.append(`<label for="name">請輸入員工姓名:</label>
        <input type="text" name="name" />
        <button type="submit" id="dbQuery">查詢</button>`);
    } else if ($("#mode").val() == "id"){
        template.append(`<label for="id">請輸入員工編號:</label>
        <input type="text" name="id">
        <button type="submit" id="dbQuery">查詢</button>`);
    }
});

$("#dbQuery").on("click",()=>{
    alert("ok");
});
