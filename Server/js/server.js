
const express = require( 'express' );
const path = require( 'path' )

const app = express();

const http = require('http').Server(app);
const io = require('socket.io')(http);


io.on('connection', (socket) => {
  console.log( 'a user connected' );
  socket.on('disconnect', () => {
    console.log('user disconnected');
  });
  socket.on( 'data', (data) =>{
    console.log( "Message :"+ data );
    const message="Hi Ennakouri My name is Reda"
    socket.emit('response',message)
    console.log( "Response :"+ message );
  })
} );
  

http.listen(6001, () => {
  console.log('listening on *:6001');
} );


