# Radicale Imap Authentication Plugin

Install the python module by running the following command in the same folder as `setup.py`:
```shell
python3 -m pip install --upgrade .
```

To use IMAP authentication in radicale adjust `auth` section in radicale config:
```ini
[auth]
type = radicale_imap_auth
imap_hostname = example.com
imap_port = 993
imap_ssl = True
```
Default values:

* `imap_hostname`: `localhost`
* `imap_port`: `143`
* `imap_ssl`: `False`

You can uninstall this module with:
```shell
python3 -m pip uninstall radicale_imap_auth
```
