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