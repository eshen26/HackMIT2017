# Instant Digest

# Inspiration
As CS students interested in the Fintech industry, we regularly follow daily digest emails from major financial news sources. We are curious about how to combine sentiment analysis using NLP and available financial news on the internet. This prompted us to look into creating a messenger bot that automatically pushes stock trend analyses each morning.

# What it does
At this point in time the messenger bot is scheduled to send a ranking of stocks based on sentiment each morning at 8AM.

# How we built it
We used Heroku to setup the backend server with Node.js, which communicates with the Facebook Messenger API and creates the bot. Selinium is used to launch Chrome and acquire URLs from Google Finance, which then feeds the articles in to IBM Watson to perform sentiment analysis for every firm name that appears. Watson exports a list of firms corresponding to sentiment weights, and is then exported into a JSON file to feed back into Node.js. Node.js parses the JSON file and sends out the text.

# Challenges we ran into
It was our first time working with web development, so Node.js and even git was a big challenge. Development environment was a constant difficulty for us as well.

# What's next for Instant Digest
We are hoping to add interactive NLP features. For instance, when the user texts "Show me the best performing stocks today", Instant Digest will be able to return the Top 3 sentiments of the day.
