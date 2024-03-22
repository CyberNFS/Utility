$(document).ready(function() {
    $('#like_btn').click(function(){
        var buildbuildingIdVar = $(this).attr('data-buildingid');
        
        $.get('/Review/like_building/',
              {'building_name': buildbuildingIdVar},
              
              function(data){
                $('#like_count').html(data);
                $('#like_btn').hide();
              })
    });

});

$(document).ready(function() {
  $('#dislike_btn').click(function(){
      var buildbuildingIdVar = $(this).attr('data-buildingid');
      
      $.get('/Review/dislike_building/',
            {'building_name': buildbuildingIdVar},
            
            function(data){
              $('#dislike_count').html(data);
              $('#dislike_btn').hide();
            })
  });

});
