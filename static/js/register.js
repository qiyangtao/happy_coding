
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
                    return false;
                }
            })

        })


        $('#jsSendCode').click(function(){  // #点击发送验证码
            // 验证手机格式
            mobile_partten = /^1[3,5,8,6,8]\d{9}$/;
            mobile = $('#jsPhoneRegCaptcha').val();
            if(mobile_partten.test(mobile)){
                $('#jsRegMobile').after('<span id="message" style="color:red">*手机格式不正确</span>');
                return false;
            }

            json_data={
                'mobile':$('#jsPhoneRegCaptcha').val(),  // 获取输入框和隐藏字段id_captcha_0的数值
            };
            $.getJSON('/sms_sender', json_data, function(data){ //ajax发送
                if(data['status'] == 0){ //status返回0为验证码发送成功， status返回1为验证码发送失败， 在输入框的后面写入提示信息
                    $('#jsPhoneRegCaptcha').after('<span id="message" style="color:blue">*验证码发送成功</span>');
                }else{
                    $('#jsPhoneRegCaptcha').after('<span id="message" style="color:red">*验证码发送失败</span>');
                };
                if(data['status'] == 1 ){
                    alert(data['status']);
                    return false;
                }
            })

        })

    })
