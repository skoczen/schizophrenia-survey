  window.VIDEO = window.VIDEO || {};
  VIDEO.max_time_played = 0;
  VIDEO.started_playing = 0;
  VIDEO.wiggle_seconds = 4;

  var tag = document.createElement('script');

  tag.src = "//www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  window.onYouTubeIframeAPIReady = function() {
    VIDEO.player = new YT.Player('player', {
      height: '390',
      width: '640',
      videoId: 'IbL4c_5WrGQ',
      playerVars: { 
        'autoplay': 1,
        'controls': 0,
        'disablekb': 1,
        'rel': 0,
        'showinfo': 0,
        'theme': 'light',
        'modestbranding': 1,
        'color': '00FFAA'
      },
      events: {
        'onReady': VIDEO.onPlayerReady,
        'onStateChange': VIDEO.onPlayerStateChange
    }
});
};

  // Autoplay
  VIDEO.onPlayerReady = function(event) {
    VIDEO.started_playing = true;
    VIDEO.total_length = VIDEO.player.getDuration()
    event.target.playVideo();
    VIDEO.check_interval = setInterval(VIDEO.checkStatus, 500);
};

VIDEO.onPlayerStateChange = function(event) {
    if (event.data === 0 && VIDEO.max_time_played + VIDEO.wiggle_seconds > VIDEO.total_length) {
      VIDEO.has_been_played = true;
      VIDEO.updateInterface();
      clearInterval(VIDEO.check_interval);
  }
};

VIDEO.checkStatus = function() {
    if (VIDEO.player)
        var cur_time = VIDEO.player.getCurrentTime();
    if (cur_time > VIDEO.max_time_played) {
        VIDEO.max_time_played = cur_time;
    }
};

VIDEO.updateInterface = function() {
    if (VIDEO.has_been_played === true) {
        $(".next_button").removeAttr("disabled");
    } else {
        $(".next_button").attr("disabled", "disabled");
    }
};
VIDEO.init = function() {
    if (VIDEO.has_been_played) {
        VIDEO.updateInterface();
    } else {
        VIDEO.started_playing = false;
        VIDEO.updateInterface();
    }
};

$(function(){
  VIDEO.init();

});