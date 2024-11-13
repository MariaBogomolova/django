window.onload = function() {
    $('.list-group').on('click', 'a.list-group-item', function(event){
        event.preventDefault();

        var categoryId = $(this).data('category-id');
        console.log(categoryId);

        $.ajax({

            url: 'category/' + categoryId + '/',
            method: 'GET',

            beforeSend: function(xhr) {
               xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            },
            success: function(data) {
                console.log(data);
                $('.filtered_products').html(data.result);
            },
        });

    });
};