import requests


headers = {
"content-type": "application/json"
"authorization" : "Bearer BQD1nKNAZK7CQ7PKAIHJnQENDaN3uslbI11bno4K_Ae1DgmCtoqBPPEJv1I5f9N_tYRZb8i2SGz80ZSlInAXpvZGLhGjYIWIGYpUzyVSd3KbKuQ69q9ScOqrqTvu9xlshS6tJfKrbCqWWiE1WO2NF1D67luzWNqRjkGxupszXOnixqwstpoC"
}
url = "https://artists.spotify.com/c/artist/7KzG8dszzwlSDGEsCbzANz/music/playlists"

requests.get(url, headers=headers)




url = "https://generic.wg.spotify.com/s4x-insights-api/v1/artist/7KzG8dszzwlSDGEsCbzANz/playlists/listener?time-filter=28day"
 header =  {
    "accept": "application/json",
    "accept-language": "en",
    "app-platform": "Browser",
    "authorization": "Bearer BQDWDWamKz0_72uiBHwSfQsU_YN4sk0sxdvA9FInDGS8VbGSwmArPz9cb72Nyu2qTwSunkTluLhUZ5CfgGHn1Mq5sNgQq-nxy1y0xt3v0z8a8lrjCop9fIx5axqK736xNFH4HjuZtRKaRO8qdy9T4ADGf-aWwPTX0-OwWc9I3i391YRaIZkd",
    "content-type": "application/json",
    "if-none-match": "\"MC-NDA5ZGJhNjcxOTA0YzM3NjE0ZDhjZGZmNzdhNzdjMDM=\"",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "spotify-app-version": "1.0.0.59061fb",
    "x-cloud-trace-context": "00000000000000001b6ff6fa478ff927/1567876910143310030;o=1"
  }
