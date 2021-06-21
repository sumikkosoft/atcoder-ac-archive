# AtCoder AC Archive

AtCoder で AC したソースコードを GitHub 上 or ローカルに保存します

GitHub Actions を利用した自動収集とローカルでの実行が可能な予定です

_※ 実装途中_

## Usages

#### Local

##### setup

```shell
$ npm install --global a3-cli
```

1. `a3 init` を実行し、初期設定を行ってください
1. `a3 config <PROPERTIES>` で設定を書き換える事ができます
1. `a3 config open` で直接設定を書き換えることもできます:
   - **config.user_id:** 利用する AtCoder の ID
   - **config.archive_dir:** 保存先のディレクトリ
   - **config.github_id:** commit に使用する GitHub ID
   - **config.github_email:** commit に使用する GitHub Email
   - **config.github_repository:** commit に使用する GitHub Remote Repository
1. `a3 archive` でコードを収集します

#### GitHub Actions

##### Setup

1. この repository を Fork します
1. `.github/workflows/schedule.yml` の[環境変数](https://github.com/ivgtr/atcoder-ac-archive/blob/master/.github/workflows/schedule.yml#L24-L31) を編集します:
   - **USER_ID:** 利用する AtCoder の ID
   - **GITHUB_ID:** commit に使用する GitHub ID
   - **GITHUB_EMAIL:** commit に使用する GitHub Email

## 進捗

- [x] CLI コマンドの追加
- [x] ローカルでのソースコードの取得・保存
- [x] 保存したソースコードを列挙・管理
- [ ] jest を書く
- [ ] npm.js に公開
- [ ] GitHub Actions の設定

## License

MIT ©[ivgtr](https://github.com/ivgtr)

[![Twitter Follow](https://img.shields.io/twitter/follow/ivgtr?style=social)](https://twitter.com/ivgtr) [![Github Follow](https://img.shields.io/github/followers/ivgtr?style=social)](https://github.com/ivgtr) [![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE) [![Donate](https://img.shields.io/badge/%EF%BC%84-support-green.svg?style=flat-square)](https://www.buymeacoffee.com/ivgtr)
