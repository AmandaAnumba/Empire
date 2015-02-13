<script src="{{ url_for('static', filename='plugins/pushmenu/js/classie.js') }}"></script>
<script>
    $(function(){
        

        

        var menuRight = document.getElementById( 'cbp-spmenu-s2' ),
            menuLeft = document.getElementById( 'cbp-spmenu-s1' ),
            showRight = document.getElementById( 'menu-btn' ),
            showLeft = document.getElementById( 'topicsTogg' ),
            closeRight = document.getElementById( 'close-btn' ),
            closeLeft = document.getElementById( 'closeLeft' );
        
        showRight.onclick = function() {
            classie.toggle( this, 'active' );
            classie.toggle( menuRight, 'cbp-spmenu-open' );
            // disableOther( 'showRight' );
        };

        showLeft.onclick = function() {
            classie.toggle( this, 'active' );
            classie.toggle( menuLeft, 'cbp-spmenu-open' );
            // disableOther( 'showRight' );
        };

        closeRight.onclick = function() {
            // classie.toggle( this, 'active' );
            classie.toggle( menuRight, 'cbp-spmenu-open' );
            // disableOther( 'showRight' );
        };

        closeLeft.onclick = function() {
            // classie.toggle( this, 'active' );
            classie.toggle( menuLeft, 'cbp-spmenu-open' );
            // disableOther( 'showRight' );
        };
    });
</script>

if (data['error']) {
                $('#login_error #message').empty().append(data['error']);
                $('#login_error, #main_login_form').show();
            }

            if (data['success']) {
                console.log('error2');
                $('#login_error #message').empty().append(data['login']);
                $('#login_error, #main_login_form').show();
            }

            if (data['username']) {
                console.log('username');
                
                //var str2 = "<img style='width:50px;height:50px;margin-right:10px;' src='" + resp['image']['url'] + "' /> ";
                //str2+= document.getElementById("mainusername").innerHTML;
                var str2 = "Welcome ";
                str2+="<span style='color:#e64c65'>" + data['username'] + "</span>";
                str2+="<a id='empirelogoutbtn' class='btn logout_btn' href='{{ url_for('logout') }}'>Logout</a>";
                document.getElementById("mainusername2").innerHTML = str2;

                jQuery('#login').modal('hide');
                jQuery('#mainusername2').show();
                jQuery('empirelogoutbtn').show();
                document.getElementById("mainusername2").style.display = "block";
                document.getElementById("mainloginbtn").style.display = "none";
                document.getElementById("mainregisterbtn").style.display = "none";
            }