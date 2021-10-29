# AtCoder AC Archive

[![CI Test](https://github.com/ivgtr/atcoder-ac-archive/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/ivgtr/atcoder-ac-archive/actions/workflows/test.yml) [![Publish to npm](https://github.com/ivgtr/atcoder-ac-archive/actions/workflows/publish.yml/badge.svg)](https://github.com/ivgtr/atcoder-ac-archive/actions/workflows/publish.yml)

AtCoder で AC したソースコードを GitHub 上 or ローカルに保存します

GitHub Actions を利用した自動収集とローカルでの実行が可能です

動いている[デモ](https://github.com/sumikkosoft/atcoder-ac-archive)

## Usages

#### Local

##### setup

```shell
$ npm install --global a3-cli
```

1. `a3 init` を実行し、初期設定を行ってください
1. `a3 config <PROPERTIES>` で設定を書き換える事ができます
1. `a3 config open` で設定ファイルのディレクトリが開くので直接設定を書き換えることもできます:
   - **config.user_id:** 利用する AtCoder の ID
   - **config.archive_dir:** ソースコードの保存先、指定しない場合は実行場所に保存される
   - **config.github_id:** commit に使用する GitHub ID
   - **config.github_email:** commit に使用する GitHub Email
1. `a3 archive` でコードを収集します

##### info

```shell
$ a3 [COMMAND] -h
```

#### GitHub Actions

##### Setup

1. このリポジトリ を Fork します
1. `.github/workflows/schedule.yml` の[環境変数](https://github.com/ivgtr/atcoder-ac-archive/blob/master/.github/workflows/update.yml#L30-L32) を編集します:
   - **USER_ID:** 利用する AtCoder の ID
   - **GH_ID:** commit に使用する GitHub の ID
   - **GH_EMAIL:** commit に使用する GitHub の Email
1. 環境変数はリポジトリの Secrets に登録しても直接書き換えても問題ないです
1. リポジトリの Actions タブを開き、GitHub Actions を有効化し、Update Workflows を有効化してください
1. スケジュール毎にコードが収集され、Fork したリポジトリの`atcoder.jp/<USER_ID>` ブランチに push されます

## 補足

- AtCoder Problems API へのリクエストと AtCoder へのスクレイピングを行っており、負荷軽減のためどちらも 1~1.5 秒程スリープを挟んで叩くようにしています
- AtCoder への負荷軽減と GitHub Actions のリミットの兼ね合いで、CI はスクレイピングの実行時間が 5 分を超えたタイミングで終了します
  - AC 数が多い方は全てのコードを取得するまでに GitHub Actions を何度か実行する必要があるかもしれません

## License

MIT ©[ivgtr](https://github.com/ivgtr)

[![Twitter Follow](https://img.shields.io/twitter/follow/ivgtr?style=social)](https://twitter.com/ivgtr) [![Github Follow](https://img.shields.io/github/followers/ivgtr?style=social)](https://github.com/ivgtr) [![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE) [![Donate](https://img.shields.io/badge/%EF%BC%84-support-green.svg?style=flat-square)](https://www.buymeacoffee.com/ivgtr)
