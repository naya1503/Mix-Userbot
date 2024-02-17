<p align="center">
  <img src="https://telegra.ph//file/19b336da463a05d7d8f8c.jpg" alt="Ayra Logo">
</p>
<h1 align="center">
  <b>Mix Userbot</b>
</h1>

<b>A stable pluggable Telegram userbot + Voice & Video Call music bot, based on Pyrogram</b>


[![Last Commit](https://img.shields.io/github/last-commit/naya1503/Mix-Userbot?color=red&logo=github&logoColor=blue&style=for-the-badge)](https://github.com/naya1503/Mix-Userbot/commits)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/naya1503/Mix-Userbot)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-blue)](https://GitHub.com/naya1503/Mix-Userbot/graphs/commit-activity)
[![CodeQuality](https://img.shields.io/codacy/grade/a723cb464d5a4d25be3152b5d71de82d?color=blue&logo=codacy)](https://app.codacy.com/gh/naya1503/Mix-Userbot/dashboard)
[![GitHub Forks](https://img.shields.io/github/forks/naya1503/Mix-Userbot?&logo=github)](https://github.com/naya1503/Mix-Userbot/fork)
[![GitHub Stars](https://img.shields.io/github/stars/naya1503/Mix-Userbot?&logo=github)](https://github.com/naya1503/Mix-Userbot/stargazers)
----

## Disclaimer

```
Saya tidak bertanggung jawab atas penyalahgunaan bot ini.
Bot ini dimaksudkan untuk bersenang-senang sekaligus membantu anda
mengelola grup secara efisien dan mengotomatiskan beberapa hal yang membosankan.
Gunakan bot ini dengan risiko Anda sendiri, dan gunakan userbot ini dengan bijak.
```

# DATABASE REQUIRETMENTS :
- MONGODB


<details>
<summary><b>🔗 Deploy Via Screen</b></summary>
<br>

• `sudo apt-get update && sudo apt-get upgrade -y`

• `sudo pip3 install -U pip`

• `sudo apt-get install python3-pip ffmpeg -y`

 • `git clone https://github.com/naya1503/Mix-Userbot`

 • `cd Mix-Userbot`

 • `pip3 install -r req*`

 • `cp .env.sample .env`

 • `nano .env`
 
  - isi vars .env api_id, api_hash, mongo_uri, db_name, session, owner_id
  - Jika sudah 
  - ketik ctrl + S
  - ctrl + X

 • `screen -S mix`

 • `bash run.sh`

</details>

<details>
<summary><b>🔗 Deploy Via Docker</b></summary>
<br>

• `curl -sSL https://get.docker.com | sh`

 • `git clone https://github.com/naya1503/Mix-Userbot`

 • `cd Mix-Userbot`

 • `cp .env.sample .env`

 • `nano .env`
 
  - isi vars .env api_id, api_hash, session, mongo_uri, db_name, owner_id
  - Jika sudah 
  - ketik ctrl + S
  - ctrl + X

 • `docker build . -t mix`

 • `docker run --name namalu --env-file .env -d -t mix`

</details>

<details>
<summary><b>🔗 Deploy on Heroku</b></summary>
<br>
• Silakan isi vars yang diperlukan api_id, api_hash, session, heroku_api, heroku_app_name, mongo_uri, db_name, dan owner_id

<h3 align="center">Click The Button</h3>
<a align="center" href="https://dashboard.heroku.com/new?template=https://github.com/naya1503/Mix-Userbot"><img src="https://www.herokucdn.com/deploy/button.svg"></a>
</div>

</details>


## © Credits & Thanks For
* [TeamUltroid](https://github.com/TeamUltroid) for [Ultroid](https://github.com/TeamUltroid/Ultroid)
* [Laky-64](https://github.com/Laky-64) for [PyTgCalls](https://github.com/pytgcalls/pytgcalls)
* [Risman](https://github.com/mrismanaziz) for [Man-Userbot](https://github.com/mrismanaziz/Man-Userbot)
* [AyiinXd](https://github.com/AyiinXd) for [Ayiin-Userbot](https://github.com/AyiinXd/Ayiin-Userbot)
* [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)
* [Kynan](https://github.com/naya1503) for [Mix-Userbot](https://github.com/naya1503/Mix-Userbot)

## Maintained By
* [![Kynan.](https://img.shields.io/static/v1?label=Ky&message=nan&color=critical)](https://t.me/kenapanan)




# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
Mix-Userbot is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.
