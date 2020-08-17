from mastodon import Mastodon

url = 'https://muknown.jp'

app = 'mstdn_random_tl_cli'

cid_file = 'client_id.txt'

Mastodon.create_app(
    app,
    api_base_url = url,
    to_file = cid_file
)