
    $(document).ready(function() {

        $('.captcha').css({
            'cursor': 'pointer'
        })
        // ajax 刷新
        $('.next-captcha').click(function () {
            console.log('click');
            $.getJSON("/captcha/refresh/",
                function (result) {
                    $('.captcha').attr('src', result['image_url']);
                    $('#id_reg_captcha_0').val(result['key'])
                });


        })

        $('#jsEmailRegBtn').blur(function(){  // #id_captcha_1为输入框的id，当该输入框失去焦点是触发函数
            json_data={
                'response':$('#id_reg_captcha_1').val(),  // 获取输入框和隐藏字段id_captcha_0的数值
                'hashkey':$('#id_reg_captcha_0').val()
            };
            $.getJSON('/ajax_val', json_data, function(data){ //ajax发送
                $('#message').remove();
                if(data['status']){ //status返回1为验证码正确， status返回0为验证码错误， 在输入框的后面写入提示信息
                    $('#jsEmailTips').after('<span id="message" style="color:blue">*验证码正确</span>')
                }else{
                    $('#jsEmailTips').after('<span id="message" style="color:red">*验证码错误</span>')
                };
                if(data['status'] == 0 ){
                    alert(data['status'])
                    return false;
                }
            })

        })

    })
