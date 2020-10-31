# Twitter-Bot

A Twitter Bot that can tweet, like, retweet, and follow. It searches up the top tweets using a certain hashtag, then likes and retweets them, and follows the twitter user.

## Instructions
* Clone the repository
* Go to [Twitter Developer](https://developer.twitter.com) and sign in with your account/bot account
* Apply for a developer account and select "Making a bot"
* Fill out all the associated account info on the next page
* Answer the questions on the following page, answering how will you use the twitter API (Answer thoroughly, as twitter has to approve your request)
* On the next page, answer no for all the questions, except the second "Will your app use Tweet, Retweet...", and answer that it will
* Review and accept the Terms and conditions, and then confirm your email
* Await your approval, and once approved, create a new app
* Fill out all the info (name, description...)
* If you are greeted with a screen that shows three keys (or random characters with a copy to clipboard button), proceed.
* You might be greeted with the "View endpoints tutorial," just skip that
* Once your app is done, under app permissions, change the app permissions to read, wright, and dm
* Because you have changed app permissions, you might have to regenerate all the keys
* Go back to the project folder
* Make sure to have Python3 installed
* Open a command line interface and download twitter's API "tweepy" by typing in the command line within the project folder `pip install tweepy` or `pip3 install tweepy`
* Once installed, open the project folder in an IDE of your choice or VS Code
* Finally, go to the keys and tokens tab, view the keys, and copy them into the string variables (replacing each "XXX") respectively
* Run the code, or host it somewhere to run automatically
