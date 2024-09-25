import redis from 'redis';

const client = redis.createClient({
  host: '127.0.0.1', // Host address
  port: 6379,        // Port number
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
