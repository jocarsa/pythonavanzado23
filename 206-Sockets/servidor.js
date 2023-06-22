const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);



app.use(express.static(__dirname + '/public'));

io.on('connection', (socket) => {
  console.log('A user connected');
    
  socket.on('movimiento', (msg) => {
    console.log('Received message:', msg);
      var existe = false;
      identificador = 0
      for(var i = 0;i<jugadores.length;i++){
          if(msg.id == jugadores[i].id){
              existe = true;
              identificador = i
          }
      }
      console.log(existe)
      if(existe == false){
          jugadores.push(msg)
      }else{
          jugadores[identificador] = msg
      }
      
    io.emit('movimiento', jugadores); // Broadcast the message to all connected clients
  });

  socket.on('disconnect', () => {
    console.log('A user disconnected');
  });
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
    jugadores = []
});
