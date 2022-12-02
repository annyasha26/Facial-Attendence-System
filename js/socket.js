    console.log("hello world")
    var socket = io();
    console.log("socket",socket)
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
