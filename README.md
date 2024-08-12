# Discord-bots
Butler, a Discord bot that acts as an intermediate to Wikipedia, will directly give snipped answers in the Discord server. Pinger that is used to send n number of notifications or pings to the destined user. A selenium code that essentially does timely inputs to complete one of the mini-games in Discord

### Butler
  1. uses the Discord and Wikipedia library to get connections to both of them
  2. We access all messages and check for particular keystrokes to activate the bot
  3. Upon activation the key content will be sliced and searched on Wikipedia
  4. A snip of the answer provided by Wikipedia will then be displayed on the server
  5. uses Flask to check if the connection is established to the actual server
  6. we use a free hosting server and host the entire repository for a functional discord bot that can then be invited to the desired server

### Pinger
  1. uses the Discord library to get a connection
  2. We access all messages and check for particular keystrokes to activate the bot
  3. Upon activation the logger key of the user will be looped n number of times
  3. uses Flask to check if the connection is established to the actual server
  4. we use a free hosting server and host the entire repository for a functional discord bot that can then be invited to the desired server

### Selenium game cheat
  1. uses the selenium library and with given inputs, will log in to your account
  2. Will type out the particular strings infinitely till the end of the game
  3. It can easily be run locally, or be hosted on a free platform for infinite use 
