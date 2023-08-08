// Import bolt package (https://www.npmjs.com/package/@slack/bolt)
const { App, LogLevel } = require("@slack/bolt");

// Initializes your app with your bot token and signing secret
const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET,
  logLevel: LogLevel.DEBUG
});

// Listens to incoming messages that contain "hello"
app.message('hello', async ({ message, say }) => {
  // say() sends a message to the channel where the event was triggered
  await say(`Hey there <@${message.user}>!`);
});

app.command("/guesswho", async ({ command, ack, say }) => {
  // Acknowledge command request
  await ack();

  await say(`You initiated a Guess Who game, <@${command.user_id}>!`);
});

// Start your app
(async () => {
  await app.start(process.env.PORT || 3000);

  console.log('⚡️ Bolt app is running!');
})();
